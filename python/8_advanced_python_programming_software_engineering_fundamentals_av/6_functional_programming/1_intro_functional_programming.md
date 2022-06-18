## Functional Programming


#### Imperative Programming
* Code is written/run sequentially
* Focus on the procedure we take to reach what we want

#### Example of imperative programming
```python
def descriptives(iterable):
    """Calculates and returns descriptive of the iterable"""
    SIZE = len(iterable)
    # Calculating Mean
    total = 0
    for value in iterable:
        total = total + value
    mean = total / SIZE
    # Calculating Variance
    squared_difference_sum = 0
    for value in iterable:
        difference = value - mean
        squared_difference = difference ** 2
        squared_difference_sum = squared_difference_sum + squared_difference
        variance = squared_difference_sum / SIZE
        # Calculating Standard Deviation
        standard_deviation = variance ** (0.5)
        return mean, variance, standard_deviation

descriptives([1, 2, 3, 4, 5, 6])
```

#### Imperative Square
* Code is written/run sequentially
```python
def imperative_square():
    for i in range(1, 100000):
        i ** 2

%timeit imperative_square()
```
In this example, only square of the single element is being calculated at single iteration.

Squaring is number is an independent task why we do sequentially. Can we do it in parallel? We can do that using `map` function.
The `map` function removes the sequential nature of the loop. This happens because of *lazy evaluation*.
```python
def functional_square():
    map(lambda x: x ** 2, range(1, 100000))

%timeit functional_square()
```

#### Example of functional programming
```python
def mean(iterable):
    return sum(iterable) / len(iterable)

def variance(iterable):
    MEAN = mean(iterable)
    SIZE = len(iterable)
    squared_deviation = map(lambda x: (x - MEAN) ** 2, iterable)
    squared_deviation_sum = sum(squared_deviation)
    result = squared_deviation_sum / SIZE
    return result

def descriptives(function_list, iterable):
    """Runs all the functions in function list over the iterable and returns result list in same order"""
    return list(map(lambda f: f(iterable), function_list))

descriptives([mean, variance, standard_deviation], [1, 2, 3, 4, 5, 6])
```

#### Functional Programming Overview
* A new programming paradigm
* Focus: what to solve
* Uses pure functions
* Immutable variables
* Recursion over loops
* Higher order functions
* Everything is a mathematical expression
* Lazy Evaluation
