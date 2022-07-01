## Lambda Expression
* This function can have any number of arguments but only one expression, which evaluated and returned.
* Lambda functions are syntactically restricted to a single expression.
* It is more efficient than function when the function task is small.
* Do not use Lambda functions when task is complex.
* It works best when you have to call a function millions of times but the execution task is simple.

```python
# add 20 to the number that is passed as an argument

def add_20(a):
    return a + 20

add_20(5)

# lambda function
var = lambda a: a + 20

print('With argument value 5: ', var(5))
print('With argument value 10: ', var(10))
```

*A lambda function with two arguments*
```python
lambda_add = lambda a, b: a + b

print('The value of 5+3 = ', lambda_add(5,3))
print('The value of 7+2 = ', lambda_add(7,2))
```

#### Filter function
The filter() function in python takes in a function and a list as arguments. To filter out all the elements of a sequence for which the function returns True.

```python
def normal_even(x):
    if x%2 != 0:
        return True
    else:
        return False

# list
original_list = [5, 17, 32, 43, 12, 62, 237, 133, 78, 21]

# filter the odd numbers from the list
filtered_list = list(filter(normal_even, original_list))
print('The odd numbers are: ', filtered_list)


# filter the multiples of 5
filtered_list = list(filter(lambda x: (x%5 == 0), original_list))
print('The multiples of 5 are: ', filtered_list)


# filter the words starting with 'S'
original_list = ["Analytics", "Standard", "Super", "Data", "Science", "Vidhya"]
# filter the words starting with 'S'
filtered_list = list(filter(lambda x: (x[0] == 'S'), original_list))
print('The words starting with "S" are: ', filtered_list)
```


#### MAP Function
The map() function in Python takes in a function and a list as argument. The function is called with a lambda function and a list and a new list is returned which contains all the lambda modified items returns by that function for each item.

```python
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# double each number in the original list
mapped_list = list(map(lambda x: x*2, original_list))
print('New List: ', mapped_list)

# capatilize first letter of each word in the original list
original_list = ["Analytics", "Standard", "Super", "Data", "Science", "Vidhya"]
mapped_list = list(map(lambda x: x[0].upper() + x[1:], original_list))
print('New list: ', mapped_list)
```


#### Reduce Function
* The reduce() function in Python takes in a function and a list as argument. The function is called with a lambda function and a list and a new reduced result in returned. This performs a repetitive operation over the pairs of the list.
* The reduce function will always take two parameters.

```python
from functools import reduce
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# use reduce function to find the sum of number in the original list
sum_of_list = reduce((lambda x, y: x+y), original_list)
print('Sum of Numbers in the original list is : ', sum_of_list)


# use reduce function to find the largest number in the original list
original_list = [110, 53, 3, 424, 255, 16, 42, 256]
largest_number = reduce((lambda x, y: x if (x > y) else y), original_list)
print('Largest number in the original list is: ', largest_number)
```




