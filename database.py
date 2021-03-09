"""Interface with the Hookster Database"""


import sqlite3
import os.path
import uuid


class Event:
    """Represents a single Calendar Event"""
    def __init__(self, name, description):
        self.id = _generate_uuid()
        self.name = name
        self.description = description

    def __str__(self):
        return f'({self.id}, {self.name}, {self.description})'

    def _setId(self, id):
        self.id = id


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

        if isinstance(event, Event):
            event_id = event.id
        else:
            event_id = event
        if isinstance(dependency, Event):
            dependency_id = dependency.id
        else:
            dependency_id = dependency

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
            event = Event(row[1], row[2])
            event._setId(row[0])
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
                FOREIGN KEY(prerequisite) REFERENCES Events(id)
                FOREIGN KEY(event) REFERENCES Events(id))
            """)


def _generate_uuid():
    return str(uuid.uuid1())
