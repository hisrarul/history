## Pure Functions

* Pure Functions
    * Same output for same input, every time
    * Never mutates/access any variable outside the function

#### Jupyter
In the below code, we can see that if we run the function several number of times, the output would out to be different, since the function is mutating the parameter passed to it.

```python
%load_ext lab_black

iterable = [1, 2, 3, 4]

def impure_function(iterable):
    """Bad function that mutates the input parameter"""
    iterable.append("mutation")

impure_function(iterable)
iterable
```

Modify it
```python
iterable = [1, 2, 3, 4]
def actual_pure_function(iterable):
    """A function that avoids mutation of input parameters, works within the function"""
    new_list = iterable[:]   # modification is happending at new var new_list
    new_list.append("mutation")
    return new_list

iterable, actual_pure_fuction(iterable)
```

The function only works with what is being given to that function. Moreover, it does not mutate the input parameters.

#### Question 1
Which among the following are the reasons we avoid loops in functional programming.
* Mutation  of variable with iteration
* Loops do not use computation graph


