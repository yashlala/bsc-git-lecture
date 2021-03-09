# Hookster

Hookster is an event-based human scheduler.

## Motivation

I use Google Calendar to organize my life.

However, it doesn't cover a lot of usecases.

1. I send an email.
2. I think "When I get a response from X, I should text Y".
3. I get a response from X.
4. I forget to text Y.


# NOTE

This project is in its infancy, and is not yet ready for use.
Even this documentation isn't ready for use.
Go look somewhere else.

# PERSONAL

basically its like a pacman or git hook; every time you check off an event as
complete, it prompts you for the next thing to do. It'll maintain an event
queue so you can handle "blocking" tasks easily.

now you can manage different threads of execution in your life without
forgetting 90% of what's going on during the context switch.

TLDR:

- Google calendar already works as a great "interrupt pin".
- To-do lists work as limited queues.
- callbacks aren't a thing. smarter queues aren't a thing. context switch
  between tasks aren't automatic. want to make a tool that fills in the gaps
  between these existing scheduling solutions, so I can stop forgetting events.

## Goals

Google Tasks integration

...is this basically a convenient to-do list with a dependency tree?
I want it to work well with calendars too...
