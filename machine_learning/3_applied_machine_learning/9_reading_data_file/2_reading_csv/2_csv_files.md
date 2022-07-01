## CSV Files

So far, we have seen the basic introduction of the python libraries that commonly used in data science tasks. Now, the first task is reading different type of files like JSON, TEXT, CSV, EXCEL, etc. In this notebook, we will see how to read `CSV` files and what are different challenges that we face while reading `CSV` files and how to tackle them.

* `Pandas` is one fo the most used library for reading data sets. 

#### Read the CSV file

*About the Data Set:* The data set that we are going to use is the Sales Data. It contains information like `Item Identifier`, `Outlet Size`, `Item MRP`, `Outlet Location Type`, `Item Outlet Sales`, etc.

```python
# read the dataset
data = pd.read_csv('datasets/big_mart_sales.csv')

type(data)
```

#### Dataframe
* Dataframe is a 2-dimensional data structure with columns that can contain different data type.
* Similar to a spreadsheet or SQL table.
* It is generally the most commonly used pandas object.

```python
# view the data from top with number of rows
data.head()     # o/p will be dataframe


# to check the dimension of the data set i.e. number of rows and column
data.shape
```

#### Read the data except first few rows in the file
Sometime, the data sets has comments at the begining of the file. While reading file, pass the parameter `skiprows = n (number of rows to skip)`

```python
# read the dataset
data_with_comments = pd.read_csv('datasets/big_mart_sales.csv', skiprows=5)

# view the data
data_with_comments.head()
```


#### Reading files from multiple directories
* When data is present in multiple directories, let's see how to read data
* Here, we have split the same dataset `year wise` into multiple files and stored them into multiple directories.
* Use the `glob` library to list the files in a directory

```python
# import the library
import glob

# list all the files in the folder
for directory in glob.glob('dataset/multiple-directory/*'):
    print(directory)
```

Each folders contains CSV. We will iterate through each of them and concatenate the files.
```python
# iterate through each of the files
for directory in glob.glob('datasets/multi-directory/*'):
    for files in glob.glob(directory + '/*'):
        print(files)
```

*Concatenate the files*
```python
# list to store data frames
data_frame_list = []

# iterate through each of the files
for directory in glob.glob('datasets/multi-directory/*'):
    for files in glob.glob(directory + '/*'):
        # read and append the data frame
        data_frame_list.append(pd.read_csv(files))
    
# concatenate the dataframes
final_data = pd.concat(data_frame_list)
final_data.head()
final_data.shape
```

#### Store the CSV
```python
final_data.to_csv('datasets/merged_big_mart_sales.csv', index=False)
```


#### Read a CSV of a specific Delimeter
* By default, while reading a CSV file pandas consider the seperate as `,`. But if the CSV file has some other seperator or delimeter like `[;, \t]` we need to specify that.
```python
# read the data
data_delimiter = pd.read_csv('datasets/big_mart_delimiter.csv')

# we can see that the seperator used in the csv is tab \t
data_delimiter

# read the file again with delimiter parameter
data_delimiterr = pd.read_csv('datasets/big_mart_delimiter.csv', delimiter='\t')

# view the data
data_delimiter.head()
```

#### Read first 'n' rows (when data is large)
```python
# specify the number of rows to read
read_sample_from_data =  pd.read_csv('dataset/big_mart.csv', nrows=100)

# shape of the data
read_sample_from_data.shape

# view the data
read_sample_from_data.head()
```

#### Read specific columns
* If the dataset has large number of columns, it is impossible to go through all of them in a single go so we can read only specific column at a time.

```python
# read specific columns
read_specific_columns = pd.read_csv('datasets/big_mart.csv', usecols=['Item_Identifier', 'Item_Type', 'Item_MRP', 'Item_Outlet_Sales'])

read_specific_columns
```


