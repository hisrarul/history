## Statsmodel
Statsmodels is a Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration.

```python
# import the statsmodels library
import statsmodels

# check the version
statsmodels.__version__

# importing thre required libraries
import statsmodels.api as sm
from sklearn import datasets
import numpy as np
import pandas as pd

# loading the dataset from datasets library
data = datasets.load_boston()

# create the dataframe
features = pd.DataFrame(data.data, columns=data.feature_names)

features.head()
```

#### Separate the target variable
```python
# target in another DataFrame
target = pd.DataFrame(data.target, columns=["MEDV"])
```

#### Create a Linear Regression Model
```python
X = features
y = target["MEDV"]
```

#### Build a model
```python
# Note the difference in argument order
model = sm.OLS(y, X).fit()      # STATISTICAL LINEAR REGRESSION TECHNIQUE
```


#### Make Predictions
```python
predictions = model.predict(X)  # make the predictions by the model
```

#### Summary of the model
```python
# Print out the statistics
model.summary()     # performance, kind of data
```

#### Statsmodels tools
* Regression and linear models
* Time series analysis
* Statistics and tools


