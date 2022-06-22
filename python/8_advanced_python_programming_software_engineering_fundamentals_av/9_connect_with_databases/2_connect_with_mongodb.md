## MongoDB

* Widely used dictionary based database
* Flexible, No-SQL database
* Can store any data
* Scalable and distributed in nature
* Can be store/operated over cluster

```python
%load_ext lab_black

!pip3 install pymongo

# importing the required libraries
import pymongo
import pprint
import json
import warnings

warnings.filterwarning("ignore")

# connect to the mongo client
client = pymongo.MongoClient("mongodb://localhost:27017")

# mongo restore HR data
!mongorestore --db training /path

# list available databases
client.list_database_names()

# get the database
db = client["training"]     # training is the database name

# list collections
db.list_collection_names()

# print one document
db.hr.find_one()        # hr is the collection name

# print in readable structure
pprint.pprint(db.hr.find_one())
```
