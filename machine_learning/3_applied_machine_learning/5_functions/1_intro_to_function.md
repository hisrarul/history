## Functions

#### Variable length arguments
* Sometimes, we need more flexibility while defining functions like we don't know in advance the fixed number of arguments.

* Python allows us to make function calls with variable length arguments.

* In the argument use *(*)* astrick sign before the argument.

```python
# define a function
def my_function(*args):         # args is tuple data structure
    for i in args:
        print(i)


my_function(1, 2, 3, 4)

my_function(1, 2, 3, 4)
```

*If you have unknown number of keyword arguments, then you can use double asterick (**)*
```python
def my_keyword_arguments(**kwargs):
    for key, value in kwargs.items():   # kwargs is dict data structure
        print(key, value)

my_keyword_arguments(a=1, b=2, c=3)
```

#### Scope of Variables: Local and Global Variables
* "Score of Variable" means that part of program where we can access particular variable
* "Local Variable" are those which are defined inside the function and can be only accessed inside that particular function.
* "Global Variable" are defined outside the function and can be accessed throughout the program.

```python
# define a global variable
name = "variable outside function"

# define a function
def my_function():
    # access the variable outside the function
    return name

print(my_function())

print(name)
```

*Inside variable*
```python
# define a global variable
name = "variable outside function"

# define a function
def my_function():
    # tell the function which variables are global
    global name
    name = "variable inside function"
    return name

print(my_function())

print(name)
```
