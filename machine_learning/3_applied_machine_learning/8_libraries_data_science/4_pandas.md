## Introduction to Pandas
* Pandas: Open source library for data manipulation and analysis.
* We can read and write different format of file like CSV, JSON, EXCEL, HTML, etc.
* We can summarize the data.
* We can filter and modify the data based on multiple conditions.
* We can merge multiple files.

```python
# import the library
import pandas as pd

# check the version of the pandas library
pd.__version__

# read the file
data = pd.read_csv('big_mart_sales.csv')

# view the data
data.head(3)

# shape of the data, rows and columns
data.shape

# check the column names
data.columns        # o/p: no of rows and col

# check the data types in the columns
data.dtypes

# check the null values in the data
data.isna().sum()       # check the missing value
data.isnull.sum()

# summary of the data
data.describe()
```


