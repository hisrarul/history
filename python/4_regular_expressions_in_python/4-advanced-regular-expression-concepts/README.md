#### Grouping and Capturing
* Quantifier immediately to the left
    * `r"apple+"`:`+` applies to e and not to apple 

```python
import re
text = "Clary has 2 friends who she spends a lot time with. Susan has 3 brothers while John has 4 sisters."

re.findall(r"[A-Za-z]+\s\w+\s\d+\s\w+", text)

# Use parentheses to group and capture characters together
re.findall(r"([A-Za-z]+)\s\w+\s\d+\s\w+", text)

# 3 groups
re.findall(r"([A-Za-z]+)\s\w+\s(\d+)\s(\w+)", text)

# organize the data
pets = re.findall(r"([A-Za-z]+)\s\w+\s(\d+)\s(\w+)", "Clary has 2 dogs but John has 3 cats")
pets[0][0]

# Apply quantifier to the entire group
re.search(r"(\d[A-Za-z])+", "My user name is 3e4r5fg")

# Capture a repeated group (\d+) vs repeat a capturing group (\d)+
my_string = "My lucky numbers are 8755 and 33"
re.findall(r"(\d)+", my_string)

re.findall(r"(\d+)", my_string)
```

#### Exercise: Try another name
You are still working on your Twitter sentiment analysis. You analyze now some things that caught your attention. You noticed that there are email addresses inserted in some tweets. Now, you are curious to find out which is the most common name.

You want to extract the first part of the email. E.g. if you have the email marysmith90@gmail.com, you are only interested in marysmith90.
You need to match the entire expression. So you make sure to extract only names present in emails. Also, you are only interested in names containing upper (e.g. A,B, Z) or lowercase letters (e.g. a, d, z) and numbers.
```python
sentiment_analysis = ['Just got ur newsletter, those fares really are unbelievable. Write to statravelAU@gmail.com or statravelpo@hotmail.com. They have amazing prices', 'I should have paid more attention when we covered photoshop in my webpage design class in undergrad. Contact me Hollywoodheat34@msn.net.', 'hey missed ya at the meeting. Read your email! msdrama098@hotmail.com']

# Capture only name from email address
# Write a regex that matches email
regex_email = r"([A-Za-z0-9]+)@\w+\S\w+"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)

    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(email_matched))
```

#### Exercise: Flying home
Your boss assigned you to a small project. They are performing an analysis of the travels people made to attend business meetings. You are given a dataset with only the email subjects for each of the people traveling.

You learn that the text followed a pattern. Here is an example:

Here you have your boarding pass LA4214 AER-CDB 06NOV.

You need to extract the information about the flight:

The two letters indicate the airline (e.g LA),
The 4 numbers are the flight number (e.g. 4214).
The three letters correspond to the departure (e.g AER),
The destination (CDB),
The date (06NOV) of the flight.
All letters are always uppercase.

```python

flight = 'Subject: You are now ready to fly. Here you have your boarding pass IB3723 AMS-MAD 06OCT'

# Import re
import re

# Write regex to capture information of the flight
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

# Find all matches of the flight information
flight_matches = re.findall(regex, flight)
    
#Print the matches
print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))
```

#### Alternation and non-capturing groups
* Pipe `|`
```python
# Vertical bar or pipe
my_string = "I want to have a pet. But I don't know if I want a cat, a dog or a bird."
re.findall(r"cat|dog|bird", my_string)

# wrong output bcz OR operator works everything on left and right i.e. dog
my_string = "I want to have a pet. But I don't know if I want 2 cat, 1 dog or a bird."
re.findall(r"\d+\scat|dog|bird", my_string)
```

#### Alternation
* Use groups to choose between optional patterns
```python
my_string = "I want to have a pet. But I don't know if I want 2 cat, 1 dog or a bird."
re.findall(r"\d+\s(cat|dog|bird)", my_string)

# capture two group, number and animal
re.findall(r"(\d+)\s(cat|dog|bird)", my_string)
```

#### Non-capturing groups
* Match but not capture a group
```python
my_string = "John Smith: 34-34-34-042-980, Rebeca Smith: 10-10-10-434-425"
re.findall(r"(?:\d{2}-){3}(\d{3}-\d{3})", my_string)
```

* Use non-capturing groups for alternation
```python
my_date = "Today is 23rd May 2019. Tomorrow is 24th May 19"
re.findall(r"(\d+)(?:th|rd)", my_date)
```

#### Exercise: Love it!
You are still working on the Twitter sentiment analysis project. First, you want to identify positive tweets about movies and concerts.

You plan to find all the sentences that contain the words love, like, or enjoy and capture that word. You will limit the tweets by focusing on those that contain the words movie or concert by keeping the word in another group. You will also save the movie or concert name.

For example, if you have the sentence: I love the movie Avengers. You match and capture love. You need to match and capture movie. Afterwards, you match and capture anything until the dot.

```python
sentiment_analysis = ['I totally love the concert The Book of Souls World Tour. It kinda amazing!', 'I enjoy the movie Wreck-It Ralph. I watched with my boyfriend.', "I still like the movie Wish Upon a Star. Too bad Disney doesn't show it anymore."]

# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)
    
    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))
```

#### Backreferences
```python
text = "Python 3.0 was released on 12-03-2008."
information = re.search('(\d{1,2})-(\d{1,2})-(\d{4})', text)
information.group(3)
information.group(0)
```

#### Named groups
* Give a name to groups `(?P<name>regex)`
```python
text = "Austin, 78701"
cities = re.search(r"(?P<city>[A-Za-z]+).*?(?P<zipcode>\d{5})", text)

# print the group city
cities.group("city")

# print the group zipcode
cities.group("zipcode")
```

* Using numbered capturing groups to reference back
```python
# Multiple occurence
sentence = "I wish wish wish you a happy happy birthday!"
re.findall(r"(\w+)\s\1", sentence)

# replace the multiple occurence of happy and wishd
re.sub(r"(\w+)\s\1", r"\1", sentence)
```

* Using named capturing groups to reference book `(?<name>regex)`
```python
sentence = "Your new code number is 23434. Please, enter 23434 to open the door"
re.findall(r"(?P<code>\d{5}).*?(?P=code)", sentence)

sentence = "This app is not working! It's repeating the last word word."
re.sub(r"(?P<word>\w+)\s(?P=word)", r"\g<word>", sentence)
```

#### Exercise: Parsing PDF files
You now need to work on another small project you have been delaying. Your company gave you some PDF files of signed contracts. The goal of the project is to create a database with the information you parse from them. Three of these columns should correspond to the day, month, and year when the contract was signed.
The dates appear as Signed on 05/24/2016 (05 indicating the month, 24 the day). You decide to use capturing groups to extract this information. Also, you would like to retrieve that information so you can store it separately in different variables.

You decide to do a proof of concept.

```python
contract = "Provider will invoice Client for Services performed within 30 days of performance.  Client will pay Provider as set forth in each Statement of Work within 30 days of receipt and acceptance of such invoice. It is understood that payments to Provider for services rendered shall be made in full as agreed, without any deductions for taxes of any kind whatsoever, in conformity with Provider’s status as an independent contractor. Signed on 03/25/2001."

# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign to each key the corresponding match
signature = {
	"day": dates.group(2),
	"month": dates.group(1),
	"year": dates.group(3)
}
# Complete the format method to print-out
print("Our first contract is dated back to {data[year]}. Particularly, the day {data[day]} of the month {data[month]}.".format(data=signature))
```

#### Exercise: Close the tag, please!
In the meantime, you are working on one of your other projects. The company is going to develop a new product. It will help developers automatically check the code they are writing. You need to write a short script for checking that every HTML tag that is open has its proper closure.

You have an example of a string containing HTML tags:

<title>The Data Science Company</title>

You learn that an opening HTML tag is always at the beginning of the string. It appears inside <>. A closing tag also appears inside <>, but it is preceded by /.

You also remember that capturing groups can be referenced using numbers, e.g \4.
```python
html_tags = ['<body>Welcome to our course! It would be an awesome experience</body>', '<article>To be a data scientist, you need to have knowledge in statistics and mathematics</article>', '<nav>About me Links Contact me!']

for string in html_tags:
    # Complete the regex and find if it matches a closed HTML tags
    match_tag =  re.match(r"<(\w+)>.*?</\1>", string)
 
    if match_tag:
        # If it matches print the first group capture
        print("Your tag {} is closed".format(match_tag.group(1))) 
    else:
        # If it doesn't match capture only the tag 
        notmatch_tag = re.match(r"<(\w+)>", string)
        # Print the first group capture
        print("Close your {} tag!".format(notmatch_tag.group(1)))
```

#### Exercise: Reeepeated characters
Back to your sentiment analysis! Your next task is to replace elongated words that appear in the tweets. We define an elongated word as a word that contains a repeating character twice or more times. e.g. "Awesoooome".

Replacing those words is very important since a classifier will treat them as a different term from the source words lowering their frequency.

To find them, you will use capturing groups and reference them back using numbers. E.g \4.

If you want to find a match for Awesoooome. You first need to capture Awes. Then, match o and reference the same character back, and then, me.
```python
sentiment_analysis=['@marykatherine_q i know! I heard it this morning and wondered the same thing. Moscooooooow is so behind the times', 'Staying at a friends house...neighborrrrrrrs are so loud-having a party', 'Just woke up an already have read some e-mail']

# Complete the regex to match an elongated word
regex_elongated = r"\w*(\w)\1\w*"

for tweet in sentiment_analysis:
	# Find if there is a match in each tweet 
	match_elongated = re.search(regex_elongated, tweet)
    
	if match_elongated:
		# Assign the captured group zero 
		elongated_word = match_elongated.group(0)
        
		# Complete the format method to print the word
		print("Elongated word found: {word}".format(word=elongated_word))
	else:
		print("No elongated word found")     	
```

#### Looking around
* Allow us to confirm that sub-pattern is ahead or behind main pattern

### Look-ahead
* Non-capturing group
* Checks that the first part of the expression is followed or not by the lookahead expression
* Return only the first part of the expression

Example: the white cat `sat` on the chair

`sat` is the look ahead

positive `(?=sat)` negative `(?!run)`
```python
my_text = "tweets.txt transferred, mypass.txt transferred, keywords.txt error"

re.findall(r"\w+\.txt", my_text)

# look for the words followed by transferred - positive look ahead
re.findall(r"\w+\.txt(?=\stransferred)", my_text)

# negative look ahead
re.findall(r"\w+\.txt(?!\stransferred)", my_text)

```

#### Look-behind
* Non-capturing group
* Get all the matches that are preceded or not by a specific pattern.
* Return pattern after look-behind expression

Example: 
Look the word before cat `the white cat sat on the chair`

positive `(?<=white)` negative `(?<!brown>)`
```python
my_text = "Member: Angus Young, Member: Chris Slade, Past: Malcolm Young, Past: Cliff Williams."

# look behind and check if Member:\s exist before \w+\s\w+
re.findall(r"(?<=Member:\s)\w+\s\w+", my_text)

# not
my_text = "My white cat sat at the table. However, my brown dog was lying on the couch."
re.findall(r"(?<!brown\s)(cat|dog)", my_text)
```

#### Exercise: Surrounding words
Now, you want to perform some visualizations with your sentiment_analysis dataset. You are interested in the words surrounding python. You want to count how many times a specific words appears right before and after it.

Positive lookahead (?=) makes sure that first part of the expression is followed by the lookahead expression. Positive lookbehind (?<=) returns all matches that are preceded by the specified pattern.

```python
sentiment_analysis = "You need excellent python skills to be a data scientist. Must be! Excellent python"

## Get all the word that are followed by the word python in sentiment_analysis

# Positive lookbehind
look_behind = re.findall(r"(?<=[pP]ython\s)\w+", sentiment_analysis)

# Print out
print(look_behind)
```

#### Filtering phone numbers
Now, you need to write a script for a cell-phone searcher. It should scan a list of phone numbers and return those that meet certain characteristics.

The phone numbers in the list have the structure:

Optional area code: 3 numbers
Prefix: 4 numbers
Line number: 6 numbers
Optional extension: 2 numbers
E.g. 654-8764-439434-01.

You decide to use .findall() and the non-capturing group's negative lookahead (?!) and negative lookbehind (?<!).

1. Get all cell phones numbers that are not preceded by the optional area code.
```python
cellphones = ['4564-646464-01', '345-5785-544245', '6476-579052-01']

for phone in cellphones:
	# Get all phone numbers not preceded by area code
	number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}", phone)
	print(number)
```

2. Get all the cell phones numbers that are not followed by the optional extension.
```python
for phone in cellphones:
	# Get all phone numbers not followed by optional extension
	number = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
	print(number)
```
