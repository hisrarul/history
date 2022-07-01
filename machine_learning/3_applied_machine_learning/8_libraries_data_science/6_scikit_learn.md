## Basics of Scikit Learn
* It provides simple and efficient tools for pre-processing and predictive modeling.

* Pre-processing
    * Impute Missing Values
    * Encode Categorical variables
    * Scaling / Normalizing of Data

* Model Building
    * Identifying category to which an object belongs
    * Predicting a continuous valued attribute associated with an object.

* Automating the process
    * After the model building create pipelines to automate the pre-processing part and predict the target using the final model.


#### Steps to build a model in scikit-learn
1. Import the model
2. Prepare the data set
3. Separate the independent and target variables
4. Create an object of the model.
5. Fit the model with the data.
6. Use the model to predict target.

```python
# import the scikit-learn library
import sklearn

# check the version, we need 0.22.1
sklearn.__version__

# read the data set and check for the null values
import pandas as pd
data = pd.read_csv('big_mart_sales.csv')
data.isnull.sum()

# import the SimpleImputer
from sklearn.impute import SimpleImputer
```

* For imputing the missing values, we will use SimpleImputer.
* First we will create an object of the Imputer and define the strategy.
* We will impute the `Item_Weight` by mean value and Outlet_Size by most_fequent value.
* Fit the objects with the data.
* Transform the data.

```python
# create the object of the imputer for Item_Weight and Outlet_Size
impute_weight = SimpleImputer(Strategy = 'mean')    # if it is numerical column then you may want to replace the missing values by mean of the column
impute_size = SimpleImputer(Strategy = 'most_fequent')  # if it's categorical column then you want to replace by the most frequent category in the column.

# fit the Item_Weight imputer with the data and tranform
impute_weight.fit(data[['Item_Weight']])
data.Item_Weight = impute_weight.tranform(data[['Item_Weight']])

# fit the Outlet_Size imputer with the data and transform
impute_size.git(data[['Outlet_Size']])
data.Outlet_Size = impute_size.transform(data[['Outlet_Size']])

# check the null values
data.isna().sum()
```

* Now, after the preprocessing step, we separate the inpependent and target variable and pass the data to the model object to train the model.

* *If we have a problem in which we have to identify the category of an object based on some features. For example whether the given picture is of a cat or a dog. These are classification problems.*
* Or if we have to identify a continuous attribute like predicting sales based on some features. These are *Regression Problems*.

* SCIKIT-LEARN has tools which will help you build Regression, Classification models and many others.

```python
some of the very basic models scikit learn has
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
```

After we have buid the model now whenever new data points are added to the existing data, we need to perform the same preprocessing steps again before we can use the model to make predictions. This becomes a tedious and time consuming process.

So, scikit-learn provides tools to create a pipeline of all those steps that will your work a lot more easier.

```python
from sklearn.pipeline import Pipeline
```