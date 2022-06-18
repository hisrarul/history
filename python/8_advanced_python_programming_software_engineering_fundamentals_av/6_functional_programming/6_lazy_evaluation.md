## Lazy Evaluation
Lazy evaluation forms a mapping of operations and only performs them when the result is needed.

* Actions are only performed when the result is needed.
* Carried out with the help of a computation graph

#### Benefits
* It helps lazy evaluation to identify the areas in the mapping where the performance could be optimised.
* It can also provide parallelism, executing independently nodes simultaneously.

#### Computation Graph
Computation graph of heron's area formula

A = Area of the triangle
a,b,c = sides of the triangle
S = semi-perimeter

#### Jupyter Notebook
Defining fundamental operations
```python
def adder(a, b):
    return a + b
```

```python
def divider(a, b):
    return a / b
```

```python
def subtractor(a, b):
    return a - b
```

```python
def multiplier(a, b):
    return a * b
```

```python
def sqrt(a):
    return a ** (0.5)
```

#### Constructing operation specific to Herons Formula
```python
from functools import reduce, partial

def heron_adder(*values):
    """Can sum any number of values (3 in case of Heron's formula)"""
    return reduce(adder, values)

def heron_multiplier(values):
    """Can multiply any number of values (4 in case of heron's formula)"""
    return reduce(multiplier, values)
```

#### Function to perform Heron's Formula
Make use of above fundamental function to calculate area of triangle using herons formula.
```python
def herons_formula(a, b, c):
    """Computes area of triangle using heron's formula

    Parameters:
    a(float): first side of a triangle
    b(float): second side of a triangle
    c(float): third side of a triangle

    returns(float): area of triangle
    """
    semi_perimeter = divider(heron_adder(a, b, c), 2)
    a_difference = subtractor(semi_perimeter, a)
    b_difference = subtractor(semi_perimeter, b)
    c_difference = subtractor(semi_perimeter, c)
    insider_product = heron_multiplier([a_difference, b_difference, c_difference, semi_perimeter])
    final_area = sqrt(insider_product)

herons_formula(3, 4, 5)
```


