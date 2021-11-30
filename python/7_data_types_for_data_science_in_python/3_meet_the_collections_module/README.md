## Meet the collections module

#### Collections Module
* Part of standard library
* Advanced data containers

#### Counter
* Special dictionary used for counting data, measuring frequency
```python
from collections import Counter
nyc_eatery_count_by_types = Counter(nyc_eatery_types)
print(nyc_eatery_count_by_types['Restaurant'])
```

#### Counter to find the most common
* `.most_common()` method returns the counter values in descending order
```print(nyc_eatery_count_by_types.most_common(3))```

#### Using Counter on lists
Counter is a powerful tool for counting, validating, and learning more about the elements within a dataset that is found in the collections module. You pass an iterable (list, set, tuple) or a dictionary to the Counter. You can also use the Counter object similarly to a dictionary with key/value assignment, for example counter[key] = value.

A common usage for Counter is checking data for consistency prior to using it, so let's do just that. In this exercise, you'll be using data from the Chicago Transit Authority on ridership.

* Import the Counter object from collections.

* Print the first ten items from the stations list.

* Create a Counter of the stations list called station_count.

* Print the station_count

```python
print(stations)

# Import the Counter object
from collections import Counter

# Print the first ten items from the stations list
print(stations[:10])

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Print the station_count
print(station_count)
```

#### Finding most common elements
Another powerful usage of Counter is finding the most common elements in a list. This can be done with the .most_common() method.

Practice using this now to find the most common stations in a stations list.

* Import the Counter object from collections.
* Create a Counter of the stations list called station_count.
* Print the 5 most common elements.
```python
# Import the Counter object
from collections import Counter

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Find the 5 most common elements
print(station_count.most_common(5))
```

#### Dictionaries of unknown structure - Defaultdict
```python
for park_id, name in nyc_eateries_parks:
	if park_id not in eateries_by_park:
  	eateries_by_park[park_id] = []
  eateries_by_park[park_id].append(name)
print(eateries_by_park['M010'])
```

#### Using defaultdict
* Pass it a default type that every key will have even if it
* Works exactly like a dictionary
```python
# for list
from collections import defaultdict
eateries_by_park = defaultdict(list)
for park_id, name in nyc_eateries_parks:
  eateries_by_park[park_id].append(name)
print(eateries_by_park['M010'])

# for number
from collections import defaultdict
eatery_contact_types = defaultdict(int)
for eatery in nyc_eateries:
	if eatery.get('phone'):
  	eatery_contact_types['phones'] += 1
  if eatery.get('website'):
  	eatery_contact_types['websites'] += 1
print(eatery_contact_types)
```

#### Creating dictionaries of an unknown structure
Occasionally, you'll need a structure to hold nested data, and you may not be certain that the keys will all actually exist. This can be an issue if you're trying to append items to a list for that key. You might remember the NYC data that we explored in the video. In order to solve the problem with a regular dictionary, you'll need to test that the key exists in the dictionary, and if not, add it with an empty list.

You'll be working with a list of entries that contains ridership details on the Chicago transit system.

* Create an empty dictionary called ridership.
* Iterate over entries, unpacking it into the variables date, stop, and riders.
* Check to see if the date already exists in the ridership dictionary. If it does not exist, create an empty list for the date key.
* Append a tuple consisting of stop and riders to the date key of the ridership dictionary.
Print the ridership for '03/09/2016'.
```python
cat cta_daily_station_totals.csv
station_id,stationname,date,daytype,rides
40010,Austin-Forest Park,01/01/2015,SUNDAY/HOLIDAY,587
40010,Austin-Forest Park,01/02/2015,WEEKDAY,1386
40010,Austin-Forest Park,01/03/2015,SATURDAY,785
40010,Austin-Forest Park,01/04/2015,SUNDAY/HOLIDAY,625
40010,Austin-Forest Park,01/05/2015,WEEKDAY,1752
40010,Austin-Forest Park,01/06/2015,WEEKDAY,1777
40010,Austin-Forest Park,01/07/2015,WEEKDAY,1269
40010,Austin-Forest Park,01/08/2015,WEEKDAY,1435
40010,Austin-Forest Park,01/09/2015,WEEKDAY,1631
40010,Austin-Forest Park,01/10/2015,SATURDAY,771
40010,Austin-Forest Park,01/11/2015,SUNDAY/HOLIDAY,588
40010,Austin-Forest Park,01/12/2015,WEEKDAY,2065
40010,Austin-Forest Park,01/13/2015,WEEKDAY,2108
40010,Austin-Forest Park,01/14/2015,WEEKDAY,2012
40010,Austin-Forest Park,01/15/2015,WEEKDAY,2069
40010,Austin-Forest Park,01/16/2015,WEEKDAY,2003
40010,Austin-Forest Park,01/17/2015,SATURDAY,953
40010,Austin-Forest Park,01/18/2015,SUNDAY/HOLIDAY,706
40010,Austin-Forest Park,01/19/2015,WEEKDAY,1216
40010,Austin-Forest Park,01/20/2015,WEEKDAY,2115
40010,Austin-Forest Park,01/21/2015,WEEKDAY,2132
40010,Austin-Forest Park,01/22/2015,WEEKDAY,2185
40010,Austin-Forest Park,01/23/2015,WEEKDAY,2072
40010,Austin-Forest Park,01/24/2015,SATURDAY,854
40010,Austin-Forest Park,01/25/2015,SUNDAY/HOLIDAY,585
40010,Austin-Forest Park,01/26/2015,WEEKDAY,2095
40010,Austin-Forest Park,01/27/2015,WEEKDAY,2251
40010,Austin-Forest Park,01/28/2015,WEEKDAY,2133
40010,Austin-Forest Park,01/29/2015,WEEKDAY,2083
40010,Austin-Forest Park,01/30/2015,WEEKDAY,2074
40010,Austin-Forest Park,01/31/2015,SATURDAY,953
40020,Harlem-Lake,01/01/2015,SUNDAY/HOLIDAY,1106
40020,Harlem-Lake,01/02/2015,WEEKDAY,3113
40020,Harlem-Lake,01/03/2015,SATURDAY,1818
40020,Harlem-Lake,01/04/2015,SUNDAY/HOLIDAY,1339
40020,Harlem-Lake,01/05/2015,WEEKDAY,3287
40020,Harlem-Lake,01/06/2015,WEEKDAY,3446
40020,Harlem-Lake,01/07/2015,WEEKDAY,2580
40020,Harlem-Lake,01/08/2015,WEEKDAY,2998
40020,Harlem-Lake,01/09/2015,WEEKDAY,3252
40020,Harlem-Lake,01/10/2015,SATURDAY,1849
40020,Harlem-Lake,01/11/2015,SUNDAY/HOLIDAY,1403
40020,Harlem-Lake,01/12/2015,WEEKDAY,3648
40020,Harlem-Lake,01/13/2015,WEEKDAY,3672
40020,Harlem-Lake,01/14/2015,WEEKDAY,3724
40020,Harlem-Lake,01/15/2015,WEEKDAY,3797
40020,Harlem-Lake,01/16/2015,WEEKDAY,3843
40020,Harlem-Lake,01/17/2015,SATURDAY,2392
40020,Harlem-Lake,01/18/2015,SUNDAY/HOLIDAY,1514
40020,Harlem-Lake,01/19/2015,WEEKDAY,2737
40020,Harlem-Lake,01/20/2015,WEEKDAY,3800
40020,Harlem-Lake,01/21/2015,WEEKDAY,3940
40020,Harlem-Lake,01/22/2015,WEEKDAY,3912
40020,Harlem-Lake,01/23/2015,WEEKDAY,3833
40020,Harlem-Lake,01/24/2015,SATURDAY,2261
40020,Harlem-Lake,01/25/2015,SUNDAY/HOLIDAY,1402
40020,Harlem-Lake,01/26/2015,WEEKDAY,3673
40020,Harlem-Lake,01/27/2015,WEEKDAY,3885
40020,Harlem-Lake,01/28/2015,WEEKDAY,3944
40020,Harlem-Lake,01/29/2015,WEEKDAY,3872
40020,Harlem-Lake,01/30/2015,WEEKDAY,4010
40020,Harlem-Lake,01/31/2015,SATURDAY,2311
40030,Pulaski-Lake,01/01/2015,SUNDAY/HOLIDAY,811
40030,Pulaski-Lake,01/02/2015,WEEKDAY,1529


# Create an empty dictionary: ridership
ridership = dict()

# Iterate over the entries
for date, stop, riders in entries:
    # Check to see if date is already in the ridership dictionary
    if date not in ridership:
        # Create an empty list for any missing date
        ridership[date] = []
    # Append the stop and riders as a tuple to the date keys list
    ridership[date].append((stop, riders))
    
# Print the ridership for '03/09/2016'
print(ridership['03/09/2016'])
```

#### Safely appending to a key's value list
Often when working with dictionaries, you will need to initialize a data type before you can use it. A prime example of this is a list, which has to be initialized on each key before you can append to that list.

A defaultdict allows you to define what each uninitialized key will contain. When establishing a defaultdict, you pass it the type you want it to be, such as a list, tuple, set, int, string, dictionary or any other valid type object.
* Import defaultdict from collections.
* Create a defaultdict with a default type of list called ridership.
* Iterate over the list entries, unpacking it into the variables date, stop, and riders, exactly as you did in the previous exercise.
	* Use stop as the key of the ridership dictionary and append riders to its value.
* Print the first 10 items of the ridership dictionary. You can use the .items() method for this. Remember, you have to convert ridership.items() to a list before slicing.
```python
# entries is a list of items saved in entries.txt file

# Import defaultdict
from collections import defaultdict

# Create a defaultdict with a default type of list: ridership
ridership = defaultdict(list)

# Iterate over the entries
for date, stop, riders in entries:
    # Use the stop as the key of ridership and append the riders to its value
    ridership[stop].append(riders)
    
# Print the first 10 items of the ridership dictionary
print(list(ridership.items())[:10])
```

#### Order in Python dictionaries
* Python version < 3.6 NOT ordered
* Python version > 3.6 ordered

#### Getting started with OrderedDict
```python
from collections import OrderedDict
nyc_eatery_permits = OrderedDict()
for eatery in nyc_eateries:
	nyc_eatery_permits[eatery['end_date']] = eatery
print(list(nyc_eatery_permits.items())[:3])
```

#### OrderedDict power feature
* `.popitem()` method returns items in reverse insertion order
```print(nyc_eatery_permits.popitem())```
* You can use the `last=False` keyword argument to return the items in insertion order
```print(nyc_eatery_permits.popitem(last=False))```

#### Working with OrderedDictionaries
Recently in Python 3.6, dictionaries were made to maintain the order in which the keys were inserted; however, in all versions prior to that you need to use an OrderedDict to maintain insertion order.

Let's create a dictionary of all the stop times by route and rider, then use it to find the ridership throughout the day.

* Import OrderedDict from collections.
* Create an OrderedDict called ridership_date.
* Iterate over the list entries, unpacking it into date and riders.
* If a key does not exist in ridership_date for the date, set it equal to 0 (if only you could use defaultdict here!)
* Add riders to the date key of ridership_date.
* Print the first 31 records. Remember to convert the items into a list.
```python
# Import OrderedDict from collections
from collections import OrderedDict

# Create an OrderedDict called: ridership_date
ridership_date = OrderedDict()

# Iterate over the entries
for date, riders in entries:
    # If a key does not exist in ridership_date, set it to 0
    if date not in ridership_date:
        ridership_date[date] = 0
        
    # Add riders to the date key in ridership_date
    ridership_date[date] += riders
    
# Print the first 31 records
print(list(ridership_date.items())[:31])
```

#### Powerful Ordered popping
Where OrderedDicts really shine is when you need to access the data in the dictionary in the order you added it. OrderedDict has a .popitem() method that will return items in reverse of which they were inserted. You can also pass .popitem() the last=False keyword argument and go through the items in the order of how they were added.

Here, you'll use the ridership_date OrderedDict you created in the previous exercise.

* Print the first key in ridership_date (Remember to make keys a list before slicing).
* Pop the first item from ridership_date and print it.
* Print the last key in ridership_date.
* Pop the last item from ridership_date and print it.
```python
# Print the first key in ridership_date
print(list(ridership_date.keys())[0])

# Pop the first item from ridership_date and print it
print(ridership_date.popitem(last=False))

# Print the last key in ridership_date
print(list(ridership_date.keys())[-1])

# Pop the last item from ridership_date and print it
print(ridership_date.popitem())
```

#### Namedtuple
* A tuple where each position (column) has a name.
* Ensure each one has the same properties
* Alternative to a `pandas` Dataframe now

#### Creating a namedtuple
* Pass a name and a list of fields
```python
from collections import namedtuple
Eatery = namedtuple('Eatery', ['name', 'location', 'park_id', 'type_name'])
eateries = []
for eatery in nyc_eateries:
    details = Eatery(eatery['name'],
                     eatery['location'],
                     eatery['park_id'],
                     eatery['type_name'])
    eateries.append(details)

# print the first element
print(eateries[0])
```

#### Leveraging namedtuples
* Each field is available as an attribute of the namedtuple
```python
for eatery in eateries[:3]:
    print(eatery.name)
    print(eatery.park_id)
    print(eatery.location)
```

#### Creating namedtuples for storing data
Often times when working with data, you will use a dictionary just so you can use key names to make reading the code and accessing the data easier to understand. Python has another container called a namedtuple that is a tuple, but has names for each position of the tuple. You create one by passing a name for the tuple type and a list of field names.

For example, Cookie = namedtuple("Cookie", ['name', 'quantity']) will create a container, and you can create new ones of the type using Cookie('chocolate chip', 1) where you can access the name using the name attribute, and then get the quantity using the quantity attribute.

* Import namedtuple from collections.
* Create a namedtuple called DateDetails with a type name of DateDetails and fields of 'date', 'stop', and 'riders'.
* Create a list called labeled_entries.
* Iterate over the entries list, unpacking it into date, stop, and riders.
* Create a new DateDetails namedtuple instance for each entry and append it to labeled_entries.
* Print the first 5 items in labeled_entries. This has been done for you, so hit 'Submit Answer' to see the result!
```python
# Import namedtuple from collections
from collections import namedtuple

# Create the namedtuple: DateDetails
DateDetails = namedtuple('DateDetails', ['date', 'stop', 'riders'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the entries list
for date, stop, riders in entries:
    # Append a new DateDetails namedtuple instance for each entry to labeled_entries
    labeled_entries.append(DateDetails(date, stop, riders))
    
# Print the first 5 items in labeled_entries
print(labeled_entries[:5])
```

#### Leveraging attributes on namedtuples
Once you have a namedtuple, you can write more expressive code that is easier to understand. Remember, you can access the elements in the tuple by their name as an attribute. For example, you can access the date of the namedtuples in the previous exercise using the .date attribute.

Here, you'll use the tuples you made in the previous exercise to see how this works.

* Iterate over the first twenty items in the labeled_entries list:
    * Print each item's stop.
    * Print each item's date.
    * Print each item's riders.
```python
# Iterate over the first twenty items in labeled_entries
for item in labeled_entries[:20]:
    # Print each item's stop
    print(item.stop)

    # Print each item's date
    print(item.date)

    # Print each item's riders
    print(item.riders)
```