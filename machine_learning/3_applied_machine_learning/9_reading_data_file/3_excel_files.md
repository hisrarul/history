## Excel

```python
# import the pandas library
import pandas as pd

# read the dataset
data = pd.read_excel('datasets/big_mart_sales.xlsx')

# view the head
data.head()
```

#### Excel files with multiple sheets: Specify the sheet name
```python
# read the data with multiple sheets
data_with_multiple_sheets = pd.read_excel('datasets/big_mart_with_multiple_sheets.xlsx')

# unique year present in the data
data_with_muultiple_sheets.Outlet_establishment_Year.unique()

# to read the data from specific sheet
sheet_1985 = pd.read_excel('datasets/big_mart_multiple_sheets.xlsx', sheet_name='1985')

sheet_1985.head()

sheet_1987 = pd.read_excel('datasets/big_mart_multiple_sheets.xlsx', sheet_name='1987')

sheet_1985.head()
```


#### Cancatenate all sheets
```python
# create an array of dataframes
sheets = [sheet_1985, sheet_1987, sheet_1997]

# concatenate the array
final_data = pd.concat(sheets)

# unique years in final data
final_data.Outlet_Establishment_Year.unique()
```

*If comments are there on the top of a file*
```python
# read the data without skiprows
sheet_with_comments = pd.read_excel('datasheets/big_mart_comments.xlsx')

# top rows of the data
sheet_with_comments.head()

# read the data with skiprows
sheet_with_comments = pd.read_excel('datasets/big_mart.xlsx', skiprows=3)

# view the top rows of the data
sheet_with_comments.head()
```

