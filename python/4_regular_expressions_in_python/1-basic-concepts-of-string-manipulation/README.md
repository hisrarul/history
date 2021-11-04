## Basic concepts of string manipulation

#### String
```python
my_string = "This is a string"
my_string2 = 'This is also a string'

# length
len(my_string)

# Convert to string
str(123)

# Concatenation
my_string1 = "Awesome day"
my_string2 = "for biking"

print(my_string1+" "+my_string2)
```

#### Indexing
```python
# Bracket notation
my_string = "Awesome day"

print(my_string[3])
print(my_string[-1])

# Slicing
print(my_string[0:3])
print(my_string[:5])
print(my_string[5:])

# Stride
my_string = "Awesome day"
print(my_string[0:6:2])
```

#### Adjusting cases
```python

# Adjusting cases
my_string = "tHis Is a niCe StriNg"
print(my_string.lower())

# Converting to upper cases
print(my_string.upper())

# Captilize the first character
print(my_string.capitalize())
```

#### Splitting
```python
my_string = "This string will be split"
my_string.split(sep=" ", maxsplit=2)

# split into substring from left
my_string.rsplit(sep=" ", maxsplit=2)

# New line
my_string = "This string will be split\nin two"
print(my_string)

# Breaking at line boundary
my_string.splitlines()
```

#### Joining
```python
# Concatenate strings from list
my_list = ["this", "would", "be", "a", "string"]
print(" ".join(my_list))
```

#### Stripping
```python
# Stripping characters from left to right
my_string = " This string will be stripped\n"
my_string.strip()

# remove character from right end
my_string.rstrip()

# remove character from left end
my_string.lstrip()
```

#### Finding substrings
Search target string for a specified substring
* string.find(substring, start, end)
```python
my_string = "Where's Waldo?"
my_string.find("Waldo")

my_string.find("Wenda")
my_string.find("Waldo", 0, 6)
```

#### Index Function
Similar to .find(), search target string for a specified substring.
* string.index(substring, start, end)
```python
my_string = "Where's Waldo?"
my_string.index("Waldo")

# error
my_string.index("Wenda")

try:
    my_string.index("Wenda")
except ValueError:
    print("Not found")
```

#### Counting occurences
Return the number of occurences for a specified substring.
* string.count(substring, start, end)
```python
my_string = "How many fruits do you have in your fruit basket?"
my_string.count("fruit")

my_string.count("fruit", 0, 16)
```

#### Replacing substring
Replace occurences of substring with new substring.
* string.replace(old, new, count)
```python
my_string = "The red house is between the blue house and the old house"
print(my_string.replace("house", "car"))

# replace two occurence
print(my_string.replace("house", "car", 2))
```

#### Exercise: Palindromes
Next, you are committed to find any peculiarity in the words included in the movie review dataset. A palindrome is a sequence of characters which can be read the same backward as forward, for example: Madam or No lemon, no melon. You realize that there are some funny movie names that can have this characteristic. You want to make a list of all movie titles that are funny palindromes but you will start by analyzing one example.

In python, you can also specify steps by using a third index. If you don't specify the first or second index and the third one is negative, it will return the characters jumping and backwards.

The text of a movie review for one example has been already saved in the variable movie. You can use print(movie) to view the variable in the IPython Shell.
```python

movie = 'oh my God! desserts I stressed was an ugly movie'

# Get the word
movie_title = movie[11:30]

# Obtain the palindrome
palindrome = movie_title[::-1]

# Print the word if it's a palindrome
if movie_title == palindrome:
	print(movie_title)
```



