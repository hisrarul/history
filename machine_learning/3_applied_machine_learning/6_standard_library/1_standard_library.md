## Standard Library

#### Math
```python
import math

# round the number to nearest above
math.ceil(20.222)       # o/p: 21

# round the number to nearest below
math.floor(20.222)      # o/p: 20

# factorial of a number
math.factorial(10)

# greatest common divisor of the integers a and b
math.gcd(20, 25)
```

#### Random
```python
import random

# select a random element from a list
random.choice(['apple', 'pear', 'banana'])

# select 10 different numbers within a range of numbers
random.sample(range(10,50), 10)

# select a random float number
random.random()

# select a random float number within a range
random.uniform(0, 2)

# random integer chosen from range(6)
random.randrange(3, 6)

random.randint(1, 10)
```

#### DATE TIME
```python
# dates are easily constructed and formatted
from datetime import date

# get the current date
TODAY = date.today()
print("Date: ", TODAY)

# format date
print("Formatted date: ", TODAY.strftime("%m-%d-%y"))

# format date
print("Formatted date: ", TODAY.strftime("%d %b %Y"))

# format date
print("Formatted date: ", TODAY.strftime("%A on the %d day of %B"))

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = TODAY - birthday
print("Age in days:", age.days)
```


#### Operating System
* The os module provides dozens of functions for interacting with the operating system.

```python
import os

# return the current working directory
print("Get current working directory: ", os.getcwd())

# list contents of a directory
print("Listing existing directories: ")
os.listdir()


# run the command mkdir in the system shell
print("Make new directory")
os.system('mkdir today')

# check if new directory got created
print("Listing existing directories: ")
os.listdir()

# change current working directory
os.chdir('today/')

print("Get current working directory: ", os.getcwd())
```

#### User defined libraries in Python
* Operator ---> Arithmetic.py, Logical.py, Comparison.py
* Arithmetic.py ---> def addition(), def subtraction(), def division()
* Logical.py ---> def and(), def or(), def not()


#### How do we import a function
* from Operator import Arithmetic ---> Arithmetic.addition(3,5)
* from Operator.Arithmetic import addition ---> addition(3,5)

* dir(Arithmetic): Check what are the things that belong to this arithmetic module.


#### Advantage of using module
* It provides a means of identifying the error easily.
* It provides a means of dividing up tasks.
* Provides a means of reuse of program code.
* It provides a means of testing individual parts of the program.





