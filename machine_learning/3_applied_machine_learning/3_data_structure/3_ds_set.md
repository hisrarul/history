## Set

* Unordered collection of elements
* No duplicate element
* Mutable or modifiable
* Set theory operations are possible


#### Set theory operations
* Intersection of two sets
    * set1.intersection(set2)
* Union of two sets
    * set1.union(set2)
* Subsets

```python
my_set = {'A', 'B', 'C', 'D', 1 'E', 2, 4, 2, 4}

# while printing automatically converted to order with unique values
my_set o/p: {1, 2, 4, 'A', 'B', 'C', 'D', 'E'}

# Add an element to the set
my_set.add('O')
```

#### Delete an element from the set
* Discard - It will not throw an error, if the element you want to remove is not present in the set.
* Remove - It will throw an error, if the element you want to remove is not present in the set.

```python
my_set = {1, 2, 4, 'A', 'B', 'C', 'D', 'E', 'O'}
my_set.discard('A')
my_set.remove('A')
```

#### Difference between two sets
* A-B

```python
# set 1
my_set = {1, 2, 4, 'B', 'C', 'D', 'E', 'O'}

# set 2
my_set_from_list = {1, 2, 'A', 'B'}

# difference of 2 sets
my_set.difference(my_set_from_list)

# it will not update the results, if not stored in a variable
my_set

# use the difference_update to store the results directly
my_set.difference_update(my_set_from_list)

# updated set
my_set
```

#### Intersection of two sets
```python
# set 1
my_set = {1, 2, 4, 'B', 'C', 'D', 'E', 'O'}

# set 2
my_set_from_list = {1, 2, 'A', 'B'}

# intersection of 2 sets
my_set.intersection(my_set_from_list)

# it will not update the results, if not stored in a variable
my_set

# to update directly, use intersection_update
my_set.intersection_update(my_set_from_list)

# updated set
my_set
```

#### Other operations on set
* is_disjoint
* is_subset
* is_superset
* union

```python
# define 3 random sets
sample_set_1 = {'A', 'B', 'C', 'E', 'F'}
sample_set_2 = {'A', 'D', 'E'}
sample_set_3 = {'S', 'T', 'U'}

# check if 2 sets are disjoint sets
sample_set_1.isdisjoint(sample_set_2)

sample_set_1.isdisjoint(sample_set_3)

# check if one set is subset of another set
sample_set_2.issubset(sample_set_1)

# check if one set is superset of another
sample_set_1.issuperset(sample_set_2)

# union of two sets
sample_set_1.union(sample_set_3)

# update a set with new values, it will add the values which are not present in the original set
sample_set_1.udpate({'C', 'D', 'E', 'R', 'Z'})

# Iterate the set
for element in sample_set_1:
    print(element)
```




