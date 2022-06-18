## Collections

* Specialized container datatypes providing alternatives to Python's general purpose built-in containers, dict, list, set and tuple.

* Alternative to dict, list, set and tuple
    * `defaultdict()` provides default value for keys that do not exist
    * `counter()`: dict subclass which helps to count hashable objects
    * `deque()`: double ended queue for fast appends and pops from either end


#### defaultdict()
A dict subclass that provides default value for key that do not exist.

```python
# storing work ex in months
work_exp = {"Rachel": 31, "Ross": 42, "Joey": 12, "Monica": 28}
print(work_exp['Emma']) # this will give error
```

Using default dict

```python
work_exp_defaultdict = collections.defaultdict(int, Rachel = 31, Ross = 42, Joey = 12, Monica = 28)
print(work_exp_defaultdict['Emma'])     # this will give 0 value for unknown key
```

```python
work_exp_defaultdict = collections.defaultdict(
    lambda: "Not present", Rachel=31, Ross=42, Joey=12, Monica=28
)
print(work_exp_defaultdict["Emma"])
```

#### Counter()
It is a collection where elements are stored as dictionary keys and their counts are stored as dictionay values.

```python
av_text = 'Analytics Vidhya is a platform to learn about Data Science, Machine Learning, Deep Learning, Data Visualisations, Business Analytics, Big Data and more'
words = av_test.split()

collections.Counter(words)  # dict output with count of each word

collections.Counter(words).most_common(3)
```

#### deque()
```python
word_queue = collections.deque(words)
word_queue.popleft()   # delete from left
word_queue.pop()       # delete from right
```


#### Applications: collections
Pandas Implementation

```python
for _ in range(startrow):
    wks.addElement(TableRow())

rows: DefaultDict = defaultdict(TableRow)
col_count: DefaultDict = defaultdict(int)

for cell in sorted(cells, key=lambda cell: (cell.row, cell.col)):
    # only add empty cells if the rows is still empty
    if not col_count[cell.row]:
        for _ in range(startcol):
            rows[cell.row].addElement(TableCell())
```


