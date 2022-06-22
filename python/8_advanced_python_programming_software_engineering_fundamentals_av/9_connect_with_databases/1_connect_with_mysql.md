## Connecting with MySQL

```python
%load_ext lab_black
```

#### Installing MySQL-Connector
```python
!pip3 install mysql-connector-python
```

#### Connecting to MySQL Server
```python
import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password"
)

print(db)

# Creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()        # it is like pointer which identify where we are in database

cursor.execute("SHOW DATABASES")    # run cmd

databases = cursor.fetchall()       # it returns a list of all databases present

print(databases)
```

#### Show and read tables
```python
import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="information_schema"
)

cursor = db.cursor()

cursor.execute("SHOW TABLES")

tables = cursor.fetchall()      # it returns a list of all databases present
print(tables)

cursor.execute("SELECT * FROM USER_ATTRIBUTES")
data = cursor.fetchall()    # it returns a list of all rows in table
print(data)
```
