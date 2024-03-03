## Lecture 11: Mutable Sequence

* Mutation is that when you change one variable, another value bounded to it also change at the same time
* Example: List, Dictionary; While tuple is the immutable sequence, it contains mutable value as an element.

```python
def f(s=[]):
    s.append(5)
    return len(s)
f()
f()
f()
	
```

* The output above is $1,2,3$, since the default ```s``` has been changed during the execution. Thus the mutation can be dangerous.

## Mutable Functions

* Nonlocal
