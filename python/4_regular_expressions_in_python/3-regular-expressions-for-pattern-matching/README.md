## Regular Expression

String containing a combination of normal characters and special metacharacters that describe patterns to find text or positions within a text
```r'st\d\s\w{3, 10}'```
Metacharacters represent types of characters (\d, \s, \w) or ideas ({3, 10}).

#### The re module
* Find all matches of a pattern:
re.findall(r"regex", string)

```python
import re
re.findall(r"#movies", "Love #movies! I had fun yesterday going to the #movies")
```

#### Split string at each match
* re.split(r"regex", string)
```python
re.split(r"!", "Nice place to eat! I'll come back! Excellent meat!")
```

#### Replace one or many matches with a string
* re.sub(r"regex", new, string)
```python
import re
re.sub(r"yellow", "nice", "I have a yellow car and a yellow house in a yellow neighborhood")
```

#### Supported Metacharacters
Metacharacter Meaning
* \d -> Digit
* \D -> Non-digit
* \w -> word
* \W -> Non-word
* \s -> Whitespace
* \S -> Non-Whitespace
```python
re.findall(r"User\d", "The winners are: User9, UserN, User8")
re.findall(r"User\D", "The winners are: User9, UserN, User8")
re.findall(r"User\w", "The winners are: User9, UserN, User8")
# find price
re.findall(r"\W\d", "This shirt is on sale, only $5 today!")
# Use space
re.findall(r"Data\sScience", "I enjoy learning Data Science")
# Non-space
re.sub(r"ice\Scream", "ice creame", "I really like ice-cream")
```

#### Exercise: Are they bots?
The company that you are working for asked you to perform a sentiment analysis using a dataset with tweets. First of all, you need to do some cleaning and extract some information.
While printing out some text, you realize that some tweets contain user mentions. Some of these mentions follow a very strange pattern. A few examples that you notice: @robot3!, @robot5& and @robot7#

To analyze if those users are bots, you will do a proof of concept with one tweet and extract them using the .findall() method.

Write a regex that matches the user mentions that starts with @ and follows the pattern, e.g. @robot3!.
```python
sentiment_analysis="@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%"
# Import the re module
import re

# Write the regex
regex = r"@robot\d\W"

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))
```

#### Repetitions
```python
# Quantifiers: A metacharacters that tells the regex engine how many times to match a character immediately to its left

import re
password = "password1234"

re.search(r"\w{8}\d{4}", password)
```

#### Quantifiers
* Once or more: `+`
* Zero times or more: `?`
* Zero or once: `*`
* n times at least, m times at most: `{n, m}`
* Immediately to the left
    * r"apple+": `+` applies to e and not to apple
```python
text = "Date of start: 4-3. Date of registration: 10-04."
re.findall(r"\d+-\d+", text)

my_string = "The concert was amazing! @ameli!a @joh&&n @mary90"
re.findall(r"\w+\W*\w+", my_string)

text = "The color of this image is amazing. However, the colour blue could be brighter."
re.findall(r"colou?r", text)

phone_number = "John: 1-966-847-3131 Michelle: 54-908-42-42424"
re.findall(r"\d{1,2}-\d{3}-\d{2,3}-\d{4,}", phone_number)
```

#### Looking for patterns
* Two different operations to find a match
    * re.search(r"regex", string)
    * re.match(r"regex", string)
```python
# this will match
re.search(r"\d{4}", "4506 people attend the show")
re.search(r"\d+", "Yesterday, I saw 3 shows")

# this will not match because first character didn't match
re.match(r"\d{4}", "4506 people attend the show")
re.match(r"\d+", "Yesterday, I saw 3 shows")
```

#### Special characters
* Match any character (except newline): `.`
* Start of the string: `^`
* End of the string: `$`
* Escape special characters: `/`
```python
my_links = "Just check out this link: www.example.com. It was amazing photos!"
re.findall(r"www.+com", my_links)

my_string = "the 80s music was much better that was the 90s"
re.findall(r"the\s\d+s", my_string)

# start of the string
re.findall(r"^the\s\d+s", my_string)

# end of the string
re.findall(r"the\s\d+s$", my_string)

my_string = "I love the music of Mr. Go. However, the sound was too loud."
print(re.split(r"\..\s", my_string))
```

#### OR operator
* Character: `|`
* Set of character: `[ ]`
    * `^` transforms the expression to negative
```python
my_string = "Elephants are the world's largest land animal! I would love to see an elephant one day"
re.findall(r"Elephant|elephant", my_string)

# set of character
my_string = "Yesterday, I spent my afternoon with my friends: MarryJohn2 Clarry3"
re.findall(r"[a-zA-Z]+\d", my_string)

my_string = "My&name&is#John Smith. I%live$in#London."
re.sub(r"[#$%&]", " ", my_string)

my_links = "Bad website: www.99.com. Favorite site: www.hola.com"
re.findall(r"www[^0-9]+com", my_links)
```

#### Greedy vs non-greedy matching
* Two types of matching methods:
    * Greedy
    * Non-greedy or lazy
* Standard quantifiers are greedy by default: `*`, `+`, `?`, `{num, num}`

#### Greedy matching
* Greedy: match as many characters as possible
* Return the longest match
* Backtracks when too many character matched
* Gives up characters one at a time
```python
import re
re.match(r"\d+", "12345bcada")

import re
re.match(r".*hello", "xhelloxxxxx")
```

#### Non-greedy matching
* Lazy: match as few characters as needed
* Returns the shortest match
* Append `?` to greedy quantifiers
* Backtracks when too many characters matched
* Expands characters one at a time
```python
import re
re.match(r"\d+?", "12345bcada")
```

#### Exercise: Match and split
Some of the tweets in your dataset were downloaded incorrectly. Instead of having spaces to separate words, they have strange characters. You decide to use regular expressions to handle this situation. You print some of these tweets to understand which pattern you need to match.

You notice that the sentences are always separated by a special character, followed by a number, the word break, and after that, another special character, e.g &4break!. The words are always separated by a special character, the word new, and a normal random character, e.g #newH.
```python
sentiment_analysis="He#newHis%newTin love with$newPscrappy. #8break%He is&newYmissing him@newLalready"
# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)

# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, " ", sentiment_sub)
print(sentiment_final)
```

#### Exercise

```python
sentiment_analysis = 'The health system is more stressed than I have ever known Dr Phillip Lee, a GP and former. \n More with @StephenNolan at 10pm. Follow more at https://www.google.com'

# Import re module
import re

for tweet in sentiment_analysis.split(sep="\n"):
	# Write regex to match http links and print out result
	print(re.findall(r"https?://www\.\w+\.\w+", tweet))

	# Write regex to match user mentions and print out result
	print(re.findall(r"@\w+\d?", tweet))
```

#### Exercise: Getting tokens
Your next step is to tokenize the text of your tweets. Tokenization is the process of breaking a string into lexical units or, in simpler terms, words. But first, you need to remove hashtags so they do not cloud your process. You realize that hashtags start with a # symbol and contain letters and numbers but never whitespace. After that, you plan to split the text at whitespace matches to get the tokens.

You bring your list of quantifiers to help you: * zero or more times, + once or more, ? zero or once, {n, m} minimum n, maximum m.
```python
sentiment_analysis="ITS NOT ENOUGH TO SAY THAT IMISS U #MissYou #SoMuch #Friendship #Forever"
# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)

# Get tokens by splitting text
print(re.split(r"\s+", no_hashtag))
```

#### Exercise: Give me your email
A colleague has asked for your help! When a user signs up on the company website, they must provide a valid email address.
The company puts some rules in place to verify that the given email address is valid:

The first part can contain:
Upper A-Z or lowercase letters a-z
Numbers
Characters: !, #, %, &, *, $, .
Must have @
Domain:
Can contain any word characters
But only .com ending is allowed
The project consist of writing a script that checks if the email address follow the correct pattern. Your colleague gave you a list of email addresses as examples to test.

The list emails as well as the re module are loaded in your session. You can use print(emails) to view the emails in the IPython Shell.
```python
emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']

# Write a regex to match a valid email address
regex = r"[a-zA-Z0-9!#%&*$.]+@\w+\.com"

for example in emails:
  	# Match the regex to the string
    if re.findall(regex, example):
        # Complete the format method to print out the result
      	print("The email {} is a valid email".format(example))
    else:
      	print("The email {} is invalid".format(example)) 
```

#### Exercise: Invalid password
The second part of the website project is to write a script that validates the password entered by the user. The company also puts some rules in order to verify valid passwords:

It can contain lowercase a-z and uppercase letters A-Z
It can contain numbers
It can contain the symbols: *, #, $, %, !, &, .
It must be at least 8 characters long but not more than 20
Your colleague also gave you a list of passwords as examples to test.

The list passwords and the module re are loaded in your session. You can use print(passwords) to view them in the IPython Shell.
```python
passwords = ['Apple34!rose', 'My87hou#4$', 'abc123']
# Write a regex to check if the password is valid
regex = r"[a-zA-Z0-9*#$%!&.]{8,20}"

for example in passwords:
  	# Scan the strings to find a match
    if re.findall(regex, example):
        # Complete the format method to print out the result
      	print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
      	print("The password {pass_example} is invalid".format(pass_example=example))
```

#### Exercise: Understanding the difference
You need to keep working and cleaning your tweets dataset. You realize that there are some HTML tags present. You need to remove them but keep the inside content as they are useful for analysis.

Let's take a look at this sentence containing an HTML tag:

I want to see that <strong>amazing show</strong> again!.

You know that to get the HTML tag you need to match anything that sits inside angle brackets < >. But the biggest problem is that the closing tag has the same structure. If you match too much, you will end up removing key information. So you need to decide whether to use a greedy or a lazy quantifier.

The string is already loaded as string to your session.
```python
string = "I want to see that <strong>amazing show</strong> again!"
# Import re
import re

# Write a regex to eliminate tags
string_notags = re.sub(r"<.+?>", "", string)

# Print out the result
print(string_notags)
```

#### Exercise: Lazy approach
You have done some cleaning in your dataset but you are worried that there are sentences encased in parentheses that may cloud your analysis.

Again, a greedy or a lazy quantifier may lead to different results.

For example, if you want to extract a word starting with a and ending with e in the string I like apple pie, you may think that applying the greedy regex a.+e will return apple. However, your match will be apple pie. A way to overcome this is to make it lazy by using ? which will return apple.

The re module and the variable sentiment_analysis are already loaded in your session.
```python
sentiment_analysis = "Put vacation photos online (They were so cute) a few yrs ago. PC crashed, and now I forget the name of the site (I'm crying)."
# Write a greedy regex expression to match 
sentences_found_greedy = re.findall(r"\(.*\)", sentiment_analysis)

# Print out the result
print(sentences_found_greedy)

#### Correct solution ####
# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.*?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)
```