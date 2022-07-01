## Dictionary

* A dictionary is an unordered data structure
* Elements are separated by a comma and stored as key : value pair
* A dictionary is enclosed within curly brackets.

```python
# define the key value pairs
my_dictionary = {
    'name'  : 'abc'
    'age'   :  21
    'roll_no': '19'
    'percentage': 85,
    'attendance': 74,
    'city': 'gurugram',
    'country': 'india'
}

my_dictionary[0]    # error bcz unordered data structure

# access key value pair of the dictionary
my_dictionary['name']

# update value of the key
my_dictionary['age'] = 25

# get the keys of the dictionary
my_dictionary.keys()

# get the values of the dictionary
my_dictionary.values()

# get the key and value both
my_dictionary.items()

# update dictionary with a dictionary
my_dictionary.update({'pincode': 110024, 'last_name': 'xyz'}) 

my_dictionary.update([('housecode', 110024), ('first_name', 'xyz')])

# add new key to the dictionary
my_dictionary['new_key'] = 'new_value'
```

#### Most of the data types can be used as keys in Dictionaries
sample = {
    'string': 'string',
    10      : 'integer',
    1.5     : 'float',
    False   : 'boolean'
}

If we add duplicate keys, it will not throw an error instead it will overwrite the value which is added in the last.
sample = {
    'string': 'string',
    10      : 'integer',
    1.5     : 'float',
    False   : 'boolean',
    'string : 'A'
}


#### A dictionary key must be of a type that is immutable
```python
# list is mutable, hence not allowed
sample = {
    1: 'integer',
    [1, 2]: 'list'
}

# set is mutable, hence not allowed
sample = {
    1: 'integer',
    {1, 2}: 'set'
}

# tuple is immutable, hence it is allowed
sample = {
    1: 'integer',
    (1, 2): 'tuple'
}
```


#### Iterate through key-value pairs of the dictionary
```python
for key,value in my_dictionary.items():
    print(key, value)
```

#### Sort the dictionary by key
```python
m_dict = {
    'KL Rahul': 45,
    'Rohit': 22,
    'Virat': 31,
    'Dhawan': 17,
    'Rishabh': 10
}

sorted(m_dict.items())
```