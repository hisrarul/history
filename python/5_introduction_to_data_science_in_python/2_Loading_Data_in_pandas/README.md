#### Exercise: Loading a DataFrame
We're still working hard to solve the kidnapping of Bayes, the Golden Retriever. Previously, we used a license plate spotted at the crime scene to narrow the list of suspects to:

Fred Frequentist
Ronald Aylmer Fisher
Gertrude Cox
Kirstine Smith
We've obtained credit card records for all four suspects. Perhaps some of them made suspicious purchases before the kidnapping?

```python
cat > credit_records.csv << EOF
suspect,location,date,item,price
Kirstine Smith,Groceries R Us,"January 6, 2018",broccoli,1.25
Gertrude Cox,Petroleum Plaza,"January 6, 2018",fizzy drink,1.9
Fred Frequentist,Groceries R Us,"January 6, 2018",broccoli,1.25
Gertrude Cox,Groceries R Us,"January 12, 2018",broccoli,1.25
Kirstine Smith,Clothing Club,"January 9, 2018",shirt,14.25
Gertrude Cox,Burger Mart,"January 10, 2018",burger,3.95
Fred Frequentist,Burger Mart,"January 6, 2018",fries,1.95
Ronald Aylmer Fisher,Clothing Club,"January 8, 2018",pants,12.05
Ronald Aylmer Fisher,Clothing Club,"January 13, 2018",shirt,14.25
Kirstine Smith,Clothing Club,"January 1, 2018",shirt,14.25
Kirstine Smith,Clothing Club,"January 7, 2018",pants,12.05
Gertrude Cox,Petroleum Plaza,"January 14, 2018",fizzy drink,1.9
Ronald Aylmer Fisher,Petroleum Plaza,"January 10, 2018",carwash,13.25
Fred Frequentist,Burger Mart,"January 7, 2018",cheeseburger,4.95
Gertrude Cox,Clothing Club,"January 5, 2018",pants,12.05
Gertrude Cox,Burger Mart,"January 2, 2018",cheeseburger,4.95
Gertrude Cox,Groceries R Us,"January 11, 2018",broccoli,1.25
Kirstine Smith,Petroleum Plaza,"January 12, 2018",carwash,13.25
Gertrude Cox,Petroleum Plaza,"January 13, 2018",fizzy drink,1.9
Fred Frequentist,Clothing Club,"January 8, 2018",shirt,14.25
Kirstine Smith,Petroleum Plaza,"January 12, 2018",fizzy drink,1.9
Fred Frequentist,Petroleum Plaza,"January 8, 2018",carwash,13.25
Ronald Aylmer Fisher,Groceries R Us,"January 13, 2018",eggs,6.5
Gertrude Cox,Burger Mart,"January 9, 2018",burger,3.95
Gertrude Cox,Burger Mart,"January 14, 2018",cheeseburger,4.95
Kirstine Smith,Groceries R Us,"January 2, 2018",cheese,5.0
Ronald Aylmer Fisher,Burger Mart,"January 8, 2018",fries,1.95
Gertrude Cox,Groceries R Us,"January 8, 2018",cheese,5.0
Fred Frequentist,Clothing Club,"January 3, 2018",dress,20.15
Kirstine Smith,Clothing Club,"January 5, 2018",dress,20.15
Kirstine Smith,Burger Mart,"January 9, 2018",burger,3.95
Gertrude Cox,Clothing Club,"January 7, 2018",pants,12.05
Kirstine Smith,Groceries R Us,"January 5, 2018",cheese,5.0
Ronald Aylmer Fisher,Petroleum Plaza,"January 7, 2018",gas,24.95
Ronald Aylmer Fisher,Groceries R Us,"January 6, 2018",cucumbers,2.05
Gertrude Cox,Clothing Club,"January 12, 2018",shirt,14.25
Gertrude Cox,Burger Mart,"January 2, 2018",cheeseburger,4.95
Fred Frequentist,Clothing Club,"January 8, 2018",dress,20.15
Kirstine Smith,Petroleum Plaza,"January 12, 2018",fizzy drink,1.9
Ronald Aylmer Fisher,Groceries R Us,"January 2, 2018",eggs,6.5
Gertrude Cox,Clothing Club,"January 1, 2018",dress,20.15
Kirstine Smith,Petroleum Plaza,"January 5, 2018",gas,24.95
Gertrude Cox,Petroleum Plaza,"January 13, 2018",fizzy drink,1.9
Ronald Aylmer Fisher,Petroleum Plaza,"January 14, 2018",fizzy drink,1.9
Ronald Aylmer Fisher,Petroleum Plaza,"January 5, 2018",fizzy drink,1.9
Fred Frequentist,Groceries R Us,"January 6, 2018",cheese,5.0
Ronald Aylmer Fisher,Groceries R Us,"January 9, 2018",cucumbers,2.05
Ronald Aylmer Fisher,Petroleum Plaza,"January 2, 2018",gas,24.95
Kirstine Smith,Clothing Club,"January 8, 2018",dress,20.15
Gertrude Cox,Groceries R Us,"January 2, 2018",broccoli,1.25
Fred Frequentist,Petroleum Plaza,"January 3, 2018",fizzy drink,1.9
Gertrude Cox,Groceries R Us,"January 14, 2018",eggs,6.5
Gertrude Cox,Burger Mart,"January 6, 2018",cheeseburger,4.95
Kirstine Smith,Petroleum Plaza,"January 10, 2018",carwash,13.25
Gertrude Cox,Burger Mart,"January 12, 2018",fries,1.95
Fred Frequentist,Clothing Club,"January 12, 2018",shirt,14.25
Kirstine Smith,Groceries R Us,"January 12, 2018",milk,4.25
Gertrude Cox,Clothing Club,"January 3, 2018",pants,12.05
Fred Frequentist,Groceries R Us,"January 9, 2018",cheese,5.0
Kirstine Smith,Burger Mart,"January 13, 2018",fries,1.95
Kirstine Smith,Petroleum Plaza,"January 2, 2018",carwash,13.25
Gertrude Cox,Petroleum Plaza,"January 5, 2018",carwash,13.25
Ronald Aylmer Fisher,Petroleum Plaza,"January 6, 2018",fizzy drink,1.9
Gertrude Cox,Clothing Club,"January 4, 2018",dress,20.15
Ronald Aylmer Fisher,Groceries R Us,"January 8, 2018",milk,4.25
Ronald Aylmer Fisher,Petroleum Plaza,"January 13, 2018",fizzy drink,1.9
Gertrude Cox,Burger Mart,"January 1, 2018",burger,3.95
Gertrude Cox,Clothing Club,"January 7, 2018",pants,12.05
Ronald Aylmer Fisher,Burger Mart,"January 14, 2018",fries,1.95
Gertrude Cox,Clothing Club,"January 6, 2018",dress,20.15
Fred Frequentist,Clothing Club,"January 13, 2018",shirt,14.25
Gertrude Cox,Burger Mart,"January 1, 2018",burger,3.95
Ronald Aylmer Fisher,Groceries R Us,"January 7, 2018",cucumbers,2.05
Ronald Aylmer Fisher,Petroleum Plaza,"January 1, 2018",gas,24.95
Fred Frequentist,Groceries R Us,"January 11, 2018",cheese,5.0
Gertrude Cox,Groceries R Us,"January 14, 2018",milk,4.25
Gertrude Cox,Clothing Club,"January 10, 2018",dress,20.15
Fred Frequentist,Burger Mart,"January 8, 2018",cheeseburger,4.95
Kirstine Smith,Clothing Club,"January 7, 2018",shirt,14.25
Kirstine Smith,Clothing Club,"January 13, 2018",pants,12.05
Ronald Aylmer Fisher,Clothing Club,"January 13, 2018",pants,12.05
Gertrude Cox,Groceries R Us,"January 13, 2018",broccoli,1.25
Ronald Aylmer Fisher,Clothing Club,"January 6, 2018",shirt,14.25
Ronald Aylmer Fisher,Burger Mart,"January 2, 2018",fries,1.95
Gertrude Cox,Clothing Club,"January 5, 2018",dress,20.15
Ronald Aylmer Fisher,Clothing Club,"January 3, 2018",pants,12.05
Fred Frequentist,Groceries R Us,"January 3, 2018",milk,4.25
Gertrude Cox,Petroleum Plaza,"January 8, 2018",gas,24.95
Ronald Aylmer Fisher,Burger Mart,"January 8, 2018",fries,1.95
Gertrude Cox,Petroleum Plaza,"January 8, 2018",gas,24.95
Fred Frequentist,Burger Mart,"January 1, 2018",fries,1.95
Gertrude Cox,Burger Mart,"January 7, 2018",burger,3.95
Fred Frequentist,Clothing Club,"January 2, 2018",pants,12.05
Ronald Aylmer Fisher,Groceries R Us,"January 10, 2018",milk,4.25
Ronald Aylmer Fisher,Petroleum Plaza,"January 9, 2018",fizzy drink,1.9
Kirstine Smith,Burger Mart,"January 5, 2018",cheeseburger,4.95
Gertrude Cox,Groceries R Us,"January 8, 2018",cucumbers,2.05
Gertrude Cox,Petroleum Plaza,"January 8, 2018",fizzy drink,1.9
Ronald Aylmer Fisher,Clothing Club,"January 12, 2018",pants,12.05
Gertrude Cox,Clothing Club,"January 7, 2018",shirt,14.25
Fred Frequentist,Clothing Club,"January 4, 2018",pants,12.05
Gertrude Cox,Clothing Club,"January 9, 2018",dress,20.15
Kirstine Smith,Burger Mart,"January 14, 2018",burger,3.95
Ronald Aylmer Fisher,Groceries R Us,"January 11, 2018",cucumbers,2.05
EOF

# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records = pd.read_csv('credit_records.csv')

# Display the first five rows of credit_records using the .head() method
print(credit_records.head())

# Use .info() to inspect the DataFrame credit_records
print(credit_records.info())
```

#### Selecting columns
* Why select columns?
	* Use in a calculation
  * Plot data
```python
# selecting with brackets and string
suspect = name_of_the_dataframe['column_name']
print(suspect)

# selecting with a dot, if columns contains letters, numbers and underscores
price = name_of_dataframe.column_name
print(price)
```

#### Exercise: More column selection mistakes
Another junior detective is examining a DataFrame of Missing Puppy Reports. He's made some mistakes that cause the code to fail.

The pandas module has been loaded under the alias pd, and the DataFrame is called mpr.
```python
######## Dataframe
  Dog Name             Owner Name         Dog Breed       Missing?
0    Bayes               DataCamp  Golden Retriever  Still Missing
1  Sigmoid                                Dachshund  Still Missing
2   Sparky             Dr. Apache     Border Collie          Found
3  Theorem  Joseph-Louis Lagrange    French Bulldog          Found
########
Sol:

# Use info() to inspect mpr
print(mpr.info())

# The following code contains one or more errors
# Correct the mistakes in the code so that it runs without errors

# Select column "Dog Name" from mpr
name = mpr['Dog Name']

# Select column "Missing?" from mpr
is_missing = mpr['Missing?']

# Display the columns
print(name)
print(is_missing)
```

#### Selecting rows with logic
* Using logic with Dataframes
```python
# This will return only columns which are greater than value
dataframe_name[dataframe_name.column_name > value]
e.g. credit_records[credit_record.price > 20.00]
     credit_records[credit_record.suspect == 'Ronald Aylmer Fisher']
```

#### Exercise: Logical testing
Let's practice writing logical statements and displaying the output.

Recall that we use the following operators:

	* == tests that two values are equal.
	* != tests that two values are not equal.
	* > and < test that greater than or less than, respectively.
	* >= and <= test greater than or equal to or less than or equal to, respectively.
```python
height_inches = 65
plate1 = "FRQ123"
fur_color = "blonde"

# Is height_inches greater than 70 inches?
print(height_inches > 70)

# Is plate1 equal to "FRQ123"?
print(plate1 == "FRQ123")

# Is fur_color not equal to "brown"?
print(fur_color != "brown")
```

#### Exercise: Selecting missing puppies
Let's return to our DataFrame of missing puppies, which is loaded as mpr. Let's select a few different rows to learn more about the other missing dogs.

* Select the dogs where Age is greater than 2.
* Select the dogs whose Status is equal to Still Missing.
* Select all dogs whose Dog Breed is not equal to Poodle.
```python
# Dataframe: mpr
  Dog Name             Owner Name         Dog Breed         Status  Age
0    Bayes               DataCamp  Golden Retriever  Still Missing    1
1  Sigmoid                                Dachshund  Still Missing    2
2   Sparky             Dr. Apache     Border Collie          Found    3
3  Theorem  Joseph-Louis Lagrange    French Bulldog          Found    4
4      Ned           Tim Oliphant          Shih Tzu  Still Missing    2
5    Benny   Hillary Green-Lerman            Poodle          Found    3

##
# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr.Status == 'Still Missing']
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr['Dog Breed'] != 'Poodle']
print(not_poodle)
```
