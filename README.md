# annealing-counter-python

A Python implementation of an annealing counter.

## Getting Started

```
>>> from counter import AnnealingCounter

>>> c = AnnealingCounter(alpha=0.9)
>>> c
Counter has value 0.0 at time 0.0

>>> c.increment()
>>> c
Counter has value 1.0 at time 0.0
>>> c.increment(t=0.5, amount=3.2)
>>> c
Counter has value 4.14868329805 at time 0.5
>>> c.increment()
>>> c
Counter has value 5.14868329805 at time 0.5

>>> c.get_value()
5.148683298050514
>>> c.get_value(t=2.0)
4.396022866630942
```
