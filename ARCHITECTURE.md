# Current Plan

It's very unlikely that the number of events on a calendar will cause
performance problems, because humans can only do so much.
So let's put aside scalability for now, and store our data in as general of
a way as possible.

We'll store our data as an `sqlite3` database for now.

- `Events(Event ID, Event Name, Event Description)`
- `Dependencies(Event ID, Dependent Event's ID)`
