## Higher Order Functions

* Can take function as argument
* Can return function
* A function extender (Decorator) -> can extend preexisting function capability without modifying pre-existing function.

#### Function as parameter
map(function, iterable)
```python
def squared(value):
    return value ** 2

iterable = [1, 2, 3, 4, 5]
new_list = list(map(squared, iterable))

new_list
```

#### Using lambda

```python
squared = lambda value: value ** 2

iterable = [1, 2, 3, 4, 5]
new_list = list(map(squared, iterable))

new_list
```

OR

```python
iterable = [1, 2, 3, 4, 5]
new_list = list(map(lambda value: value ** 2, iterable))

new_list
```

#### filter(function, iterable)
```python
def even(value):
    return value % 2 == 0

iterable = [1, 2, 3, 4, 5]
new_list = list(filter(even, iterable))

new_list
```

```python
even = lambda value: value % 2 == 0

iterable = [1, 2, 3, 4, 5]
new_list = list(filter(even, iterable))

new_list
```

```python
iterable = [1, 2, 3, 4, 5]
new_list = list(filter(lambda value: value % 2 == 0, iterable))

new_list
```

#### functools.reduce(function, iterable)
```python
from functools import reduce

iterable = [1, 2, 3, 4, 5]

multiplier = lambda x,y: x*y

factorial = reduce(multiplier, iterable)
factorial
```

```python
from functools import reduce
adder = lambda x,y: x+y

cum_sum = reduce(adder, iterable)
cum_sum
```

#### Function as a return of another function
In this exmaple, adding is the main function to which values are passwed (either 2 or 3 values).

appropriate_adder is used to determine whether a sum of two numbers is to be carried out or a sum of three numbers. Returns the appropriate function.

```python
def add_two_nums(x, y):
    return x + y

def add_three_nums(x, y, z):
    return x + y + z

def appropriate_adder(values):
    """Finds out whether there are two number or three numbers to add, returns corresponding function"""
    assert len(values) in (2, 3), "Invalid number of values, Only enter two or 3 digits"
    if len(values) == 3:
        return add_three_nums
    else:
        return add_two_nums
    
def adding(*values):
    """Will only work for two or three values"""
    adder = appropriate_adder(values)
    return adder(*values)

```

Question: Key characteristic of a higher order function
* They can return a function
* They can take a function as parameter

Question:  Key purpose of Higher order function
* It is used to extend the fuctionality of an existing function
* It allows re-use of a function without overwriting the original function.


