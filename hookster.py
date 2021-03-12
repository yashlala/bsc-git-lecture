#!/usr/bin/env python

from hookster.database import Event, HooksterDatabase

db = HooksterDatabase('hookster.db')

event = Event('wait for simba to respond', 'why isnt he checking his email')
db.insert_event(event)
handle = db.insert_event(Event('forward simbas response to nala', 'let her deal with it'))
# Works with both database handles and with the original objects.
db.insert_dependency(event, handle)

for event in db.find_direct_dependencies(*db.search_events('wait')):
    print(event)

# vim: ft=python
