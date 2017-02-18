# annealing-counter-python

A Python implementation of an annealing counter.

## Getting Started

```
>>> from counter import AnnealingCounter
>>> c = AnnealingCounter(alpha=0.9)
>>> c
Counter value at time 0.0: 0.0
>>> c.increment()
>>> c
Counter value at time 0.0: 1.0
>>> c.increment(amount=5)
>>> c
Counter value at time 0.0: 6.0
>>> c.increment(t=1.1)
>>> c
Counter value at time 1.1: 6.34340399431
>>> c
Counter value at time 1.1: 6.34340399431
>>> c.get_value(10)
2.4835945910305464
>>> c.get_value(100)
0.00018919364956576542
```
