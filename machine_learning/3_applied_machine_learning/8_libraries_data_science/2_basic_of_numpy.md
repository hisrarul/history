## Numpy

Numpy is the fundamental package for scientific computing with Python. It contains among other things:
* A powerful N-dimensional array object
* Sophisticated (broadcasting) functions
* Tools for integrating C/C++ and Fortran code
* Useful linear algebra, Fourier transform, and random number capabilities

```python
# importing the numpy library
import numpy as np

# check version of the numpy library
np.__version__

# create a numpy array
np.array([1, 4, 3, 5, 3])
```


#### Difference between  numpy array and list
* Data type should be same of all the elements in a numpy array whereas it can be different in case of lists.
* Broadcasting

```python
# if we add an element of string data type in a numpy array
# then it will upcast the data type to string
np.array([1, 4, 2, '5', 3, False])
```

*Now, we will create one sample list and numpy array and apply a very basic function of multiplication by 2. We will see that in case of list the elements are duplicated and appended to the list whereas in case of numpy array we got an array where all elements are multiplied by 2*

```python
# create a sample list
sample_list = [1, 2, 3, 4, 5, 6]
sample_list*2

# create a sample numpy array
sample_numpy_array = np.array([1, 2, 3, 4, 5, 6])
sample_numpy_array+2
```


#### Create a matrix using numpy
a = 
$\left[\begin{array}{ccc}
[1,2,3],\\
[4,5,6],\\
[7,8,9]
\end{array}\right]$

```python
# MATRIX
a = np.array(a)

A[0][1]
```

* we can directly pass structure
```python
b = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]
])

# create a 3x3 array of random integers in the intreval (0,10)
np.random.randint(0, 10, (3, 3))

# create another matrix
np.random.randint(0, 10, (3,3))
```

#### Fix behavior of a random generator
```python
# fixing the random seed
np.random.seed(0)
np.random.randint(0, 10, (3,3))

# fixing the random seed

np.random.seed(0)
np.random.randint(0, 10, (3,3))
```

#### Create a matrix of Zeros of specific dimension
```python
# create a 2 X 10 integer array filled with zeros
np.zeros((3,4), dtype=int)

# create a 4X5 integer array filled with zeros
np.zeros((4,5), dtype=int)
```

#### Create a matrix of Ones of specific dimension
```python
# create a 2 X 10 integer array filled with ones
np.ones((2, 10), dtype=int)

# create a 4x5 integer array filled with one
np.ones((4,5), dtype=int)

# diagonal with 1
np.identity(5, dtype=int)
```


#### Create a matrix of filled with any specific number of specific dimension
```python
# create a 3x5 array filled with 3.14
np.full((3,5), 3.14)

# create a 2x4 array filled with 7
np.full((2,4), 7)
```


#### Array Concatenation
```python
# concatenating 2-D arrays
matrix1 = np.array([[1, 2, 3], [4,5,6]])

print("matrix 1")

matrix1

matrix2 = np.array([[7,8,9], [10,11,12]])

print("matrix 2")

matrix2
```

#### Concatenate Row wise
```python
# concatenate along the first axis
matrix_1_2_combineRowwise = np.concatenate([matrix1, matrix2, axis=0])
print("Combined on Row (axis=0)")

matrix_1_2_combineRowwise
```


#### Concatenate Column wise
```python
# concatenate along the first axis
matrix_1_2_combineColwise = np.concatenate([matrix1, matrix2, axis=1])
print("Combined on Row (axis=0)")

matrix_1_2_combineRowwise
```






