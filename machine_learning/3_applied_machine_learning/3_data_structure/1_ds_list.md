#### Why Data Structure

*Existing data types* - int, float, bool, str

#### Problems with existing data types
* Data in a variable can be stored in a single format i.e either integers or decimals or strings etc.
* Large memory overhead by creating large number of variables.
* Ungit for storing large structured data.

#### What is a data structure
The data structure has three main properties.
* Efficient storage for large data
* Manipulations/Operations on data
* Underlying relationships of data.

#### Different data structure in Python
* List
* Tuple
* Set
* Dictionary

#### List
A list is an ordered data structure with elements separated by comma and enclosed within square brackets. And python remember the order of the list meaning that each element has an index in it starting from zero. e.g.

```python
list 1 = [2, 3, 4, 5, 6]                        # single data type

list2 = ["Python", "is", "Awesome"]             # single data type

list3 = [1, "Python", 2, "is", 3, "Awesome"]   # mixed data type
index = 0, 1, 2, 3, 4, 5

# to extract a single element
list3[1]    # output value will be Python because it is present at index position 1

# To extract a sequence of elements
list3[1:4]  # get the value from starting index position 1 to end index position 3

# Adding a single element
list3.append(4)

# Adding multiple elements
list3.extend([5,6])

# Deleting an element by value
list3.remove("is")

# Deleting an element by index
del list3[3]

# using step 2
list3[0:5:2]

# reverse the list using step value as -1
list3[::-1]

# insert value at the index position
list3.insert(0, 33)

# check if the particular element is present in the list or not
90 in list3                 # false

["Python", 2] in list3      # check sub-list o/p: false

[33] not in list3           # true, not in list3

# find index position of an element
list3.index(2)

# iterate a list
for elment in list3:
    print(element)

# length of a list
print(len(list3))

# sorting list
print(sorted(list3))    # err bcz need to have any integers

list4 = [3, 3,1, 4,6]
print(sorted(list4))

# nested list
list4 = [1, 3, 4, [5, 6], [A, B, C]]
```


#### Question to solve:
Marks of 5 different subject out of 100
```python
# student marks
student_marks = [['Name',    ['A', 'B', 'C', 'D', 'E']],
                 ['Ankit',   [41, 34, 45, 55, 63]],
                 ['Aravind', [42, 23, 34, 44, 53]],
                 ['Lakshay', [32, 23, 13, 54, 67]],
                 ['Gyan',    [23, 82, 23, 63, 34]],
                 ['Pranav',  [21, 23, 25, 56, 56]]
]
* Who scored the highest marks in subject B
* What is the average marks scored in the subject C?
* Who scored the highest percentage of marks?
* If considered only top-4 subjects of a candidate, then who scored the highest percentage of marks?

```python
# 1
score = []
for subject_b in student_marks:
    if type(subject_b[1][1]) == int:
        score.append(subject_b[1][1])
sorted(score)[-1]

# 2 solution
from functools import reduce

score = []
for subject_c in student_marks:
    if type(subject_c[1][1]) == int:
        score.append(subject_c[1][1])
avg_score = reduce(lambda x, y: x + y, score)/len(score)

# 3 solution
perc = []
student = []
for subjects in student_marks:
    if 'A' not in subjects[1]:
        student.append(subjects[0])
        perc.append(reduce(lambda x, y: x + y, subjects[1])/len(subjects[1]))
        pos = perc.index(max(perc))
print(student[pos])

# 4 solution
perc = []
student = []
for subjects in student_marks:
    if 'A' not in subjects[1]:
        student.append(subjects[0])
        perc.append(reduce(lambda x, y: x + y, sorted(subjects[1])[0:4])/len(subjects[1]))
        pos = perc.index(max(perc))
print(student[pos])
```


