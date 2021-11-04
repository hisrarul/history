## Positional Formatting

#### What is string formatting?
* String interpolation
* Insert a custom string or variable in predefined text.
```python
custom_string = "String formatting"
print(f"{custom_string} is a powerful technique")

#### Placeholder replace by value
* Using str.format()
```python
print("Machine learning provides {} the ability to learn {}".format("systems","automatically"))

# Use variables for both the initial string and the values passed into the method
```python
my_string = "{} rely on {} datasets"
method = "Supervised algorithms"
condition = "labeled"

print(my_string.format(method, condition))
```

#### Reordering values
* Include an index number into the placeholders to reorder values
```python
print("{} has a friend called {} and a sister called {}".format("Betty","Linda","Daisy"))
print("{2} has a friend called {0} and a sister called {1}".format("Betty","Linda","Daisy"))
```

#### Name placeholders
Specify a name for the placeholders
```python
tool="Unsupervised algorithms"
goal="patterns"
print("{title} try to find {aim} in the dataset".format(title=tool, aim=goal))

my_methods = {"tool": "Unsupervised algorithms", "goal": "patterns"}
print('{data[tool]} try to find {data[goal]} in the dataset'.format(data=my_methods))
```

#### Format specifier
* Specify data type to be used: {index:specifier}
```python
print("Only {0:f}% of the {1} produced worldwide is {2}!".format(0.5155675,"data","analyzed"))
```

#### Formatting datetime
```python
from datetime import datetime
print(datetime.now())
print("Today's date is {:%Y-%m-%d %H:%M}".format(datetime.now()))
```

#### Formatted string literal (f-string)
* Minimal syntax
* f"literal string{expression}"
```python
way = "code"
method = "learning Python faster"
print(f"Practicing how to {way} is the best method for {method}")
```

#### Type conversion
* !s (string version)
* !r (string containing a printable representation, i.e  with quotes)
* !a (some as !r but escape the non-ASCII characters)
```python
name = "Python"
print(f"Python is called {name!r} due to a comedy series")
```

#### Format specifiers
* e (scientific notation, e.g. 5 10^3)
* d (digit, e.g. 4)
* f (float, e.g. 4.535353)
```python
number = 90.41890417471841
print(f"In the last 2 years, {number:.2f}% of the data was produced worldwide!")
```python
from datetime import datetime
my_today = datetime.now()
print(f"Today's date is {my_today:%B %d, %Y}")
```

#### Index Lookup
```python
family = {"dad": "John", "siblings": "Peter"}
print("Is your dad called {family[dad]}?".format(family=family))

# incorrect
print(f"Is your dad called {family[dad]}?")

# correct
print(f"Is your dad called {family['dad']}?")
```

#### Escape characters
```python
# John in double quotes
print("My dad is called \"John\"")

# f-string expression part cannot include a backslash
print(f"Is your dad called {family['dad']}?")
```

#### Inline operations
* Evaluate expressions and call functions inline
```python
my_multiplier = 7
my_number = 4
print(f'{my_number} multiplied by {my_multiplier} is {my_number * my_multiplier}')
```

#### Calling functions
```python
def my_function(a, b):
    return a+b

print(f"If you sum up 10 and 20 the result is {my_function(10, 20)}")
```

#### Template strings
* Simpler syntax
* Slower than f-strings
* Limited: don't allow format specifiers
* Good when working with externally formatted strings
```python
from string import Template
my_string = Template('Data science has been called $identifier')
my_string.substitute(identifier="sexiest job of the 21st century")
```

#### Substitution
* Use many $identifier
* Use variables
```python
from string import Template
job = "Data science"
name = "sexiest job of the 21st century"
my_string = Template('$title has been called $description')
my_string.substitute(title=job, description=name)

# Use ${identifier} when valid characters follow identier
my_string = Template('I find Python very ${noun}ing but my sister has lost $noun')
my_string.substitute(noun="interest")

# Use $$ to escape the dollar sign
my_string = Template('I paid for the Python course only $$ $price, amazing!')
my_string.substitute(price="12.50")

# Raise error when placeholder is missing
favorite = dict(flavor="chocolate")
my_string = Template('I love $flavor $cake very much')
my_string.substitute(favorite)

# 
favorite = dict(flavor="chocolate")
my_string = Template('I love $flavor $cake very much')

try:
    my_string.substitute(favorite)
except KeyError:
    print("missing information")
```

#### Safe substitution
* Missing placeholders will appear in resulting string
```python
favorite = dict(flavor="chocolate")
my_string = Template('I love $flavor $cake very much')
my_string.safe_substitute(favorite)
```

#### Which should I use?
* str.format() : 
1. Good to start with. Concepts apply to f-strings.
2. Compatible with all versions of Python.
* f-strings:
1. Always advisable above all methods.
2. Not suitable if not working with modern versions of Python (3.6+).
* Template strings:
1. When working with external or user-provided strings

#### Exercise: What day is today?
It's lunch time and you are talking with some of your colleagues. They comment that they feel that every morning someone should send them a reminder of what day it is so they can check in the calendar what their assignments are for that day.

You want to help out and decide to write a small script that takes the date and time of the day so that every morning, a message is sent to your colleagues. You can use the module datetime along with named placeholders to achieve your goal.

The date should be expressed as Month day, year, e.g. April 16, 2019 and the time as hh:mm, e.g. 16:30.

You write down some specifiers to help you: %d(day), %B (monthname), %m (monthnumber), %Y(year), %H (hour) and %M(minutes)

You can use the IPython Shell to explore the module datetime.
```python
# Import datetime 
from datetime import datetime

# Assign date to get_date
get_date = datetime.now()

# Add named placeholders with format specifiers
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Use the format method replacing the placeholder with get_date
print(message.format(today=get_date))
```

#### Exercise: On time
Lastly, you want to rewrite an old real estate prediction project. At the time, you obtained historical information about house prices and used it to make a prediction on future values.

The date was in the datetime format: datetime.datetime(1990, 3, 17) but to print it out, you format it as 3-17-1990. You also remember that you defined a dictionary for each neighborhood. Now, you believe that you can handle both type of data better with f-strings.

Two dictionaries, east and west, both with the keys date and price, have already been loaded. You can use print() to view them in the IPython Shell.
```python
east="{'date': datetime.datetime(2007, 4, 20, 0, 0), 'price': 1232443}"
# Access values of date and price in east dictionary
print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")
```

#### Identifying prices
After you showed your report to your boss, he came up with the idea of offering courses to the company's users on some of the tools you studied. In order to make a pilot test, you will send an email offering a course about one of the tools, randomly chosen from your dataset. You also mention that the estimated fee needs to be paid on a monthly basis.

For writing the email, you will use Template strings. You remember that you need to be careful when you use the dollar sign since it is used for identifiers in this case.

For this example, the list tools contains the corresponding tool name, fee and payment type for the product offer. If you want to explore the variable, you can use print() to view it in the IPython Shell.

*Instruction
Complete the template string using $tool, $fee, and $pay as identifiers. Add the dollar sign before the $fee identifier and add the characters ly directly after the $pay identifier.
```python
tools=['Natural Language Toolkit', '20', 'month']
# Import template
from string import Template

# Select variables
our_tool = tools[0]
our_fee = tools[1]
our_pay = tools[2]

# Create template
course = Template("We are offering a 3-month beginner course on $tool just for $$ $fee ${pay}ly")

# Substitute identifiers with three variables
print(course.substitute(tool=our_tool, fee=our_fee, pay=our_pay))
```

#### Exercise: Playing safe
You are in charge of a new project! Your job is to start collecting information from the company's main application users. You will make an online quiz and ask your users to voluntarily answer two questions. However, it is not mandatory for the user to answer both. You will be handling user-provided strings so you decide to use the Template method to print the input information. This allows users to double-check their answers before submitting them.
```python
answers="{'answer1': 'I really like the app. But there are some features that can be improved'}"

# Import template
from string import Template

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use safe_substitute to replace identifiers
try:
    print(the_answers.safe_substitute(answers))
except KeyError:
    print("Missing information")
```

#### 