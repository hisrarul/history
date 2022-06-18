## Defensive Programming

1. Preventive measures to avoid or easily detect bugs in future
2. What to do when code encounters some unexptected condition

#### Enforced during implementation
* Document constraints and specification
* Document assumptions behind code design
* Identify boundary conditions for the code.

```python
def mutating_complex_operation(x):
    """
    Perform complex operation and mutation over the input data

    Parameters:
    x(pd.Series): data for which the complex operation is to be performed

    Returns(pd.Series): input data after complex operation mutation
    """
    mini = x.min()
    maxi = x.max()
    ...
    ...
    variance = x.var()
    ...
    ...
    return new_x
```
The function has assumed that input `x` is in the form of panda series. What will be happen if input `x` comes in python list rather than panda series. In that case, initial operation will work fine but the `variance` function will through the error because it is not define for the python list. This seems normal error but what if input `x` is result of some ml algorithm which tooks few hours to run. It has mutated right before the error has encountered. How can we prevent this loss of computation time to occur in the first place. This can be done by enforcing the assumptions of the code.


