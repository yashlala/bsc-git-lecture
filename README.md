# Hookster

Hookster is an event-based human scheduler. 

Basically, it's my attempt to bring CPU scheduling into my life. 

## Motivation 

I use Google Calendar to organize my life. 

However, it doesn't cover a lot of usecases. 

1. I send an email. 
2. I think "When I get a response from X, I should text Y".
3. I get a response from X. 
4. I forget to text Y. 


basically its like a pacman or git hook; every time you check off an event as
complete, it prompts you for the next thing to do. It'll maintain an event
queue (async lyfe) so you can handle blocking tasks easily. 

now you can manage different threads of execution in your life without
forgetting 90% of what's going on during the context switch. 

TLDR: 

- Google calendar already works as a great interrupt pin. 
- To-do lists work as limited queues. 
- callbacks aren't a thing. smarter queues aren't a thing. context switch
  between tasks aren't automatic. 

think it through yo
python lets gooo

## Goals

Google Tasks integration

...is this basically a convenient to-do list with a dependency tree? 
I want it to work well with calendars too
