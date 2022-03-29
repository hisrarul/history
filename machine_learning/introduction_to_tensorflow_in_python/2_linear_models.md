## Linear models

#### Input data
Data can be imported from external sources and it may include numeric, image, or text data. This need to be convertible in to usable format. External data can be imported using TensorFlow.

#### Importing data for use in TensorFlow
* Data can be imported using `tensorflow`
    * Useful for managing complex pipelines
* Simpler option can be used
    * Import data using `pandas`
    * Convert data to `numpy` array
    * Use in `tensorflow` with modification

```python
# Import numpy and pandas
import numpy as np
import pandas as pd

# Load data from csv
housing = pd.read_csv('kc_housing.csv')

# Convert to numpy array
housing = np.array(housing)
```

* We will focus on data stored in csv format
* Pandas also has methods for handling data in other formats
    * e.g. `read_json()`, `read_html()`, `read_excel()`


#### Parameters of read_csv()
| Parameter | Description |
|-----------|-------------|
| filepath_or_buffer | Accepts a file path or a URL | None |
| sep | Delimiter betweeen columns | , |
| delim_whitespace | Boolean for whether to delimit whitespace | False |
| encoding | Specifies encoding to be used if any | None |


#### Using mixed type datasets
| date | price | bedrooms |
|------|-------|----------|
| 20141013T000000 | 221900 | 3 |
| 20141209T000000 | 538000 | 3 |

| floors | waterfront | view |
|--------|------------|------|
| 1 | 0 | 0 |
| 2 | 1 | 0 |
| 1 | 0 | 2 |
| 1 | 0 | 0 |

#### Setting the data type
```python
# Load KC dataset
housing = pd.read_csv('kc_housing.csv')

# Convert price column to float32
price = np.array(housing['price'], np.float32)

# Convert waterfront column to Boolean
waterfront = np.array(housing['waterfront'], np.bool)
```

```python
# Using tensorflow cast
housing = pd.read_csv('kc_housing.csv')

#  Convert price column to float32
price = tf.cast(housing['price'], tf.float32)

# Convert waterfront column to Boolean
waterfront = tf.cast(housing['waterfront'], tf.bool)
```

#### Load data using pandas
Before you can train a machine learning model, you must first import data. There are several valid ways to do this, but for now, we will use a simple one-liner from pandas: pd.read_csv().

* Import pandas under the alias pd.
* Assign the path to a string variable with the name data_path.
* Load the dataset as a pandas dataframe named housing.
* Print the price column of housing.

```python
# Import pandas under the alias pd
import pandas as pd

# Assign the path to a string variable named data_path
data_path = 'kc_house_data.csv'

# Load the dataset as a dataframe named housing
housing = pd.read_csv(data_path)

# Print the price column of housing
print(housing['price'])
```

#### Setting the data type
You will import numpy and tensorflow, and define tensors that are usable in tensorflow using columns in housing with a given data type. Recall that you can select the price column, for instance, from housing using housing['price'].

* Import numpy and tensorflow under their standard aliases.
* Use a numpy array to set the tensor price to have a data type of 32-bit floating point number
* Use the tensorflow function cast() to set the tensor waterfront to have a Boolean data type.
* Print price and then waterfront. Did you notice any important differences?
```python
# Import numpy and tensorflow with their standard aliases
import tensorflow as tf
import numpy as np

# Use a numpy array to define price as a 32-bit float
price = np.array(housing['price'], np.float32)

# Define waterfront as a Boolean using cast
waterfront = tf.cast(housing['waterfront'], tf.bool)

# Print price and waterfront
print(price)
print(waterfront)
```
Output:

Note that printing price yielded a numpy array; whereas printing waterfront yielded a tf.Tensor().

#### Loss function
We need loss functions to train models bcz they tell us how well our model explains the data. Without this feedback, it is unclear how to adjust model parameters during the training process.

* Fundamental `tensorflow` operation
    * Used to train a model
    * Measure of model fit
* Higher value -> worse model fit
    * train the model by selecting parameter values that minimize the loss function

#### Common loss functions in TensorFlow
* TensorFlow has operations for common loss functions
* Typical choices for training linear models includes
    * Mean squared error (MSE)
    * Mean absolute error (MAE)
    * Huber error

#### Why do we care about loss functions?
* MSE
    * Strongly penalizes outliers
    * High (gradient) sensitivity near minimum

* MAE
    * Scales linearly with size of error
    * Low sensitivity near minimum

* Huber
    * Similar to MSE near minimum
    * Similar to MAE away from minimum

#### Defining a loss function
```python
# Import TensorFlow under standard alias
import tensorflow as tf

# Compute the MSE loss
loss = tf.keras.losses.mse(targets, predictions)
```

```python
# Define a linear regression model
def linear_regression(intercept, slope = slope, features = features):
    return intercept + features*slope
```

```python
# Define a loss function to compute the MSE
def loss_function(intercept, slope, targets = targets, features = features):
    # Compute the predictions for a linear model
    predictions = linear_regression(intercept, slope)

    # return the loss
    return tf.keras.lossed.mse(targets, predictions)
```

```python
# Compute the loss for test data inputs
loss_function(intercept, slope, test_targets, test_features)

# Compute the loss for default data inputs
loss_function(intercept, slope)
```

#### Exercise: Loss functions in TensorFlow
In this exercise, you will compute the loss using data from the King County housing dataset. You are given a target, price, which is a tensor of house prices, and predictions, which is a tensor of predicted house prices. You will evaluate the loss function and print out the value of the loss.
```python
# Import the keras module from tensorflow
from tensorflow import keras 

# Compute the mean squared error (mse)
loss = keras.losses.mse(price, predictions)

# Print the mean squared error (mse)
print(loss.numpy())
```

* Modify your code to compute the mean absolute error (mae), rather than the mean squared error (mse).
```python
# Import the keras module from tensorflow
from tensorflow import keras

# Compute the mean absolute error (mae)
loss = keras.losses.mae(price, predictions)

# Print the mean absolute error (mae)
print(loss.numpy())
```

Output:

You may have noticed that the MAE was much smaller than the MSE, even though price and predictions were the same. This is because the different loss functions penalize deviations of predictions from price differently. MSE does not like large deviations and punishes them harshly.


#### Exercise: Modifying the loss function
In the previous exercise, you defined a tensorflow loss function and then evaluated it once for a set of actual and predicted values. In this exercise, you will compute the loss within another function called loss_function(), which first generates predicted values from the data and variables. The purpose of this is to construct a function of the trainable model variables that returns the loss. You can then repeatedly evaluate this function for different variable values until you find the minimum. In practice, you will pass this function to an optimizer in tensorflow. Note that features and targets have been defined and are available. Additionally, Variable, float32, and keras are available.
* Define a variable, scalar, with an initial value of 1.0 and a type of float32.
* Define a function called loss_function(), which takes scalar, features, and targets as arguments in that order.
* Use a mean absolute error loss function.
```python
# Initialize a variable named scalar
scalar = Variable(1.0, float32)

# Define the model
def model(scalar, features = features):
  	return scalar * features

# Define a loss function
def loss_function(scalar, features = features, targets = targets):
	# Compute the predicted values
	predictions = model(scalar, features)
    
	# Return the mean absolute error loss
	return keras.losses.mae(targets, predictions)

# Evaluate the loss function and print the loss
print(loss_function(scalar).numpy())
```

#### What is a linear regression?
To better understand it, let's say we want to examine the relationship between house size and price. We might start by plotting the size in square feet against the price in dollars.
We might expect an x% increase in size to be associated with y% increase in price. A linear regression model assumes that the relationship between these variable can be captured by a line. 

That is, two parameters -- the line's slope and intercept -- fully characterize the relationship between size and price.

#### The linear regression model
* A linear regression model assumes a linear relationship:
    * price = intercept + size * slope + error

* This is an example of a univariate regression.
    * There is only one feature, `size`.

* Multiple regression models have more than one feature.
    * E.g. `size` and `location`

#### Linear regression in TensorFlow
```python
# Define the targets and features
price = np.array(housing['price'], np.float32)
size = np.array(housing['sqft_living'], np.float32)

# Define the intercept and slope
intercept = tf.Variable(0.1, np.float32)
slope = tf.Variable(0.1, np.float32)

# Define a linear regression model
def linear_regression(intercept, slope, features = size):
    return intercept + features*slope

# Compute the predicted values and loss
def loss_function(intercept, slope, targets = price, features = size):
    predictions = linear_regression(intercept, slope)
    return tf.keras.losses.mse(targets, predictions)
```

```python
# Define an optimization operation
opt = tf.keras.optimizers.Adam()

# Minimize the loss function and print the loss
for j in range(1000):
    opt.minimize(lambda: loss_function(intercept, slope), var_list=[intercept, slope])
    print(loss_function(intercept, slope))
```

```python
# print the trained parameters
print(intercept.numpy(), slope.numpy())
```

#### Set up a linear regression
A univariate linear regression identifies the relationship between a single feature and the target tensor. In this exercise, we will use a property's lot size and price. Just as we discussed in the video, we will take the natural logarithms of both tensors, which are available as price_log and size_log.

In this exercise, you will define the model and the loss function. You will then evaluate the loss function for two different values of intercept and slope. Remember that the predicted values are given by intercept + features*slope. Additionally, note that keras.losses.mse() is available for you. Furthermore, slope and intercept have been defined as variables.

* Define a function that returns the predicted values for a linear regression using intercept, features, and slope, and without using add() or multiply().
* Complete the loss_function() by adding the model's variables, intercept and slope, as arguments.
* Compute the mean squared error using targets and predictions.

```python
# Define a linear regression model
def linear_regression(intercept, slope, features = size_log):
	return intercept + slope*features

# Set loss_function() to take the variables as arguments
def loss_function(intercept, slope, features = size_log, targets = price_log):
	# Set the predicted values
	predictions = linear_regression(intercept, slope, features)
    
    # Return the mean squared error loss
	return keras.losses.mse(targets, predictions)

# Compute the loss for different slope and intercept values
print(loss_function(0.1, 0.1).numpy())
print(loss_function(0.1, 0.5).numpy())
```

#### Exercise: Train a linear model
In this exercise, we will pick up where the previous exercise ended. The intercept and slope, intercept and slope, have been defined and initialized. Additionally, a function has been defined, loss_function(intercept, slope), which computes the loss using the data and model variables.

You will now define an optimization operation as opt. You will then train a univariate linear model by minimizing the loss to find the optimal values of intercept and slope. Note that the opt operation will try to move closer to the optimum with each step, but will require many steps to find it. Thus, you must repeatedly execute the operation.
* Initialize an Adam optimizer as opt with a learning rate of 0.5.
* Apply the .minimize() method to the optimizer.
* Pass loss_function() with the appropriate arguments as a lambda function to .minimize().
* Supply the list of variables that need to be updated to var_list.

```python
# Initialize an Adam optimizer
opt = keras.optimizers.Adam(0.5)

for j in range(100):
	# Apply minimize, pass the loss function, and supply the variables
	opt.minimize(lambda: loss_function(intercept, slope), var_list=[intercept, slope])

	# Print every 10th value of the loss
	if j % 10 == 0:
		print(loss_function(intercept, slope).numpy())

# Plot data and regression line
plot_results(intercept, slope)
```

*Output:*

Notice that we printed loss_function(intercept, slope) every 10th execution for 100 executions. Each time, the loss got closer to the minimum as the optimizer moved the slope and intercept parameters closer to their optimal values.

#### Multiple linear regression
In most cases, performing a univariate linear regression will not yield a model that is useful for making accurate predictions. In this exercise, you will perform a multiple regression, which uses more than one feature.

You will use price_log as your target and size_log and bedrooms as your features. Each of these tensors has been defined and is available. You will also switch from using the the mean squared error loss to the mean absolute error loss: keras.losses.mae(). Finally, the predicted values are computed as follows: params[0] + feature1*params[1] + feature2*params[2]. Note that we've defined a vector of parameters, params, as a variable, rather than using three variables. Here, params[0] is the intercept and params[1] and params[2] are the slopes.

* Define a linear regression model that returns the predicted values.
* Set loss_function() to take the parameter vector as an input.
* Use the mean absolute error loss.
* Complete the minimization operation.

```python
# Define the linear regression model
def linear_regression(params, feature1 = size_log, feature2 = bedrooms):
	return params[0] + feature1*params[1] + feature2*params[2]

# Define the loss function
def loss_function(params, targets = price_log, feature1 = size_log, feature2 = bedrooms):
	# Set the predicted values
	predictions = linear_regression(params, feature1, feature2)
  
	# Use the mean absolute error loss
	return keras.losses.mae(targets, predictions)

# Define the optimize operation
opt = keras.optimizers.Adam()

# Perform minimization and print trainable variables
for j in range(10):
	opt.minimize(lambda: loss_function(params), var_list=[params])
	print_results(params)
```

*Output:*

Note that params[2] tells us how much the price will increase in percentage terms if we add one more bedroom. You could train params[2] and the other model parameters by increasing the number of times we iterate over opt.

#### What is batch training?
Let's say the dataset is much larger and you want to perform the training on a GPU, which has only small amount of memory. Since you can't fit the entire dataset in memory. You will instead divide it into batches and train on those batches sequentially. A single pass over all the batches is called an epoch and the process itself is called batch training.

Beyond alleviating memory constaints, batch training will also allow you to update model weights and optimizer parameters after each batch, rather than at the end of the epoch.

#### The chucksize parameter
* `pd.read_csv()` allows us to load data in batches
    * Avoid loading entire dataset e.g. 100 GB in size
    * `chunksize` parameter provides batch size
```python
# Import pandas and numpy
import pandas as pd
import numpy as np

# Load data in batches
for batch in pd.read_csv('kc_housing.csv', chunksize=100):
    # Extract price column
    price = np.array(batch['price'], np.float32)

    # Extract size column
    size = np.array(batch['size'], np.float32)
```

#### Training a linear model in batches
```python
# Import tensorflow, pandas, and numpy
import tensorflow as tf
import pandas as pd
import numpy as np

# Define trainable variables
intercept = tf.Variable(0.1, tf.float32)
slope = tf.Variable(0.1, tf.float32)

# Define the model
def linear_regression(intercept, slope, features):
    return intercept + features*slope

# Compute predicted values and return loss function
def loss_function(intercept, slope, targets, features):
    predictions = linear_regression(intercept, slope, features)
    return tf.keras.losses.mse(targets, predictions)

# Dine optimization operation, it is used to performm minimization
opt = tf.keras.optimizers.Adam()

# Load the data in batches from pandas
for batch in pd.read_csv('kc_housing.csv', chunksize=100):
    # Extract the target and feature columns
    price_batch = np.array(batch['price'], np.float32)
    size_batch = np.array(batch['lot_size'], np.float32)

    # Minimize the loss function
    opt.minimize(lambda: loss_function(intercept, slope, price_batch, size_batch), var_list=[intercept, slope])

# Print parameter values
print(intercept.numpy(), slope.numpy())
```

#### Full sample versus batch training
| Full Sample | Batch Training |
| One update per epoch | Multiple updates per epoch |
| Accepts dataset without modification | Requires division of dataset |
| Limited by memory | No limit on dataset size |


#### Preparing to batch train
Before we can train a linear model in batches, we must first define variables, a loss function, and an optimization operation. In this exercise, we will prepare to train a model that will predict price_batch, a batch of house prices, using size_batch, a batch of lot sizes in square feet. In contrast to the previous lesson, we will do this by loading batches of data using pandas, converting it to numpy arrays, and then using it to minimize the loss function in steps.

`Variable()`, `keras()`, and `float32` have been imported for you. Note that you should not set default argument values for either the model or loss function, since we will generate the data in batches during the training process.
* Define intercept as having an initial value of 10.0 and a data type of 32-bit float.
* Define the model to return the predicted values using intercept, slope, and features.
* Define a function called loss_function() that takes intercept, slope, targets, and features as arguments and in that order. Do not set default argument values.
* Define the mean squared error loss function using targets and predictions.

```python
# Define the intercept and slope
intercept = Variable(10.0, float32)
slope = Variable(0.5, float32)

# Define the model
def linear_regression(intercept, slope, features):
	# Define the predicted values
	return intercept + slope*features

# Define the loss function
def loss_function(intercept, slope, targets, features):
	# Define the predicted values
	predictions = linear_regression(intercept, slope, features)
    
 	# Define the MSE loss
	return keras.losses.mse(targets, predictions)
```

*Output:*

Notice that we did not use default argument values for the input data, features and targets. This is because the input data has not been defined in advance. Instead, with batch training, we will load it during the training process.


#### Training a linear model in batches
In this exercise, we will train a linear regression model in batches, starting where we left off in the previous exercise. We will do this by stepping through the dataset in batches and updating the model's variables, intercept and slope, after each step. This approach will allow us to train with datasets that are otherwise too large to hold in memory.

Note that the loss function,loss_function(intercept, slope, targets, features), has been defined for you. Additionally, keras has been imported for you and numpy is available as np. The trainable variables should be entered into var_list in the order in which they appear as loss function arguments.

* Use the .Adam() optimizer.
* Load in the data from 'kc_house_data.csv' in batches with a chunksize of 100.
* Extract the price column from batch, convert it to a numpy array of type 32-bit float, and assign it to price_batch.
* Complete the loss function, fill in the list of trainable variables, and perform minimization.

```python
# Initialize Adam optimizer
opt = keras.optimizers.Adam()

# Load data in batches
for batch in pd.read_csv('kc_house_data.csv', chunksize=100):
	size_batch = np.array(batch['sqft_lot'], np.float32)

	# Extract the price values for the current batch
	price_batch = np.array(batch['price'], np.float32)

	# Complete the loss, fill in the variable list, and minimize
	opt.minimize(lambda: loss_function(intercept, slope, price_batch, size_batch), var_list=[intercept, slope])

# Print trained parameters
print(intercept.numpy(), slope.numpy())
```

*Outputs:* 

Batch training will be very useful when you train neural networks
