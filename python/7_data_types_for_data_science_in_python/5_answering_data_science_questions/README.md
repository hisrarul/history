## Answering Data Science Questions

#### Counting with Data Ranges
* Data sets is in csv format, also available at https://data.cityofchicago.org/
* Import data from csv
```python
import csv

csvfile = open('ART_GALLERY.csv', 'r')
for row in csv.reader(csvfile):
	print(row)
```

* Create and use a Counter with a slight twist
```python
from collections import Counter
nyc_eatery_count_by_types = Counter(nyc_eatery_types)
```

* Use date parts for Grouping
```python
daily_violations = defaultdict(int)

for violation in parking_violations:
	violation_date = datetime.strptime(violation[4], '%m/%d/%Y')
  daily_violations[violation_date.day] += 1
```

* Group data my Month
* The date components we learned about earlier:
```python
from collections import defaultdict

eateries_by_park = defaultdict(list)

for park_id, name in nyc_eateries_parks:
	eateries_by_park[park_id].append(name)
```

* Find 5 most common locations for crime each month
```python
print(nyc_eatery_count_by_types.most_common(3))
```

#### Reading your data with CSV Reader and Establishing your Data Containers
Let's get started! The exercises in this chapter are intentionally more challenging, to give you a chance to really solidify your knowledge. Don't lose heart if you find yourself stuck; think back to the concepts you've learned in previous chapters and how you can apply them to this crime dataset. Good luck!

Your data file, crime_sampler.csv contains the date (1st column), block where it occurred (2nd column), primary type of the crime (3rd), description of the crime (4th), description of the location (5th), if an arrest was made (6th), was it a domestic case (7th), and city district (8th).

Here, however, you'll focus only 4 columns: The date, type of crime, location, and whether or not the crime resulted in an arrest.

Your job in this exercise is to use a CSV Reader to load up a list to hold the data you're going to analyze.

* Import the Python csv module.
* Create a Python file object in read mode for crime_sampler.csv called csvfile.
* Create an empty list called crime_data.
* Loop over a csv reader on the file object :
	* Inside the loop, append the date (first element), type of crime (third element), location description (fifth element), and arrest (sixth element) to the crime_data list.
* Remove the first element (headers) from the crime_data list.
* Print the first 10 records of the crime_data list. This has been done for you, so hit 'Submit Answer' to see the result!
```python
cat > crime_sampler.csv << EOF
Date,Block,Primary Type,Description,Location Description,Arrest,Domestic,District
05/23/2016 05:35:00 PM,024XX W DIVISION ST,ASSAULT,SIMPLE,STREET,false,true,14
03/26/2016 08:20:00 PM,019XX W HOWARD ST,BURGLARY,FORCIBLE ENTRY,SMALL RETAIL STORE,false,false,24
04/25/2016 03:05:00 PM,001XX W 79TH ST,THEFT,RETAIL THEFT,DEPARTMENT STORE,true,false,6
04/26/2016 05:30:00 PM,010XX N PINE AVE,BATTERY,SIMPLE,SIDEWALK,false,false,15
06/19/2016 01:15:00 AM,027XX W AUGUSTA BLVD,BATTERY,AGGRAVATED: HANDGUN,SIDEWALK,false,false,12
05/28/2016 08:00:00 PM,070XX S ASHLAND AVE,BATTERY,DOMESTIC BATTERY SIMPLE,GAS STATION,false,true,7
07/03/2016 03:43:00 PM,0000X N STATE ST,THEFT,RETAIL THEFT,OTHER,false,false,1
06/11/2016 06:55:00 PM,044XX W MAYPOLE AVE,PUBLIC PEACE VIOLATION,RECKLESS CONDUCT,STREET,true,false,11
10/04/2016 10:20:00 AM,016XX W 63RD ST,BATTERY,SIMPLE,STREET,true,false,7
02/14/2017 09:00:00 PM,018XX S WOOD ST,CRIMINAL DAMAGE,TO CITY OF CHICAGO PROPERTY,PARK PROPERTY,false,false,12
03/01/2017 12:29:00 AM,001XX N WESTERN AVE,ROBBERY,ARMED: HANDGUN,CURRENCY EXCHANGE,false,false,12
12/29/2016 10:00:00 AM,071XX S NORMAL BLVD,ASSAULT,AGGRAVATED:KNIFE/CUTTING INSTR,APARTMENT,false,true,7
EOF

# Import the csv module
import csv

# Create the file object: csvfile
csvfile = open('crime_sampler.csv', 'r')

# Create an empty list: crime_data
crime_data = []

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):

    # Append the date, type of crime, location description, and arrest
    crime_data.append((row[0], row[2], row[4], row[5]))
    
# Remove the first element from crime_data
crime_data.pop(0)

# Print the first 10 records
print(crime_data[:10])
```

#### Find the Months with the Highest Number of Crimes
Using the crime_data list from the prior exercise, you'll answer a common question that arises when dealing with crime data: How many crimes are committed each month?

Feel free to use the IPython Shell to explore the crime_data list - it has been pre-loaded for you. For example, crime_data[0][0] will show you the first column of the first row which, in this case, is the date and time time that the crime occurred.
* Import Counter from collections and datetime from datetime.
* Create a Counter object called crimes_by_month.
* Loop over the crime_data list:
	* Using the datetime.strptime() function, convert the first element of each item into a Python Datetime Object called date.
	* Increment the counter for the month associated with this row by one. You can access the month of date using date.month.
	* Print the 3 most common months for crime.
```python
# Import necessary modules
from collections import Counter
from datetime import datetime

# Create a Counter Object: crimes_by_month
crimes_by_month = Counter()

# Loop over the crime_data list
for row in crime_data:
    
    # Convert the first element of each item into a Python Datetime Object: date
    date = datetime.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')
    
    # Increment the counter for the month of the row by one
    crimes_by_month[date.month] += 1
    
# Print the 3 most common months for crime
print(crimes_by_month.most_common(3))
```

#### Transforming your Data Containers to Month and Location
Now let's flip your crime_data list into a dictionary keyed by month with a list of location values for each month, and filter down to the records for the year 2016. Remember you can use the shell to look at the crime_data list, such as crime_data[1][4] to see the location of the crime in the second item of the list (since lists start at 0).
* Import defaultdict from collections and datetime from datetime.
* Create a dictionary that defaults to a list called locations_by_month.
* Loop over the crime_data list:
	* Convert the first element to a date object exactly like you did in the previous exercise.
	* If the year is 2016, set the key of locations_by_month to be the month of date and .append() the location (fifth element of row) to the values list.
* Print the dictionary. This has been done for you, so hit 'Submit Answer' to see the result!
```python
# Import necessary modules
from collections import defaultdict
from datetime import datetime

# Create a dictionary that defaults to a list: locations_by_month
locations_by_month = defaultdict(list)

# Loop over the crime_data list
for row in crime_data:
    # Convert the first element to a date object
    date = datetime.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')
    
    # If the year is 2016 
    if date.year == 2016:
        # Set the dictionary key to the month and append the location (fifth element) to the values list
        locations_by_month[date.month].append(row[4])
    
# Print the dictionary
print(locations_by_month)
```

#### Find the Most Common Crimes by Location Type by Month in 2016
Using the locations_by_month dictionary from the prior exercise, you'll now determine common crimes by month and location type. Because your dataset is so large, it's a good idea to use Counter to look at an aspect of it in an easier to manageable size and learn more about it.
* Import Counter from collections.
* Loop over the items from your dictionary, using tuple expansion to unpack locations_by_month.items() into month and locations.
	* Make a Counter of the locations called location_count.
	* Print the month.
	* Print the five most common crime locations
```python
# Import Counter from collections
from collections import Counter

# Loop over the items from locations_by_month using tuple expansion of the month and locations
for month, locations in locations_by_month.items():
    # Make a Counter of the locations
    location_count = Counter(locations)
    # Print the month 
    print(month)
    # Print the most common location
    print(location_count.most_common(5))
```

## Case Study - Crimes by District and Differences by Block
* Read in the CSV data as a Dictionary
```python
import csv
csvfile = open('ART_GALLERY.csv', 'r')
for row in csv.DictReader(csvfile):
	print(row)
```

* Pop out the key and store the remaining dict
```python
galleries_10310 = art_galleries.pop('10310')
```

* Pythonically iterate over the Dictionary
```python
for zip_code, galleries in art_galleries.items():
	print(zip_code)
  print(galleries)
```

#### Wrapping Up
* Use sets for uniqueness
```python
cookies_eaten_today = ['chocolate chip', 'peanut butter', 'chocolate chip', 'oatmeal cream', 'chocolate chip']
types_of_cookies_eaten = set(cookies_eaten_today)
print(types_of_cookies_eaten)
```
* `difference()` set method

#### Reading your Data with DictReader and Establishing your Data Containers
Your data file, crime_sampler.csv contains in positional order: the date, block where it occurred, primary type of the crime, description of the crime, description of the location, if an arrest was made, was it a domestic case, and city district.

You'll now use a DictReader to load up a dictionary to hold your data with the district as the key and the rest of the data in a list. The csv, defaultdict, and datetime modules have already been imported for you.
* Create a Python file object in read mode for crime_sampler.csv called csvfile.
* Create a dictionary that defaults to a list called crimes_by_district.
* Loop over a DictReader of the CSV file:
	* Pop 'District' from each row and store it as district.
	* Append the rest of the data (row) to the district key of crimes_by_district.
```python
# Create the CSV file: csvfile
csvfile = open('crime_sampler.csv', 'r')

# Create a dictionary that defaults to a list: crimes_by_district
crimes_by_district = defaultdict(list)

# Loop over a DictReader of the CSV file
for row in csv.DictReader(csvfile):
    # Pop the district from each row: district
    district = row.pop('District')
    # Append the rest of the data to the list for proper district in crimes_by_district
    crimes_by_district[district].append(row)
```

#### Determine the Arrests by District by Year
Using your crimes_by_district dictionary from the previous exercise, you'll now determine the number arrests in each City district for each year. Counter is already imported for you. You'll want to use the IPython Shell to explore the crimes_by_district dictionary to determine how to check if an arrest was made.
* Loop over the crimes_by_district dictionary, unpacking it into the variables district and crimes.
	* Create an empty Counter object called year_count.
	* Loop over the crimes:
  	* If there was an arrest,
		* Convert crime['Date'] to a datetime object called year.
		* Add the crime to the Counter for the year, by using year as the key of year_count.
* Print the Counter. This has been done for you, so hit 'Submit Answer' to see the result!
```python
# Loop over the crimes_by_district using expansion as district and crimes
for district, crimes in crimes_by_district.items():
    # Print the district
    print(district)
    
    # Create an empty Counter object: year_count
    year_count = Counter()
    
    # Loop over the crimes:
    for crime in crimes:
        # If there was an arrest
        if crime['Arrest'] == 'true':
            # Convert the Date to a datetime and get the year
            year = datetime.strptime(crime['Date'], '%m/%d/%Y %I:%M:%S %p').year
            # Increment the Counter for the year
            year_count[year] += 1
            
    # Print the counter
    print(year_count)
```

#### Unique Crimes by City Block
You're in the home stretch!

Here, your data has been reshaped into a dictionary called crimes_by_block in which crimes are listed by city block. Your task in this exercise is to get a unique list of crimes that have occurred on a couple of the blocks that have been selected for you to learn more about. You might remember that you used set() to solve problems like this in Chapter 1.

* Create a unique list of crimes for the '001XX N STATE ST' block called n_state_st_crimes and print it.
* Create a unique list of crimes for the '0000X W TERMINAL ST' block called w_terminal_st_crimes and print it.
* Find the crimes committed on 001XX N STATE ST but not 0000X W TERMINAL ST. Store the result as crime_differences and print it.
```python
print(crimes_by_block)

# Create a unique list of crimes for the first block: n_state_st_crimes
n_state_st_crimes = set(crimes_by_block['001XX N STATE ST'])

# Print the list
print(n_state_st_crimes)

# Create a unique list of crimes for the second block: w_terminal_st_crimes
w_terminal_st_crimes = set(crimes_by_block['0000X W TERMINAL ST'])

# Print the list
print(w_terminal_st_crimes)

# Find the differences between the two blocks: crime_differences
crime_differences = n_state_st_crimes.difference(w_terminal_st_crimes)

# Print the differences
print(crime_differences)
```




