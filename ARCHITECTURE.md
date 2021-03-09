# Current Plan

It's very unlikely that the number of events on a calendar will cause
performance problems, because humans can only do so much.
So let's put aside scalability for now, and store our data in as general of
a way as possible.

We'll store our data as an `sqlite3` database for now.

The table structure will be as follows:

- `Events(Event ID, Event Name, Event Description)`
- `Dependencies(Event ID, Dependent Event's ID)`

Later, we'll use Xapian or FTS5 to index/search our data.
