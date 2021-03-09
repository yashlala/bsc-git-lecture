#!/usr/bin/env python

from hookster.database import Event, HooksterDatabase

db = HooksterDatabase('hookster.db')

event = Event('wait for simba to respond', 'why isnt he checking his email')
db.insert_event(event)
handle = db.insert_event(Event('forward simbas response to nala', 'let her deal with it'))
# Works with both database handles and with the original objects.
db.insert_dependency(event, handle)

print(list(map(str, db.search_events('nala'))))

# vim: ft=python
