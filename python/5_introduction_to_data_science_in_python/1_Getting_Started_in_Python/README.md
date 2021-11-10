#### What is a module?
* Groups related tools together
* akes it easy to know where to look for a particular tool
* Common examples:
  * matplotlib - create charts
  * pandas - loads tabular data
  * scikit-learn - perform machine learning
  * scipy - contains statistics functions
  * nltk - works with text data
  
#### Importing modules 
```python
# import pandas and matplotlib
import pandas as pd
from matplotlib import pyplot as plt

# pandas loads our data
df = pd.read_csv('ransom.csv')

# Matplotlib plots and displays
plt.plot(df.letters, df.frequency)
plt.show()
```

#### Exercise: Importing Python modules
Modules (sometimes called packages or libraries) help group together related sets of tools in Python. In this exercise, we'll examine two modules that are frequently used by Data Scientists:

statsmodels: used in machine learning; usually aliased as sm
seaborn: a visualization library; usually aliased as sns
Note that each module has a standard alias, which allows you to access the tools inside of the module without typing as many characters. For example, aliasing lets us shorten seaborn.scatterplot() to sns.scatterplot().
```python
# Use an import statement to import seaborn with alias sns
import statsmodels as sm
import seaborn as sns

# module for performing mathematical operations on lists of data
import numpy as np
```

#### Exercise: Load a DataFrame
A ransom note was left at the scene of Bayes' kidnapping. Eventually, we'll want to analyze the frequency with which each letter occurs in the note, to help us identify the kidnapper. For now, we just need to load the data from ransom.csv into Python.

We'll load the data into a DataFrame, a special data type from the pandas module. It represents spreadsheet-like data (something with rows and columns).

We can create a DataFrame from a CSV (comma-separated value) file by using the function pd.read_csv.
```python
# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv('random.csv')

# Display DataFrame
print(r)

cat > ransom.csv << EOF
letter_index,letter,frequency
1,A,7.38
2,B,1.09
3,C,2.46
4,D,4.1
5,E,12.84
6,F,1.37
7,G,1.09
8,H,3.55
9,I,7.65
10,J,0.0
11,K,3.01
12,L,3.28
13,M,2.46
14,N,7.38
EOF

# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv('ransom.csv')

# Display DataFrame
print(r)
```

#### What can pandas do for you?
* Loading tabular data from different success
* Search for particular rows or columns
* Calculate aggregate statistics
* Combining data from multiple sources
```python
import pandas as pd
df = pd.read_csv('ransom.csv')
print(df)
```
#### Inspecting a DataFrame
```python
# print only 5 lines
df.head()
print(df.head())
```

* Info about dataframe
  * Column names
  * Number of rows
  * Data types
```python
df.info()
print(df.info())
```
