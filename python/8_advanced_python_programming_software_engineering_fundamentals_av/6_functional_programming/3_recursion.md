## Recursion

* Recursion
    * Avoids mutation of variables
    * Code design may become simpler
    * Uses computation graph
    * Computationally expensive in Python


#### Factorial Example
```python
%load_ext lab_black

def imperative_factorial(value):
    """Calculate and returns factorial of a number

    Parameters:
    value(int): value to calculate factorial of

    returns(int): final resulting factorial
    """
    final_factorial = 1
    for number in range(1, value+1):
        final_factorial = number * final_factorial #variable final_factorial is being mutated every iteration
    return final_factorial

imperative_factorial(6)
```

#### Functional factorial
* We can see that there is no assignment operator being used which means there is no overwriting of variables happening
* Moreover, the code looks cleaner and simpler.
```python
def functional_factorial(value):
    """Calculate and returns factorial of a number

    Parameters:
    value(int): value to calculate factorial of

    returns(int): final resulting factorial
    """
    if value <= 1:
        return 1
    else:
        return value * functional_factorial(value - 1)
```

#### Fibonacchi Numbers
The fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21...
where every nth term is a sum of previous two terms.
```python
def imperative_fibonacchi(n_terms):
    n1, n2 = 0, 1
    count = 0
    output = []
    if n_terms == 1:
        print(n1)
    else:
        while count < n_terms:
            output.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
    print(output)

imperative_fibonacchi(7)
Number of mutations = ?
Complexity of code = ?
```

#### Funtional prog fro fibonacchi numbers
```python
def functional_fibonacchi(n_terms):
    if n_terms <= 1:
        return n_terms
    else:
        return functional_fibonacchi(n_terms - 1) + functional_fibonacchi(n_terms - 2)

[functional_fibonacchi(i) for i in range(0, 7)]
```





