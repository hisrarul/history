## Assertions

#### Definition
Dictionary - A confident and forceful statement of fact or belief

Code - Enforcing the assumptions documented

#### Assertions: Example
```python
def greatest_of_two(value1, value2):
    """Returns whichever value is greater, assuming they are not equal

    params:
    value1(float): First number for comparison
    value2(float): Second number for comparison

    returns(float): greatest among two values
    """
    if value1 > value2:
        return value1
    else:
        return value2
```
In this example, according to the docstring these numbers are float and return whichever number is greater but there is an assumption that input value used should not be equal.

* Enforce the assumption in above code
```python
def greatest_of_two(value1, value2):
    """Returns whichever value is greater, assuming they are not equal

    params:
    value1(float): First number for comparison
    value2(float): Second number for comparison

    returns(float): greatest among two values
    """
    assert type(value1) in (int, float) and type(value2) in (int, float), "unexpected input values, should be int or float"
    # if values not equal, do nothing: Else return prompt
    assert value1 != value2, "The two values must not be equal"
    if value1 > value2:
        return value1
    else:
        return value2
```

`greatest_of_two(5, 5)` will raise the assertion error.

#### Assertions for defensive programming
* Halts execution on first apprerance of unexpected condition
* Generally used right before chunk of logical code
* Can be used to check input
* Can be used to check output, avoids propagation of bad values
* Can easily detect source of bugs

#### Assertions as return checker
```python
def extending_list(list1, list2):
    """
    Takes list1 and extends it with element of list2
    Such that:
    length(result_list) = len(list1) + len(list2)

    params:
    list1(list): the original list to be extended
    list2(list): list of elements to be added to original list

    returns(list): result of extention of list1 and list2
    """
    assert (
        type(list1) == list and type(list2) == list
    ), "Both inputs must be of type list only"
    new_list = list1[:]
    new_list.append(list2)  #try with extend too
    assert len(new_list) == len(list1) + len(list2), "The length of the resulting list is not as intended"
    return new_list
```

Note: Assertions can only signal unexpected conditions, not circumvent it.
