## Typing in Python

* Promoting the expectations of the function

* May, or may not enforce the function expectation

```python
def calculate_factorial(x):
```

```python
def calculate_factorial(x: int) -> int:
```

#### Enforce Python typing

Example of factorial

```python
def factorial(x: int) -> int:
    """Returns factorial of the number

    params:
    x(int): positive integer

    returns(int): factorial of number x
    """
    if x < 0:
        return None
    elif x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    
# testing code
test_cases = [0, 1, 2, 3, 4, 6, 2.3]
for case in test_cases:
    print(factorial(case))
```
Here, we will get the error at the floating value `2.3` but now user has instruction to input `int` only. To enforce python typing, we need to follow steps:

```bash
pip3 install mypy
mypy factorial_test.py
```

This will be clear output what is the issue with the code.



