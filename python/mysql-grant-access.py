import pymysql.cursors
import argparse
import sys
import random
import string

dbEndpoint = sys.argv[1]
dbLoginUser = sys.argv[2]
dbLoginPassword = sys.argv[3]

connection = pymysql.connect(host=dbEndpoint,
                             user=dbLoginUser,
                             password=dbLoginPassword,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def createUser(username, password, querynum=0, updatenum=0, connection_num=0):
    try:
        with connection.cursor() as cursor:
            createUser = "CREATE USER '{}'@'%' IDENTIFIED BY '{}';".format(username, password)
            cursor.execute(createUser)
            print("User, {} has create successfully!".format(username))
    except:
        print("Error creating MySQL user: {}".format(username))


def checkUser(username):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT USER FROM `mysql`.user WHERE USER like '%{}%'".format(username)
            cursor.execute(sql)
            usersList = cursor.fetchall()
            if not usersList:
                print("'{}', No such user available!".format(username))
            else:
                for user in usersList:
                    if username in user['USER']:
                        print("'{}', user already exist!".format(username))
                    else:
                        print("'{}', user doesn't exist!".format(username))
    except Exception as err:
        print(err)


def usageAccess(username):
    try:
        # Check user existence
        checkUser(username)
        with connection.cursor() as cursor:
            sql = "GRANT USAGE ON *.* TO '{}'@'%';".format(username)
            cursor.execute(sql)
            print("Usage access has been granted to user, '{}'".format(username))
    except:
        print('Unable to provide usage access!')


def readAccess(username, dbList):
    try:
        # Check user existence
        checkUser(username)
        with connection.cursor() as cursor:
            for dbName in dbList:
                sql = "GRANT SELECT ON `{}`.* TO '{}'@'%';".format(dbName, username)
                cursor.execute(sql)
                print("Read access has been granted on '{}' to user '{}'".format(dbName, username))
    except:
        print('Unable to provide read access!')

def writeAccess(username, dbList):
    try:
        # Check user existence
        checkUser(username)
        with connection.cursor() as cursor:
            for dbName in dbList:
                sql = "GRANT SELECT, INSERT, UPDATE, CREATE, DELETE, DROP, REFERENCES, INDEX, ALTER, EXECUTE, CREATE VIEW, SHOW VIEW, ALTER ROUTINE, TRIGGER ON `{}`.* TO '{}'@'%'".format(dbName, username)
                cursor.execute(sql)
                print("Write access has been granted on {} to user, {}".format(dbName, username))
    except:
        print('Unable to provide write access!')

def get_password_str(length):
    letters = string.ascii_lowercase
    password_str = ''.join(random.choice(letters) for i in range(length))
    return password_str

db = []
action = sys.argv[4]
username = sys.argv[5]
password = get_password_str(14)

for dbName in sys.argv[6:]:
    db.append(dbName)

try: 
    if action == 'read':
        readAccess(username, db)

    elif action == 'create':
        createUser(username, password)
        print("user password: {}".format(password))

    elif action == 'write':
        writeAccess(username, db)

    else:
        print('mysql_access.py dbEndpoint dbLoginUser dbLoginPassword action=create/read/write username dbName1 dbName2')

    connection.close()
except:
    print("Something went wrong!")
