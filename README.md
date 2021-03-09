# Hookster

Hookster is an event-based human scheduler.

*NOTE*:
This project is in its infancy, and is not yet ready for use.
Because the goals of the project are still changing, there's a good chance this
documentation isn't even ready for use.

## Motivation

I'm a very forgetful person when it comes to scheduling.

I work around this by using technology; Google Calendar tells me when to wake
up, when my homework is due, and when to call my friends.
However, I often find myself in situations like this:

1. I send an email to person X.
2. I think: "When I get a response from X, I should text Y".
3. I get a response from X.
4. I forget to text Y.

Or sometimes like this:

1. I send an email to person X.
2. Person X doesn't respond.
3. I forget I sent the email, and don't follow up.

Google Calendar is great for situations where progress is "blocking" on me, but
falls short where I'm blocking on other people.
I want a tool that gives me "hooks" on event initiation and completion.
It should be:

- *Scriptable*: This program should be a "good UNIX CLI program". I should be
  able to integrate it into my existing shell scripts -- this will probably
  entail some sort of `fzf` style interface or keyword parsing.
- *Interoperable*: I want this tool to integrate with Google Calendar.
- *Simple*: I'm trying to save time, not waste it. If this program takes more
  than 5-10 seconds to use, I've failed.

My initial design was a to-do list with dependencies and hooks, so the project
is called Hookster.


## Architecture

We'll store our data as an `sqlite3` database, in the following form:

- `Events(Event ID, Event Name, Event Description)`
- `Dependencies(Event ID, Dependent Event's ID)`

Later, we'll use Xapian or FTS5 to index/search our data.
