## Tuple
* We generally use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) data types.
* If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

#### Tuple in Python
* *Ordered collection of elements*
* Immutable
* Uses circular brackets in syntax

#### Benefits of using Tuple
* Faster than lists
* Provide security over updation
* Unlike lists, can be used as key of dictionaries

e.g.
```python
my_tuple = (1, 3, 4, "hello")
print(my_tuple)

# find out the index of any element if present in Tuple
my_tuple.index(4)

# Count of an element in a tuple
my_tuple.count('hello')

# iterate through the elements of the tuple
for element in my_tuple:
    print(element)

# get first three elements
my_tuple[:3]

# define the start and end point to slice
my_tuple[3:5]

# count method on a slice
my_tuple[3:5].count(4)

# index method on a slice
my_tuple[1:4].index('B')

# tuples are immutable
my_tuple[2] = "bye"

del my_tuple[2]
```




