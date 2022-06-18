## Bug

#### Categories of Bug
* Based on visibility, bug has been categories.
    1. Overt
    2. Covert

* Based on Consistency
    1. Persistent
    2. Intermittent

#### Overt Bugs
Overt bugs are obvious to catch, code crashes or run forever.
```python
def calculate_factorial(value):
    """
    Calculates and returns factorial of the given value

    Parameters:
    value(int): value for which factorial is to be calculated

    returns(int): the calculated factorial
    """
    fact = value * calculate_factorial(value - 1)
```

This example is calculating factorial using recursion but recursion does not know when to stop.

#### Covert Bugs
Covert bugs are not obvious to catch, code returns abnormal value.

Implementation of Logic is Flawed

```python
def area_of_circle(radius):
    """Calculates area of a circle - pi*radius**2

    params:
    radius(float): Radius of the circle

    returns(float): Area of circle
    """
    return 3.114*radius**2
```
In this example, the value of Pi is incorrect. Hence, everytime will result incorrect answer.


#### Persistent 
Persistent bugs appear everytime the code is run. They are highly reproducible. Like in above example of area of circle, the value of Pi.

#### Intermittent
Intermittent bugs are only visible under special circumstances. They are not easily reproducible.

```python
def absolute(value):
    """
    returns value if value is positive else return negative value

    Parameters:
    value(float): value to calculate absolute of

    returns(float): absolute of value
    """
    if value < 1:
        return - value
    else:
        return value
```

#### Categories of Bugs
* Overt and Persistent
    * Obvious to detect, reproducible
    * Defensive programming ensures bug fall into this category

* Overt and Intermittent
    * Harder to debug, somewhat reproducible
    * If spotted, can be handled

* Covert and Intermittent
    * Highly Dangerous
    * Takes a long time to event detect
