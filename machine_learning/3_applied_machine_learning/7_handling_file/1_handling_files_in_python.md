## File Handling

#### Text files
* .txt

#### File Access Modes
* `Read Only ('r')`: It opens the text file for reading. If the file does not exist, raises I/O error.
* `Read and Write ('r+')`: It opens the file for reading and writing. Raises I/O error if the file does not exist.
* `Write Only ('w')`: It opens the file for writing. For existing file, the data over-written. Creates the file if the file not exist.
* `Write and Read ('w+')`: It opens the file for reading and writing. For existing file, data is truncated and over-written.
* `Append Only ('a')`: It opens the file for writing. The file is created if it does not exist. The data written will be inserted at the end, after the existing data.
* `Append and Read ('a+')`: It opens the file for reading and writing. The file is created if it does not exist. The data being written will be inserted at the end, after the existing data.


#### Reading text files
```python
# open the file in read only mode
text_file = open("dataset/file_1.txt", "r")

# read the file and store the text in a variable
complete_text = text_file.read()
complete_text

# read the file again
complete_text = text_file.read()

complete_text       # it will not give any output bcz the pointer has move from top to bottom of the file and to avoid it, we can use close()

text_file.close()       # close after every read

# Using the seek function, we can move to any point in the file and read the file
complete_text.seek(0)

complete_text.read()
```


#### Using the seek function, we can move to any point in the file and read the file
```python
# read from 300th character in the file
complete_text.seek(300)

# read the file
complete_text.read()

# close the file
complete_text.close()
```

#### Read the file line by line
```python
# read the file again store each line in a list
text_file = open("dataset/file_1.txt", "r")

lines = text_file.readlines()

# no of lines
print('No of lines in file is ', format(len(lines)))

# print each line text
for line in lines:
    print(line)

# close the file
text_file.close()
```


#### Another way to read text files
```python
# Using with statement, python will automatically closes the file after reading it
with open('dataset/file_1.txt', 'r') as f:
    complete_text = f.read()

complete_text
```

#### Writing text files
*write function will return the number of characters written in the file*
```python
# let's open a file in write only mode
my_file = open('dataset/new_file.txt', 'w')

# write function will return the length of text written in the file
my_file.write('Data Science is Awesome!')
```

```python
# open the file write and read mode
my_file = open('dataset/new_file.txt', 'w+')

# read the file
my_file.read()

# close the file
my_file.close()

# Now, add some lines to the file again
my_file = open('dataset/new_file.txt', 'w+')

# create a list of strings
lines = ['Line 1', 'Line 2', 'Line 3', 'Line 4']
my_file.writelines(lines)

# take the pointer to the initial position
my_file.seek(0)

# read the data
print(my_file.read())
my_file.close()
```
*The context is overwritten when we tried to write again on the same file*


#### Append text in file
```python
# open the file in the append and read mode
my_file = open('dataset/new_file.txt', 'a+')

my_file.write('Welcome to the python course')

# take the pointer to the initial position of the file
my_file.seek(0)

# read the file
my_file.read()
```



