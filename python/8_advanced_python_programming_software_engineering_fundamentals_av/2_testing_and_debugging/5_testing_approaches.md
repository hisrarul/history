## Testing approaches

* Testing
    * Random testing
        * Random test cases
        * More test cases, more surety
    * Black box testing
        * Code is black box
        * Testing through docstrings
    * Glass box testing
        * Testing through code
        * All paths are explored
        * Exhaustive

#### Black box testing
* What are the natural boundaries in this logic?
```python
def absolute(value):
    """
    returns value if value is positive else returns negative value

    Parameters:
    value(float): value to calculate absolute of

    returns(float): absolute of value
    """
```

| Test Input | Expected Output |
| 1 | 1 |
| 0 | 0 |
| -1 | 1 |

#### Glass box testing
* Using code to design test cases
* Check every potential path
* Can be time taking and difficult to catch every path

* Guidelines for test cases:
    * branches: check for if-else
    * loops: check for break, continue, etc.
```python
def absolute(value):
    """
    returns value if value is positive else returns negative value

    Parameters:
    value(float): value to calculate absolute of

    returns(float): absolute of value
    """
    if value < -1:
        return -value
    else:
        return value
```

| Test input | Expected output | Actual output |
| 2 | 2 | 2 |
| -2 | 2 | 2 |


