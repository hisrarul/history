## Exception Handling

* do something <- True <- check condition -> False -> do something else

* Finally wind up code <- Else run default code <- `Runs successfully` <- Try something -> `Something unexpected` -> Run exception code -> Finally wind up code

#### Example
```python
def divisor():
    """
    Asks for two numbers as input and prints the quotient
    """
    try:
        a = int(input("Tell me a number"))
        b = int(input("Tell me another number"))
    except ValueError:  # 5/a
        print("Input could not be converted to a number")
    try:
        print(a / b)
    except ZeroDivisionError:   # (5,0)
        print("Can not divide by zero")
```

#### Asking for input until user inputs right value
```python
def persuasive_divisor():
    """
    Asks for two numbers as input and prints the quotient
    """
    while True:
        try:
            a = int(input("Tell me a number"))
            b = int(input("Tell me another number"))
        except ValueError:  # 5/a
            print("Input could not be converted to a number")
        try:
            print(a / b)
            break
        except ZeroDivisionError:   # (5,0)
            print("Can not divide by zero")
        except UnboundLocalError as ule:
            print("Could not perform division because of bad inputs: ")
```
persuasive_divisor()
1 inputs: a
2 input: 5, 0
3 input: 5, 1


#### Circumventing unexpected condition
```python
def strange_operation(iterable):
    """Returns ratio of Variance to Standard deviation multiplied to every element of iterable

    iterable(pandas.Series): a series of numerical values

    returns(float): pd.Series with strange operation implemented
    """
    variance = iterable.var()
    standard_deviation = iterable.std()
    ratio = variance/standard_deviation
    return iterable.map(lambda x: x * ratio)
```

* Test with panda series
```python
import pandas as pd
import numpy as np

strange_operation(pd.Series([1, 2, 3, 4, 5]))
```

* Test with list
```python
strange_operation([1, 2, 3, 4, 5])  # it will give error
```

```python
def robust_strange_operation(iterable):
    """Returns ratio of Variance to Standard deviation multiplied to every element of iterable
    
    iterable(pandas.Series): a series of numerical values

    returns(float): pd.Series with strange operation implemented
    """
    try:
        variance = iterable.var()
        standard_deviation = iterable.std()
    except AttributeError as ae:
        print("Input not in pandas.Series format, Trying to convert: ", ae)
        assert type(iterable) in (pd.Series, list), "input not convertible either"
        iterable = pd.Series(iterable)
        variance = iterable.var()
        standard_deviation = iterable.std()
    finally:
        ratio = variance/standard_deviation
        return iterable.map(lambda x: x * ratio)
```

* Test
```python
robust_strange_operation(pd.Series([1, 2, 3, 4, 5]))

robust_strange_operation([1, 2, 3, 4, 5])

robust_strange_operation(np.array([1, 2, 3, 4, 5])) # need to add exception for nd.array
```

