"""This module provides an implementation of Hookster's database methods."""


import sqlite3
import os.path
import uuid


class Event:
    """Represents a single Calendar Event.

    Every event is generated with a unique ID, unless otherwise specified.
    """
    def __init__(self, name, description, id=None):
        self.id = _generate_uuid() if id == None else id
        self.name = name
        self.description = description

    def __str__(self):
        return f'({self.id}, {self.name}, {self.description})'

    def __eq__(self, other):
        try:
            return self.id == _extract_key(other)
        except TypeError:
            return False


class HooksterDatabase:
    def __init__(self, db_file):
        new_database = not os.path.exists(db_file)
        self.connection = sqlite3.connect(db_file)
        if new_database:
            self._create_tables()

    def sync(self):
        """Write the database state to disk."""
        self.connection.commit()

    def close(self):
        """Close the database, writing to disk."""
        self.sync()
        self.connection.close()

    def insert_event(self, event):
        """Insert an event into the database.

        Returns a handle to the inserted event.
        """
        return self.insert_events([event])[0]

    def insert_events(self, events):
        """Insert a list of Events into the database.

        Returns a list of handles to the inserted events.
        """

        # TODO: use executeMany instead
        cursor = self.connection.cursor()
        handles = []
        for event in events:
            handles.append(event.id)
            cursor.execute("INSERT INTO Events VALUES (?, ?, ?)",
                    (event.id, event.name, event.description))

        self.sync()
        return handles

    def insert_dependency(self, event, dependency):
        """Associates 2 events to represent a dependency.

        Accepts either Events or handles to Events.
        """

        event_id = _extract_key(event)
        dependency_id = _extract_key(dependency)

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Dependencies VALUES (?, ?)",
                (event_id, dependency_id))

        self.sync()

    def search_events(self, pattern):
        """Returns events with names matching the given pattern"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Events WHERE name LIKE '%' || ? || '%'",
                (pattern,))
        results = cursor.fetchall()
        events = []
        for row in results:
            event = Event(row[1], row[2], id=row[0])
            events.append(event)

        return events

    def find_direct_dependencies(self, event):
        """Returns all events that are direct dependencies of event.

        Arguments: event should be an Event or a db handle to an Event.
        Returns: A list of dependency events.
        """

        key = _extract_key(event)
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT E.id, E.name, E.description
            FROM Events E, Dependencies D
            WHERE (D.prerequisite = ? AND E.id = D.event)""",
            (key,))
        results = cursor.fetchall()
        events = []
        for row in results:
            event = Event(name=row[1], description=row[2], id=row[0])
            events.append(event)
        return events

    def _create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE Events (
                id TEXT,
                name TEXT,
                description TEXT,
                PRIMARY KEY (id))
            """)

        cursor.execute("""
            CREATE TABLE Dependencies (
                prerequisite TEXT,
                event TEXT,
                FOREIGN KEY(prerequisite)
                    REFERENCES Events(id)
                    ON DELETE CASCADE,
                FOREIGN KEY(event)
                    REFERENCES Events(id)
                    ON DELETE CASCADE)
            """)


def _generate_uuid():
    """Create a random UUID."""
    return str(uuid.uuid1())


def _extract_key(obj):
    """Convert a handle or Event handle into a Database Event ID."""
    if isinstance(obj, Event):
        return obj.id
    elif isinstance(obj, str):
        return obj

    raise TypeError('Must provide an Event or Event handle (string)')
