# annealing-counter-python

A Python implementation of an annealing counter.

* The counter exponentially decays over time; controlled by the rate `alpha`
* When you read and write the counter, you provide a time index (increment or read the counter at time t)
* You can read the counter in the present and future (w.r.t. index of last increment), but not in the past
* Time indices of sequential increments must be weakly monotonically increasing

## Getting Started

```
>>> from counter import AnnealingCounter

>>> c = AnnealingCounter(alpha=0.9)
Counter has value 0.0 at time 0.0

>>> c.increment()  # increment by 1.0, but don't move time forward
Counter has value 1.0 at time 0.0
>>> c.increment(amount=3.2, t=0.5)  # increment by 3.2 and move time forward (t=0.5)
Counter has value 4.14868329805 at time 0.5
>>> c.increment()  # increment by 1.0, but don't move time forward
Counter has value 5.14868329805 at time 0.5


>>> c.get_value()  # get value as after last increment (t=0.5)
5.148683298050514
>>> c.get_value(t=2.0)
4.396022866630942  # get future value (t=2.0)
```
