## String manipulation

```python
my_string = "Analytics Vidhya creating next generation data science eco-system"

# length of the string
len(my_string)

# access characters in a string
my_string[0]

# access characters with negative indexing
my_string[-1]

# string slicing
my_string[1:3]

my_string[10:-10]

# reverse a string
my_string[::-1]

# count a character
my_string.count('A')

my_string.count('a')
```

#### Find a substring in the string using find and index function
* If present it will return the starting index
* If not found, then it will return -1.

```python
my_string.find('next')

my_string.find('python')
```

*index*
* If present it will return the starting index
* If not found, then it will give error.

```python
my_string.index('next')

my_string.index('python')
```

#### Check whether if the start startswith or endswith a particular substring or not
```python
my_string

my_string.endswith('python')

my_string.startswith('python')
```


#### Convert the string

```python
# to upper case
my_string.upper()

# first character
my_string.capitalize()

# is lower
my_string.islower()

# is upper
my_string.isupper()

# is numeric
my_string.isnumeric()

# is alpha
my_string.isalpha()

# replace substrings
"java is easy to learn.".replace('java', 'python')

# split function
"python is easy to learn".split(' ')

"python is easy to learn".split('easy')

len("python is easy to learn".split(' '))

```



