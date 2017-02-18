# annealing-counter-python

A Python implementation of an annealing counter.

* When you read and write the counter, you provide a time index (increment or read the counter at time t)
* Sequential time indices of increments must be weakly monotonically increasing
* The counter will decay exponentially over time; controlled by the rate `alpha`
* You can read the counter in the present and future, but not in the past.

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
