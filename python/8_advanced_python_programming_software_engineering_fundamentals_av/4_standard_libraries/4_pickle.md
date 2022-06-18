## Pickle
The pickle module implements binary protocols for serializing and de-serializing a Python object structure.

* Used for serializing and de-serializing a Python object structure
* `Serializing:` The process to converts any kind of python objects (list, dict, etc) into byte streams (0s and 1s).
* `De-serializing`: Converts the byte stream (generated through pickling) back into python objects
* `dump()` and `load()` are the functios used for pickling and unpickling. The load function is used for `Serializing` and the dump function is used for `de-serializing`.

```python
import pickle

# out list and dictionary
emp_names = ["Akash", "Bhavish", "Chandra", "Derek"]
emp_ID = {"Akash": 1045, "Bhavish": 5306, "Chandra": 4931, "Derek": 5311}
```

Example 1
```python
# pickling
my_file = open("datafile.pkl", "wb")
pickle.dump(emp_names, my_file)  # list -> emp_names
my_file.close()
```

```python
# unpickling
my_file = open("datafile.pkl", "rb")
emp = pickle.load(my_file)
print(emp)
```

Example 2
```python
# pickling
my_file_2 = open("emp_ID.pkl", "wb")
pickle.dump(emp_ID, my_file_2)  # list -> emp_ID
my_file_2.close()
```

```python
# unpickling
my_file_2 = open("emp_ID.pkl", "rb")
EmpID = pickle.load(my_file_2)
print(EmpID)
```

#### Applications: pickle
Deploying machine learning models using Streamlit

```python
# saving the model
import pickle
pickle_out = open("classifier.pkl", mode="wb")
pickle.dump(model, pickle_out)
pickle_out.close()

# loading the trained model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)
```