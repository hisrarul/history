## Decorator

* Higher order function
    * A wrapper over a pre existing functino
    * Extends the basic function's ability
    * Used to generalise over large number of functions

#### Decorator Syntax: Extending a Function
```python
def decorator_function(existing_function):    #existing_function
    wrapper_function(params):    # parameters
        # do something before a function
        existing_function(params)  # existing_function and params
        # do something after a function
    return wrapper_function
```

#### Decorator Use Case
* Used with scalable framework: Dask, PySpark
* Extensively used with model deployment


#### Jupyter notebook
```python
%load_ext lab_black
```

Syntax implementation
```python
def decorator_function(existing_function):
    def wrapper_function():
        print("Doing something before existing function")
        existing_function()
        print("Doing something after existing function")
    return wrapper_function
```

#### Decorating a simple function
Method 1
This method is used when we are trying to decorate a predefined function. This does not change the existing function.
```python
def speak():
    print("*******Python is pretty easy to learn******)

resultant_function = decorator_function(speak)
resultant_function()
```

Method 2
Decorating and calling the predefined function on the go. This does not change the existing function.

```python
decorator_function(speak)()
```

Method 3
Decorating the definition of a function. This adds to the existing function
```python
@decorator_function
def speak():
    print("*******Python is pretty easy to learn*******")
    return

speak()
```

#### Decorating functions with parameters
Note the arguments in wrapper function
```python
def greet(name):
    print("Hey {}, Python is easy to learn".format(name))

def decorator_function(existing_function):
    def wrapper_function(*params):
        print("Doing something before existing function")
        existing_function(*params)
        print("Doing something after existing function")
    return wrapper_function
```

Method 1
pre-existing function with parameters

```python
resultant_function = decorator_function(greet)
resultant_function("Aishwarya")
```

Method 2
Decorating and calling function on the go.
Syntax:
decorator_name(function_to_be_decorated)(parameters_expected)

```python
decorator_function(greet)("Aishwarya")
```

Method 3
Decorating the definition of a function with parameters
```python
def decorator_function(existing_function):
    def wrapper_function(*params):
        print("Doing something before existing function")
        existing_function(*params)


# Method 1
@decorator_function
def greet(name):
    print("Hey {}, Python is easy to learn".format(name))

greet("Aishwarya")
```

#### Question: What will be output of code below
```python
def f(x):
    def f1(a, b):
        print("hello")
        if b == 0:
            print("NO")
            return
        return f(a, b)
    return f1

@f
def f(a, b):
    return a % b

f(4, 0)
```
Answer: hello, NO
