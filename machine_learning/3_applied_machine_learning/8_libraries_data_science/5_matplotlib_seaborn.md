## Data Visualisation: Matplotlib and Seaborn

#### Matplotlib
* Making plots and static or interactive visualizations is one of the most important task in data analysis. It may be part of the exploratory process; for example, helping identify outliers, needed data transformations, or coming up with ideas for models.
* Matplotlib is the most extensively used library of python for data visualization due to it's high flexibility and extensive functionality that it provides.

```python
import matplotlib

matplotlib.__version__

# import matplotlib for plotting
import matplotlib.pyplot as plt
%matplotlib inline          # help visualization in jupyter
import numpy as np
import pandas as pd
```

#### Line Plot
```python
# random data
x = np.linspace(0, 10, 1000)

# plot
plt.plot(x, np.cos(x), label='Cosine');
```

#### Stacked bar plot
```python
# sample dataframe
data = pd.Dataframe([[1, 2],
                    [3,4],
                    [8,7],
                    [6,5],
                    [4,3],
                    [2,1]])

data.plot(kind='bar', stacked=True);
```

## Seaborn
* Seaborn is a Python data visualization library based on matplotlib.
* It provides a high-level interface for drawing attractive and informative statistical graphics. It provide choices for plot style and color defaults, define simple high level functions for commmon statistical plot types, and integrates with the functionality provides by Pandas dataframes.
* The main idea of Seaborn is that it provides high level commands to create a variety of plot types useful for statistical data exploration, and even more statistical model fitting.

```python
import seaborn as sns
sns.set()

# create random data
data = np.random.multivariate_normal([0,0], [[5,2],[2,2]], size=2000)
data = pd.DataFrame(data, columns=['x','y'])
```

#### Density Plots
```python
for col in 'xy':
    sns.kdeplot(data[col], shade=True)

for col in 'xy':
    sns.distplot(data[col], kde=False)

for col in 'xy':
    sns.distplot(data[col])
```


#### Pair Plot
```python
iris = sns.load_dataset("iris")
iris.head()

# visualizing the multidimensional relationships among the samples is as easy as calling sns.pairplot
sns.pairplot(iris, hue='species', height=2.5);
```

