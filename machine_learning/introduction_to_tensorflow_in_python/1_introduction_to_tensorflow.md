## Introduction to TensorFlow

#### Constants and Variables
Two basic objects of computation:
1. constants
2. variables

#### What is TensorFlow?
* Open-source library for graph-based numerical computation
    * Developed by the Google brain team
* Low and high level APIs
    * Addition, multiplication, differentiation
    * Machine learning models
* Important changes in TensorFlow 2.0
    * Eager execution by default
    * Model bulding with Keras and Estimators

#### What is a tensor?
* Generalization of vectors and matrices
* Collection of numbers which is arranged into particular shape
* Specific shape

#### Defining tensors in TensorFlow
```python
import tensorflow as tf

# 0D Tensor
d0 = tf.ones((1,))

# 1D Tensor
d1 = tf.ones((2,))

# 2D Tensor
d2 = tf.ones((2, 2))

# 3D Tensor
d3 = tf.ones((2, 2, 2))

# Print the 3D Tensor
print(d3.numpy())
```

#### Defininf constants in TensorFlow
* A constant is the simplest category of tensor
    * Not trainable
    * Can have any dimension
```python
from tensorflow import constant

# Define a 2x3 constant
a = constant(3, shape=[2, 3])

# Define a 2x2 constant
b = constant([1, 2, 3, 4], shape=[2, 2])
```

#### Using convenience function to define constants
| Operation | Example |
|-----------|---------|
| tf.constant() | constant([1, 2, 3]) |
| tf.zeros() | zeros([2, 2]) |
| tf.zeros_like() | zeros_like(input_tensor) |
| tf.ones() | ones([2, 2]) |
| tf.ones_like() | ones_like(input_tensor) |
| tf.fill() | fill([3, 3], 7) |

#### Defining and initializing variables
```python
import tensorflow as tf

# Define a variable
a0 = tf.Variable([1, 2, 3, 4, 5, 6], dtype=tf.float32)
a1 = tf.Variable([1, 2, 3,, 4, 5,6], dtype=tf.int16)

# Define a constant
b = tf.constant(2, tf.float32)

# Compute their product
c0 = tf.multiply(a0, b)
c1 = a0*b
```

#### Exercise: Defining data as constants
Transform a numpy array, `credit_numpy`, into a tensorflow constant, `credit_constant`. This array contains feature columns from a dataset on credit card holders.
```python
# Import constant from TensorFlow
from tensorflow import constant

# Convert the credit_numpy array into a tensorflow constant
credit_constant = constant(credit_numpy)

# Print constant datatype
print('\n The datatype is:', credit_constant.dtype)

# Print constant shape
print('\n The shape is:', credit_constant.shape)
```

#### Exercise: Defining variables
* Define a variable, A1, as the 1-dimensional tensor: [1, 2, 3, 4].
* Apply .numpy() to A1 and assign it to B1.
```python
# Define the 1-dimensional variable A1
A1 = Variable([1, 2, 3, 4])

# Print the variable A1
print('\n A1: ', A1)

# Convert A1 to a numpy array and assign it to B1
B1 = A1.numpy()

# Print B1
print('\n B1: ', B1)
```

#### Basic operations

#### Applying the addition operator
```python
# Import constant and add from tensorflow
from tensorflow import constant, add

# Define 0-dimensional tensors
A0 = constant([1])
B0 = constant([2])

# Define 1-dimensional tensors
A1 = constant([1, 2])
B1 = constant([3, 4])

# Define 2-dimensional tensors
A2 = constant([[1, 2], [3,4]])
B2 = constant([[5, 6], [7, 8]])
```

#### Applying the addition operator
```python
# Perform tensor addition with add()
C0 = add(A0, B0)
C1 = add(A1, B1)
C2 = add(A2, B2)
```

#### Performing tensor addition
* The `add()` operation performs *element-wise addition*  with two tensors
* Element-wise addition requires both tensors to have the same shape:
    * Scalar addition: 1 + 2 = 3
    * Vector addition: [1,2] + [3,4] = [4,6]
    * Matrix addition: $\left[\begin{array}{ccc}1 & 2\\3 & 4\end{array}\right]$  $\left[\begin{array}{ccc} 3 & 4\\ 5 & 6 \end{array}\right]$  = $\left[\begin{array}{ccc} 4 & 6\\ 6 & 8 \end{array}\right]$
    * The `add()` operator is overloaded

#### How to perform multiplication in TensorFlow
* Element-wise multiplication performed using `multiply()` operation
    * The tensors multiplied must have the same shape
    * E.g. [1,2,3] and [3,4,5] or [1,2] and [3,4]
* Matrix multiplication performed with `matmul()` operator
    * The `matmul(A,B)` operation multiplies A by B
    * Number of columns of A must equal the number of rows of B

#### Applying the multiplication
```python
# Import operators from tensorflow
from tensorflow import ones, matmul, multiply

# Define tensors
A0 = ones(1)
A31 = ones([3, 1])
A34 = ones([3, 4])
A43 = ones([4, 3])
```

* What types of operations are valid?
    * `multiply(A0, A0)`, `multiply(A31, A31)`, and `multiply(A34, A34)`
    * `matmul(A43, A34)`, but not `matmul(A43, A43)`

#### Summing over tensor dimensions
* The `reduce_sum()` operator sums over the dimension of a tensor
    * `reduce_sum(A)` sums over all dimensions of A
    * `reduce_sum(A, i)` sums over dimension i
```python
# Import operations from tensorflow
from tensorflow import onces, reduce_sum

# Define 1 2x3x4 tensor of ones
A = ones([2, 3, 4])
```

```python
# Sum over all dimensions
B = reduce_sum(A)

# Sum over dimensions 0, 1, and 2
B0 = reduce_sum(A, 0)
B1 = reduce_sum(A, 1)
B2 = reduce_sum(A, 2)
```

#### Exercise: Performing element-wise multiplication
Element-wise multiplication in TensorFlow is performed using two tensors with identical shapes. This is because the operation multiplies elements in corresponding positions in the two tensors. An example of an element-wise multiplication

$\left[\begin{array}{ccc}1 & 2\\3 & 4\end{array}\right]$ * $\left[\begin{array}{ccc} 3 & 4\\ 5 & 6 \end{array}\right]$  = $\left[\begin{array}{ccc} 4 & 6\\ 6 & 8 \end{array}\right]$

* Define the tensors A1 and A23 as constants.
* Set B1 to be a tensor of ones with the same shape as A1.
* Set B23 to be a tensor of ones with the same shape as A23.
* Set C1 and C23 equal to the element-wise products of A1 and B1, and A23 and B23, respectively.

```python
# Define tensors A1 and A23 as constants
A1 = constant([1, 2, 3, 4])
A23 = constant([[1, 2, 3], [1, 6, 4]])

# Define B1 and B23 to have the correct shape
B1 = ones_like(A1)
B23 = ones_like(A23)

# Perform element-wise multiplication
C1 = multiply(A1, B1)
C23 = multiply(A23, B23)

# Print the tensors C1 and C23
print('\n C1: {}'.format(C1.numpy()))
print('\n C23: {}'.format(C23.numpy()))
```

#### Exercise: Making predictions with matrix multiplication
This process will yield a vector of parameters that can be multiplied by the input data to generate predictions. In this exercise, you will use input data, features, and a target vector, bill, which are taken from a credit card dataset we will use later in the course.

features = $\left[\begin{array}{ccc}2 & 24\\2 & 26\\2 & 57\\1 & 37\end{array}\right]$, bill = $\left[\begin{array}{ccc} 3913 \\2682 \\8617 \\64400\end{array}\right]$, params = $\left[\begin{array}{ccc} 1000 \\ 150 \end{array}\right]$

The matrix of input data, features, contains two columns: education level and age. The target vector, bill, is the size of the credit card borrower's bill.

Since we have not trained the model, you will enter a guess for the values of the parameter vector, params. You will then use matmul() to perform matrix multiplication of features by params to generate predictions, billpred, which you will compare with bill. Note that we have imported matmul() and constant().

* Define features, params, and bill as constants.
* Compute the predicted value vector, billpred, by multiplying the input data, features, by the parameters, params. Use matrix multiplication, rather than the element-wise product.
* Define error as the targets, bill, minus the predicted values, billpred.
```python
# Define features, params, and bill as constants
features = constant([[2, 24], [2, 26], [2, 57], [1, 37]])
params = constant([[1000], [150]])
bill = constant([[3913], [2682], [8617], [64400]])

# Compute billpred using features and params
billpred = matmul(features, params)

# Compute and print the error
error = bill - billpred
print(error.numpy())
```

#### Exercise: You've been given a matrix, wealth. This contains the value of bond and stock wealth for five individuals in thousands of dollars.

wealth = $\left[\begin{array}{ccc}11 & 50\\7 & 2\\4 & 60\\ 3 & 0\\25 & 10\end{array}\right]$
 

The first column corresponds to bonds and the second corresponds to stocks. Each row gives the bond and stock wealth for a single individual. Use wealth, reduce_sum(), and .numpy() to determine which statements are correct about wealth.

Hint:
* reduce_sum(wealth,1) will sum wealth over its rows.
* reduce_sum(wealth,0) will sum wealth over its columns.
* Note bonds appear first and stocks appear second in reduce_sum(wealth,0).
* You can append .numpy() to reduce_sum() to convert the results to a numpy array. 

    e.g. `reduce_sum(wealth, 0).numpy()`

Answer:

Combined, the 5 individuals hold $50,000 in bonds.

#### Overview of Advanced operations

| Operation | Use |
|-----------|-----|
| gradient() | Computes the slope of a function at a point |
| reshape() | Reshapes a tensor (e.g. 10x10 to 100x1)
| random() | Populates tensor with entries drawn from a probability distribution |

#### Finding the optimum
* In many problems, we will want to find the optimum of a function.
    * Minimum: Lowest valut of a loss function.
    * Maximum: Highest value of object function.
* We can do this using the `gradient()` operation.
    * Optimum: Find a point where gradient = 0.
    * Minimum: Change in gradient > 0
    * Maximum: Change in gradient < 0

#### Gradients in TensorFlow
```python
# Import tensorflow under the alias tf

import tensorflow as tf

# Define x
x = tf.Variable(-1.0)
```

```python
with tf.GradientTape() as tape:
    tape.watch(x)
    y = tf.multiply(x, x)

# Evaluate the gradient of y at x = -1
g = tape.gradient(y, x)
print(g.numpy())
```

#### How to reshape a grayscale image
```python
# reshape the image of 4 square into 4 by 1 vector
import tensorflow as tf

# Generate grayscale image
gray = tf.random.uniform([2, 2], maxval=255, dtype='int32')

# Reshape grayscale image
gray = tf.reshape(gray, [2*2, 1])
```

```python
# generate 3 such matrices to form a 2 by 2 by 3 tensor
import tensorflow as tf

# Generate color image
color = tf.random.uniform([2, 3, 3], maxval=255, dtype='int32')

# Reshape color image
color = tf.reshape(color, [2*2, 3])
```

#### Reshaping tensors
In some cases, the network will take 1-dimensional tensors as inputs, but your data will come in the form of images, which will either be either 2- or 3-dimensional tensors, depending on whether they are grayscale or color images.

The figure below shows grayscale and color images of the sign language letter A. The two images have been imported for you and converted to the numpy arrays gray_tensor and color_tensor. Reshape these arrays into 1-dimensional vectors using the reshape operation, which has been imported for you from tensorflow. Note that the shape of gray_tensor is 28x28 and the shape of color_tensor is 28x28x3.

* Reshape gray_tensor from a 28x28 matrix into a 784x1 vector named gray_vector.
* Reshape color_tensor from a 28x28x3 tensor into a 2352x1 vector named color_vector.

```python
# Reshape the grayscale image tensor into a vector
gray_vector = reshape(gray_tensor, (28*28, 1))

# Reshape the color image tensor into a vector
color_vector = reshape(color_tensor, (28*28*3, 1))
```

#### Optimizing with gradients
You are given a loss function, , which you want to minimize. You can do this by computing the slope using the GradientTape() operation at different values of x. If the slope is positive, you can decrease the loss by lowering x. If it is negative, you can decrease it by increasing x. This is how gradient descent works.

In practice, you will use a high level tensorflow operation to perform gradient descent automatically. In this exercise, however, you will compute the slope at x values of -1, 1, and 0. The following operations are available: GradientTape(), multiply(), and Variable().

* Define x as a variable with the initial value x0.
* Set the loss function, y, equal to x multiplied by x. Do not make use of operator overloading.
* Set the function to return the gradient of y with respect to x
```python
def compute_gradient(x0):
  	# Define x as a variable with an initial value of x0
	x = Variable(x0)
	with GradientTape() as tape:
		tape.watch(x)
        # Define y using the multiply operation
		y = multiply(x, x)
    # Return the gradient of y with respect to x
	return tape.gradient(y, x).numpy()

# Compute and print gradients at x = -1, 1, and 0
print(compute_gradient(-1.0))
print(compute_gradient(1.0))
print(compute_gradient(0.0))
```
*Output*:

Notice that the slope is positive at x = 1, which means that we can lower the loss by reducing x. The slope is negative at x = -1, which means that we can lower the loss by increasing x. The slope at x = 0 is 0, which means that we cannot lower the loss by either increasing or decreasing x. This is because the loss is minimized at x = 0.


#### Working with image data
You are given a black-and-white image of a letter, which has been encoded as a tensor, letter. You want to determine whether the letter is an X or a K. You don't have a trained neural network, but you do have a simple model, model, which can be used to classify letter.

The 3x3 tensor, letter, and the 1x3 tensor, model, are available in the Python shell. You can determine whether letter is a K by multiplying letter by model, summing over the result, and then checking if it is equal to 1. As with more complicated models, such as neural networks, model is a collection of weights, arranged in a tensor.

Note that the functions reshape(), matmul(), and reduce_sum() have been imported from tensorflow and are available for use.
* The model, model, is 1x3 tensor, but should be a 3x1. Reshape model.
* Perform a matrix multiplication of the 3x3 tensor, letter, by the 3x1 tensor, model.
* Sum over the resulting tensor, output, and assign this value to prediction.
* Print prediction using the .numpy() method to determine whether letter is K.

```python
# Reshape model from a 1x3 to a 3x1 tensor
model = reshape(model, (1*3, 1))

# Multiply letter by model
output = matmul(letter, model)

# Sum over output and print prediction using the numpy method
prediction = reduce_sum(output)
print(prediction.numpy())
```

*Output*:

Your model found that prediction=1.0 and correctly classified the letter as a K. In the coming chapters, you will use data to train a model, model, and then combine this with matrix multiplication, matmul(letter, model), as we have done here, to make predictions about the classes of objects.

