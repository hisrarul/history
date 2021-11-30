## Dictionaries - the root of python

#### Creating and looping through dictionaries
* Hold data in key/value pairs
* Nestable (use a dictionary as the value of a key within a dictionary)
* Iterable
* Created by dict() or {}
```python
art_galleries = {}

for name, zip_codes in galleries:
    art_galleries[name] = zip_code

# printing in loop
for name in art_galleries:
    print(name)
```

#### Safely finding by key
* `.get()` method allows you to safely access a key without error or exception handling
* If a key is not in the dictionary, `.get()` returns `None` by default or you can supply a value to return
```python
art_galleries['Louvre']
art_galleries.get('Louvre', 'Not found')
```

#### Working with nested dictionaries
* The keys() method shows the keys for a given dictionary
```python
art_galleries.keys()

# get value of a key
print(art_galleries['10027'])
```

#### Accessing nested data
* Command way to deal with repeating data structures
* Can be accessed using multiple indices or the `.get()` method
```python
art_galleries['10027']['Inner Art Gallery Inc']
```

#### Creating and looping through dictionaries
You start that by creating an empty dictionary and assigning part of your array data as the key and the rest as the value.

Previously, you used sorted() to organize your data in a list. Dictionaries can also be sorted. By default, using sorted() on a dictionary will sort by the keys of the dictionary. You can also reverse the order by passing reverse=True as a keyword argument.
* Create an empty dictionary called names_by_rank.
* Loop over female_baby_names_2012.items(), unpacking it into the variables rank and name.
* Inside the loop, add each name to the names_by_rank dictionary using the rank as the key.
* Sort the names_by_rank dictionary keys in descending order, select the first ten items. Print each item.
```python
# print(female_baby_names_2012)
{1: 'EMMA', 2: 'LEAH', 3: 'SARAH', 4: 'SOPHIA', 5: 'ESTHER', 6: 'RACHEL', 7: 'CHAYA', 8: 'AVA', 9: 'CHANA', 10: 'MIRIAM', 11: 'ELLA', 12: 'EMILY', 13: 'MIA', 14: 'SARA', 15: 'CHARLOTTE', 16: 'ISABELLA', 17: 'MAYA', 18: 'ELIZABETH', 19: 'ABIGAIL', 20: 'ALEXANDRA', 21: 'VICTORIA', 22: 'LILY', 23: 'SOFIA', 24: 'RIVKA', 25: 'ZOE', 26: 'JULIA', 27: 'SOPHIE', 28: 'GABRIELLA', 29: 'HANNAH', 30: 'GRACE', 31: 'AVERY', 32: 'STELLA', 33: 'SHAINDY', 34: 'FAIGY', 35: 'GITTY', 36: 'MADISON', 37: 'MALKY', 38: 'EVA', 39: 'MALKA', 40: 'ALEXA', 41: 'MADELINE', 42: 'PENELOPE', 43: 'TOBY', 44: 'RIVKY', 45: 'NICOLE', 46: 'VIOLET', 47: 'NATALIE', 48: 'REBECCA', 49: 'MARIA', 50: 'YITTY', 51: 'NINA', 52: 'KATHERINE', 53: 'RILEY', 54: 'SIENNA', 55: 'SYDNEY', 56: 'VIVIENNE', 57: 'VALENTINA', 58: 'TALIA', 59: 'JOSEPHINE', 60: 'FRANCESCA', 61: 'ZISSY', 62: 'SURY', 63: 'NAOMI', 64: 'YIDES', 65: 'SKYLAR', 66: 'VERONICA', 67: 'TAYLOR', 68: 'ZOEY', 69: 'LILIANA', 70: 'YAEL', 71: 'SAVANNAH', 72: 'VANESSA', 73: 'SIMONE', 74: 'SLOANE', 75: 'VERA', 76: 'YEHUDIS', 77: 'SYLVIA', 78: 'SIMA', 79: 'SHAINA', 80: 'TZIPORA', 81: 'YITTA', 82: 'TZIVIA', 83: 'YARA'}

# Create an empty dictionary: names_by_rank
names_by_rank = {}

# Loop over the girl names
for rank, name in female_baby_names_2012.items():
    # Add each name to the names_by_rank dictionary using rank as the key
    names_by_rank[rank] = name
    
# Sort the names_by_rank dict by rank in descending order and slice the first 10 items
for rank in sorted(names_by_rank, reverse=True)[:10]:
    # Print each item
    print(names_by_rank[rank])
```

#### Safely finding by key
If you attempt to access a key that isn't present in a dictionary, you'll get a KeyError. One option to handle this type of error is to use a try: except: block.

Python provides a faster, more versatile tool to help with this problem in the form of the .get() method. The .get() method allows you to supply the name of a key, and optionally, what you'd like to have returned if the key is not found.

* Safely print rank 7 from the names dictionary.
* Safely print the type of rank 100 from the names dictionary.
* Safely print rank 105 from the names dictionary or 'Not Found' if 105 is not found.
```python
# Safely print rank 7 from the names dictionary
print(names.get(7))

# Safely print the type of rank 100 from the names dictionary
print(type(names.get(100)))

# Safely print rank 105 from the names dictionary or 'Not Found'
print(names.get(105, 'Not Found'))
```

#### Dealing with nested data
A dictionary can contain another dictionary as the value of a key, and this is a very common way to deal with repeating data structures such as yearly, monthly or weekly data. All the same rules apply when creating or accessing the dictionary.

For example, if you had a dictionary that had a ranking of my cookie consumption by year and type of cookie. It might look like
```python
cookies = {'2017': {'chocolate chip': 483, 'peanut butter': 115}, '2016': {'chocolate chip': 9513, 'peanut butter': 6792}}
```

I could access how many chocolate chip cookies I ate in 2016 using cookies['2016']['chocolate chip'].
	
When exploring a new dictionary, it can be helpful to use the .keys() method to get an idea of what data might be available within the dictionary. You can also iterate over a dictionary and it will return each key in the dictionary for you to use inside the loop.

* Print the keys of the boy_names dictionary.
* Print the keys of the boy_names dictionary for the year 2013.
* Loop over the boy_names dictionary.
	* Inside the loop, safely print the year and the third ranked name. Print 'Unknown' if the third ranked name is not found.
```python
print(boy_names)
{2012: {}, 2013: {1: 'David', 2: 'Joseph', 3: 'Michael', 4: 'Moshe', 5: 'Daniel', 6: 'Benjamin', 7: 'James', 8: 'Jacob', 9: 'Jack', 10: 'Alexander', 11: 'William', 12: 'John', 13: 'Henry', 14: 'Noah', 15: 'Samuel', 16: 'Nicholas', 17: 'Matthew', 18: 'Adam', 19: 'Chaim', 20: 'Abraham', 21: 'Liam', 22: 'Ryan', 23: 'Lucas', 24: 'Anthony', 25: 'Isaac', 26: 'Oliver', 27: 'Andrew', 28: 'Gabriel', 29: 'Yosef', 30: 'Leo', 31: 'Thomas', 32: 'Luke', 33: 'Jackson', 34: 'Shimon', 35: 'Theodore', 36: 'Joshua', 37: 'Christopher', 38: 'Sebastian', 39: 'Mason', 40: 'Eli', 41: 'Nathan', 42: 'Aaron', 43: 'Zachary', 44: 'Aron', 45: 'Luca', 46: 'Yehuda', 47: 'Yitzchok', 48: 'Owen', 49: 'Menachem', 50: 'Logan', 51: 'Aiden', 52: 'Yisroel', 53: 'Peter', 54: 'Yaakov', 55: 'Yakov', 56: 'Omar', 57: 'Levi', 58: 'Simon', 59: 'Shmuel', 60: 'Patrick', 61: 'Connor', 62: 'Jonah', 63: 'Zev', 64: 'Tzvi', 65: 'Nathaniel', 66: 'Harrison', 67: 'Tyler', 68: 'Mark', 69: 'Hunter', 70: 'Mohamed', 71: 'Lipa', 72: 'Mendel', 73: 'Sean', 74: 'Sam', 75: 'Solomon', 76: 'Martin', 77: 'Edward', 78: 'Wyatt', 79: 'Parker', 80: 'Steven', 81: 'Yechiel', 82: 'Nicolas', 83: 'Timothy', 84: 'Spencer', 85: 'Usher', 86: 'Rafael', 87: 'Yusuf', 88: 'Yehoshua', 89: 'Shaya', 90: 'Rayan', 91: 'Tristan', 92: 'Yossi', 93: 'Wesley', 94: 'Yoel', 95: 'Sawyer', 96: 'Yousef', 97: 'Walter', 98: 'Zalmen', 99: 'Yeshaya', 100: 'Yitzchak'}, 2014: {1: 'Joseph', 2: 'David', 3: 'Michael', 4: 'Moshe', 5: 'Jacob', 6: 'Benjamin', 7: 'Alexander', 8: 'Daniel', 9: 'Samuel', 10: 'Jack', 11: 'James', 12: 'Adam', 13: 'William', 14: 'Henry', 15: 'Abraham', 16: 'Nicholas', 17: 'John', 18: 'Ethan', 19: 'Liam', 20: 'Ryan', 21: 'Noah', 22: 'Matthew', 23: 'Chaim', 24: 'Theodore', 25: 'Isaac', 26: 'Lucas', 27: 'Thomas', 28: 'Yosef', 29: 'Anthony', 30: 'Oliver', 31: 'Max', 32: 'Gabriel', 33: 'Eli', 34: 'Shimon', 35: 'Luke', 36: 'Mason', 37: 'Mordechai', 38: 'Andrew', 39: 'Zachary', 40: 'Owen', 41: 'Yehuda', 42: 'Jackson', 43: 'Yisroel', 44: 'Nathan', 45: 'Aiden', 46: 'Christopher', 47: 'Jonathan', 48: 'Asher', 49: 'Logan', 50: 'Robert', 51: 'Yitzchok', 52: 'George', 53: 'Christian', 54: 'Aron', 55: 'Mark', 56: 'Levi', 57: 'Shmuel', 58: 'Miles', 59: 'Shlomo', 60: 'Peter', 61: 'Sean', 62: 'Eliezer', 63: 'Solomon', 64: 'Gavin', 65: 'Zev', 66: 'Nathaniel', 67: 'Yaakov', 68: 'Yakov', 69: 'Hunter', 70: 'Vincent', 71: 'Ari', 72: 'Edward', 73: 'Yechiel', 74: 'Oscar', 75: 'Shia', 76: 'Leonardo', 77: 'Victor', 78: 'Tyler', 79: 'Wyatt', 80: 'Sam', 81: 'Shaya', 82: 'Ian', 83: 'Raphael', 84: 'Philip', 85: 'Timothy', 86: 'Yehoshua', 87: 'Xavier', 88: 'Youssef', 89: 'Simcha', 90: 'Naftali', 91: 'Ronan', 92: 'Usher', 93: 'Shmiel', 94: 'Yousef', 95: 'Naftuli', 96: 'Yusuf', 97: 'Yossi', 98: 'Yisrael', 99: 'Shea', 100: 'Yoel', 101: 'Yahya', 102: 'Yidel'}}

# Print a list of keys from the boy_names dictionary
print(boy_names.keys())

# Print a list of keys from the boy_names dictionary for the year 2013
print(boy_names[2013].keys())

# Loop over the dictionary
for year in boy_names:
    # Safely print the year and the third ranked name or 'Unknown'
    print(year, boy_names[year].get(3, 'Unknown'))
```

#### Adding and extending dictionaries
* Assignment to add a new key/value to a dictionary
* `.update()` method to update a dictionary from another dictionary, tuples or keywords
```python
user = {'location': 'delhi'}
print(user)
user['location'] = 'mumbai'
print(user)
```

#### Popping and deleting from dictionaries
* `del` instruction deletes a key/value
* `.pop()` method safely removes a key/value from a dictionary

#### Adding and extending dictionaries
If you have a dictionary and you want to add data to it, you can simply create a new key and assign the data you desire to it. It's important to remember that if it's a nested dictionary, then all the keys in the data path must exist, and each key in the path must be assigned individually.

You can also use the .update() method to update a dictionary with keys and values from another dictionary, tuples or keyword arguments.

Here, you'll combine several techniques used in prior exercises to setup your dictionary in a way that makes it easy to find the least popular baby name for each year.

Your job is to add data for the year 2011 to your dictionary by assignment, 2012 by update, and then find the least popular baby name for each year.

* Assign the names_2011 dictionary as the value to the 2011 key of the boy_names dictionary.
* Update the 2012 key in the boy_names dictionary with the following data in a list of tuples: (1, 'Casey'), (2, 'Aiden').
* Loop over the boy_names dictionary.
	* Inside the for loop, sort the data for each year of boy_names by descending rank and take the first result which will be the lowest ranked name.
	* Safely print the year and least popular name or 'Not Available' if it is not found. Take advantage of the .get() method.
```python
# print(names_2011)
{1: 'Michael', 2: 'Joseph', 3: 'Jacob', 4: 'David', 5: 'Benjamin', 6: 'Moshe', 7: 'Daniel', 8: 'Alexander', 9: 'Matthew', 10: 'Jack', 11: 'Samuel', 12: 'James', 13: 'William', 14: 'John', 15: 'Nicholas', 16: 'Henry', 17: 'Chaim', 18: 'Anthony', 19: 'Andrew', 20: 'Liam', 21: 'Charles', 22: 'Lucas', 23: 'Dylan', 24: 'Ryan', 25: 'Thomas', 26: 'Ethan', 27: 'Menachem', 28: 'Yosef', 29: 'Luke', 30: 'Oliver', 31: 'Noah', 32: 'Eli', 33: 'Gabriel', 34: 'Max', 35: 'Shimon', 36: 'Isaac', 37: 'Joshua', 38: 'Zachary', 39: 'Leo', 40: 'Julian', 41: 'Aiden', 42: 'Jake', 43: 'Mordechai', 44: 'Yisroel', 45: 'Yehuda', 46: 'Sebastian', 47: 'Mark', 48: 'Robert', 49: 'Logan', 50: 'George', 51: 'Owen', 52: 'Vincent', 53: 'Tyler', 54: 'Yakov', 55: 'Aidan', 56: 'Yitzchok', 57: 'Asher', 58: 'Theodore', 59: 'Peter', 60: 'Solomon', 61: 'Zev', 62: 'Nathaniel', 63: 'Yaakov', 64: 'Shmuel', 65: 'Shulem', 66: 'Tzvi', 67: 'Levi', 68: 'Jayden', 69: 'Mohamed', 70: 'Cole', 71: 'Sean', 72: 'Sam', 73: 'Victor', 74: 'Omar', 75: 'Steven', 76: 'Moses', 77: 'Shia', 78: 'Usher', 79: 'Nicolas', 80: 'Yechiel', 81: 'Shaya', 82: 'Wyatt', 83: 'Tristan', 84: 'Louis', 85: 'Yehoshua', 86: 'Sholom', 87: 'Yoel', 88: 'Rocco', 89: 'Xavier', 90: 'Yitzchak', 91: 'Shea', 92: 'Spencer', 93: 'Zalmen', 94: 'Yida', 95: 'Yousef', 96: 'Youssef', 97: 'Yonah'}

# print(boy_names)
{2012: {}, 2013: {1: 'David', 2: 'Joseph', 3: 'Michael', 4: 'Moshe', 5: 'Daniel', 6: 'Benjamin', 7: 'James', 8: 'Jacob', 9: 'Jack', 10: 'Alexander', 11: 'William', 12: 'John', 13: 'Henry', 14: 'Noah', 15: 'Samuel', 16: 'Nicholas', 17: 'Matthew', 18: 'Adam', 19: 'Chaim', 20: 'Abraham', 21: 'Liam', 22: 'Ryan', 23: 'Lucas', 24: 'Anthony', 25: 'Isaac', 26: 'Oliver', 27: 'Andrew', 28: 'Gabriel', 29: 'Yosef', 30: 'Leo', 31: 'Thomas', 32: 'Luke', 33: 'Jackson', 34: 'Shimon', 35: 'Theodore', 36: 'Joshua', 37: 'Christopher', 38: 'Sebastian', 39: 'Mason', 40: 'Eli', 41: 'Nathan', 42: 'Aaron', 43: 'Zachary', 44: 'Aron', 45: 'Luca', 46: 'Yehuda', 47: 'Yitzchok', 48: 'Owen', 49: 'Menachem', 50: 'Logan', 51: 'Aiden', 52: 'Yisroel', 53: 'Peter', 54: 'Yaakov', 55: 'Yakov', 56: 'Omar', 57: 'Levi', 58: 'Simon', 59: 'Shmuel', 60: 'Patrick', 61: 'Connor', 62: 'Jonah', 63: 'Zev', 64: 'Tzvi', 65: 'Nathaniel', 66: 'Harrison', 67: 'Tyler', 68: 'Mark', 69: 'Hunter', 70: 'Mohamed', 71: 'Lipa', 72: 'Mendel', 73: 'Sean', 74: 'Sam', 75: 'Solomon', 76: 'Martin', 77: 'Edward', 78: 'Wyatt', 79: 'Parker', 80: 'Steven', 81: 'Yechiel', 82: 'Nicolas', 83: 'Timothy', 84: 'Spencer', 85: 'Usher', 86: 'Rafael', 87: 'Yusuf', 88: 'Yehoshua', 89: 'Shaya', 90: 'Rayan', 91: 'Tristan', 92: 'Yossi', 93: 'Wesley', 94: 'Yoel', 95: 'Sawyer', 96: 'Yousef', 97: 'Walter', 98: 'Zalmen', 99: 'Yeshaya', 100: 'Yitzchak'}, 2014: {1: 'Joseph', 2: 'David', 3: 'Michael', 4: 'Moshe', 5: 'Jacob', 6: 'Benjamin', 7: 'Alexander', 8: 'Daniel', 9: 'Samuel', 10: 'Jack', 11: 'James', 12: 'Adam', 13: 'William', 14: 'Henry', 15: 'Abraham', 16: 'Nicholas', 17: 'John', 18: 'Ethan', 19: 'Liam', 20: 'Ryan', 21: 'Noah', 22: 'Matthew', 23: 'Chaim', 24: 'Theodore', 25: 'Isaac', 26: 'Lucas', 27: 'Thomas', 28: 'Yosef', 29: 'Anthony', 30: 'Oliver', 31: 'Max', 32: 'Gabriel', 33: 'Eli', 34: 'Shimon', 35: 'Luke', 36: 'Mason', 37: 'Mordechai', 38: 'Andrew', 39: 'Zachary', 40: 'Owen', 41: 'Yehuda', 42: 'Jackson', 43: 'Yisroel', 44: 'Nathan', 45: 'Aiden', 46: 'Christopher', 47: 'Jonathan', 48: 'Asher', 49: 'Logan', 50: 'Robert', 51: 'Yitzchok', 52: 'George', 53: 'Christian', 54: 'Aron', 55: 'Mark', 56: 'Levi', 57: 'Shmuel', 58: 'Miles', 59: 'Shlomo', 60: 'Peter', 61: 'Sean', 62: 'Eliezer', 63: 'Solomon', 64: 'Gavin', 65: 'Zev', 66: 'Nathaniel', 67: 'Yaakov', 68: 'Yakov', 69: 'Hunter', 70: 'Vincent', 71: 'Ari', 72: 'Edward', 73: 'Yechiel', 74: 'Oscar', 75: 'Shia', 76: 'Leonardo', 77: 'Victor', 78: 'Tyler', 79: 'Wyatt', 80: 'Sam', 81: 'Shaya', 82: 'Ian', 83: 'Raphael', 84: 'Philip', 85: 'Timothy', 86: 'Yehoshua', 87: 'Xavier', 88: 'Youssef', 89: 'Simcha', 90: 'Naftali', 91: 'Ronan', 92: 'Usher', 93: 'Shmiel', 94: 'Yousef', 95: 'Naftuli', 96: 'Yusuf', 97: 'Yossi', 98: 'Yisrael', 99: 'Shea', 100: 'Yoel', 101: 'Yahya', 102: 'Yidel'}}

# Assign the names_2011 dictionary as the value to the 2011 key of boy_names
boy_names[2011] = names_2011

# Update the 2012 key in the boy_names dictionary
boy_names[2012].update([(1, 'Casey'), (2, 'Aiden')])

# Loop over the years in the boy_names dictionary 
for year in boy_names:
    # Sort the data for each year by descending rank and get the lowest one
    lowest_ranked =  sorted(boy_names[year], reverse=True)[0]
    # Safely print the year and the least popular name or 'Not Available'
    print(year, boy_names[year].get(lowest_ranked, 'Not Available'))
```

#### Popping and deleting from dictionaries
Often, you will want to remove keys and value from a dictionary. You can do so using the del Python instruction. It's important to remember that del will throw a KeyError if the key you are trying to delete does not exist. You can not use it with the .get() method to safely delete items; however, it can be used with try: catch:.

If you want to save that deleted data into another variable for further processing, the .pop() dictionary method will do just that. You can supply a default value for .pop() much like you did for .get() to safely deal with missing keys. It's also typical to use .pop() instead of del since it is a safe method.

Here, you'll remove 2011 and 2015 to save them for later, and then delete 2012 from the dictionary.
* Remove 2011 from female_names and store it as female_names_2011.
* Safely remove 2015 from female_names with a empty dictionary as the default and store it as female_names_2015. To do this, pass in an empty dictionary {} as a second argument to .pop().
* Delete 2012 from female_names.
* Print female_names.
```python
# print(female_names)
{2011: {1: 'Olivia', 2: 'Esther', 3: 'Rachel', 4: 'Leah', 5: 'Emma', 6: 'Chaya', 7: 'Sarah', 8: 'Sophia', 9: 'Ava', 10: 'Miriam'}, 2012: {}, 2013: {1: 'Olivia', 2: 'Emma', 3: 'Esther', 4: 'Sophia', 5: 'Sarah', 6: 'Leah', 7: 'Rachel', 8: 'Chaya', 9: 'Miriam', 10: 'Chana'}, 2014: {1: 'Olivia', 2: 'Esther', 3: 'Rachel', 4: 'Leah', 5: 'Emma', 6: 'Chaya', 7: 'Sarah', 8: 'Sophia', 9: 'Ava', 10: 'Miriam'}}

# Remove 2011 from female_names and store it: female_names_2011
female_names_2011 = female_names.pop(2011)

# Safely remove 2015 from female_names with an empty dictionary as the default: female_names_2015
female_names_2015 = female_names.pop(2015, {})

# Delete 2012 from female_names
del female_names[2012]

# Print female_names
print(female_names)
```

#### Working with dictionaries more pythonically
* `.items()` method returns an object we can iterate over
```print(subjects.items())```
* `.get()` does a lot of work to check for a key
* `in` operator is much more efficient and cleaner

#### Working with dictionaries more pythonically
So far, you've worked a lot with the keys of a dictionary to access data, but in Python, the preferred manner for iterating
* Iterate over baby_names[2014], unpacking it into rank and name.
	* Print each rank and name.
* Repeat the process for baby_names[2012].
```python
# Iterate over the 2014 nested dictionary
for rank, name in baby_names[2014].items():
    # Print rank and name
    print(rank, name)
    
# Iterate over the 2012 nested dictionary

for rank, name in baby_names[2012].items():
    # Print rank and name
    print(rank, name)
```

#### Checking dictionaries for data
You can check to see if a key exists in a dictionary by using the in expression.

For example, you can check to see if 'cookies' is a key in the dictionary by using if 'cookies' in recipes_dict: this allows you to safely react to data being present in the dictionary.

You can also use the in expression so see if data is in the value of a dictionary such as if 'cookies' in recipes_dict.values(). 
* Check to see if 2011 is in the baby_names dictionary.
	* Print 'Found 2011' if it is present.
* Check to see if 1 is in baby_names[2012].
	* Print 'Found Rank 1 in 2012' if found and 'Rank 1 missing from 2012' if not found.
* Check to see if rank 5 is in baby_names[2013].
	* Print 'Found Rank 5' if it is present.
```python
# print(baby_names)
{2012: {}, 2013: {1: 'David', 2: 'Joseph', 3: 'Michael', 4: 'Moshe', 5: 'Daniel', 6: 'Benjamin', 7: 'James', 8: 'Jacob', 9: 'Jack', 10: 'Alexander'}, 2014: {1: 'Joseph', 2: 'David', 3: 'Michael', 4: 'Moshe', 5: 'Jacob', 6: 'Benjamin', 7: 'Alexander', 8: 'Daniel', 9: 'Samuel', 10: 'Jack'}}

# Check to see if 2011 is in baby_names
if 2011 in baby_names:
    # Print 'Found 2011'
    print('Found 2011')
    
# Check to see if rank 1 is in 2012
if 1 in baby_names[2012]:
    # Print 'Found Rank 1 in 2012' if found
    print('Found Rank 1 in 2012')
else:
    # Print 'Rank 1 missing from 2012' if not found
    print('Rank 1 missing from 2012')
    
# Check to see if Rank 5 is in 2013
if 5 in baby_names[2013]:
   # Print 'Found Rank 5'
   print('Found Rank 5')
```

#### Reading from a file using CSV reader
* Python `csv` module
* `open()` function provides a variable that represents a file, takes a path and a made
* `csv.reader()` reads a file object and returns the lines from the file as tuples
* `.close()` method closed file objects
```python
import csv
csvfile = open('ART.csv', 'r')
for row in csv.reader(csvfile):
  print(row)
csvfile.close()
```

#### Creating a dictionary from a file
* Often we want to go from CSV file to dictionary
* DictReader does just that
* If data doesn't have a header row, you can pass in the column names
```python
for row in csv.DictReader(csvfile):
	print(row)
```

#### Reading from a file using CSV reader
Python provides a wonderful module called csv to work with CSV files. You can pass the .reader() method of csv a Python file object and use it as you would any other iterable. To create a Python file object, you use the open() function, which accepts a file name and a mode. The mode is typically 'r' for read or 'w' for write.

Though you won't use it for this exercise, often CSV files will have a header row with field names, and you will need to use slice notation such as [1:] to skip the header row.

You'll now use the csv module to read the baby_names.csv file and fill the baby_names dictionary with data.
* Import the python csv module.
* Create a Python file object in read mode for baby_names.csv called csvfile with the open function.
* Use the reader method from the csv module on the file object in a for loop. Inside the loop:
	* Print each row and add the rank (the 6th element of row) as the key and name (the 4th element of row) as the value to the existing dictionary (baby_names).
* Print the keys of baby_names.
```python
cat >> baby_names.csv < EOF
BRITH_YEAR,GENDER,ETHNICTY,NAME,COUNT,RANK
2011,FEMALE,HISPANIC,GERALDINE,13,75
2011,FEMALE,HISPANIC,GIA,21,67
2011,FEMALE,HISPANIC,GIANNA,49,42
2011,FEMALE,HISPANIC,GISELLE,38,51
2011,FEMALE,HISPANIC,GRACE,36,53
2011,FEMALE,HISPANIC,GUADALUPE,26,62
2011,FEMALE,HISPANIC,HAILEY,126,8
2011,FEMALE,HISPANIC,HALEY,14,74
2011,FEMALE,HISPANIC,HANNAH,17,71
EOF

# Import the python CSV module
import csv

# Create a python file object in read mode for the baby_names.csv file: csvfile
csvfile = open('baby_names.csv', 'r')

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):
    # Print each row 
    print(row)
    # Add the rank and name to the dictionary
    baby_names[row[5]] = row[3]

# Print the dictionary keys
print(baby_names.keys())
```

#### Creating a dictionary from a file
The csv module also provides a way to directly create a dictionary from a CSV file with the DictReader class. If the file has a header row, that row will automatically be used as the keys for the dictionary. However, if not, you can supply a list of keys to be used. Each row from the file is returned as a dictionary. Using DictReader can make it much easier to read your code and understand what data is being used, especially when compared to the numbered indexes you used in the prior exercise.

Your job in this exercise is to create a dictionary directly from the data file using DictReader. NOTE: The misspellings are from the original data, and this is a very common issue. Again, the baby_names dictionary has already been created for you.

* Import the Python csv module.
* Create a Python file object in read mode for the baby_names.csv called csvfile.
* Loop over a csv DictReader on csvfile. Inside the loop:
	* Print each row.
	* Add the 'RANK' of each row as the key and 'NAME' of each row as the value to the existing dictionary.
* Print the dictionary keys.
```python
# Import the python CSV module
import csv

# Create a python file object in read mode for the `baby_names.csv` file: csvfile
csvfile = open('baby_names.csv', 'r')

# Loop over a DictReader on the file
for row in csv.DictReader(csvfile):
    # Print each row 
    print(row)
    # Add the rank and name to the dictionary: baby_names
    baby_names[row['RANK']] = row['NAME']

# Print the dictionary keys
print(baby_names.keys())
```
