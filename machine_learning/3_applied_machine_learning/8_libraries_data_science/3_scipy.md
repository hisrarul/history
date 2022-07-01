## Scipy
It provides convenient and fast N-dimensinoal array manipulation.

```python
# import the scipy library
import scipy

# check the version of scipy
scipy.__version__
```

#### Compute the nth Derivate of a function
```python
# import the derivative from scipy
from scipy.misc import derivative

# define the function
def my_function(x):
    return x**2 + x + 1

# calculate the first derivative of the function at x = 2
derivative(func=my_function, x0=2)

derivative(func=my_function, x0=2, n=2)
```

Function: f(x) = x**2 + x + 1
Derivate: f'(x) = 2*x + 1
Solution: f'(2) = 2*2 + 1 = 5


#### Permutation and Combinations
```python
# Combinations
from scipy.special import comb

# total number of combinations from 4 different values takes 2 at a time value of 4C2
com = comb(4, 2)

print(com)
```

```python
# PERMUTATIONS: Value of 4P2
from scipy.special import perm
per = perm(4, 2)

print(per)
```


#### Linear Algebra
```python
# import linear algebra module and numpy
from scipy import linalg
import numpy as np

# square matrix
matrix = np.array([[1,5, 2],
                   [3,2,1],
                   [1,2,1]])

matrix

# pass values to det() function
linalg.det(matrix)

# inverse of a matrix
linalg.inv(matrix)
```