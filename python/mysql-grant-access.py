import pymysql.cursors
import sys

# Connect to the database
connection = pymysql.connect(host='172.17.0.1',
                             user='root',
                             password='example123',
                             db='mysql',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def createUser(username, password, querynum=0, updatenum=0, connection_num=0):
    try:
        with connection.cursor() as cursor:
            createUser = "CREATE USER '{}'@'localhost' IDENTIFIED BY '{}';".format(username, password)
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
                sql = "GRANT SELECT, INSERT, UPDATE, CREATE, REFERENCES, INDEX, ALTER, EXECUTE, CREATE VIEW, SHOW VIEW, ALTER ROUTINE, TRIGGER ON `{}`.* TO '{}'@'%'".format(dbName, username)
                cursor.execute(sql)
                print("Write access has been granted on {} to user, {}".format(dbName, username))
    except:
        print('Unable to provide write access!')

db = []
action = sys.argv[1]
username = sys.argv[2]

for dbName in sys.argv[3:]:
    db.append(dbName)

try:
    if action == 'read':
        readAccess(username, db)
    elif action == 'write':
        writeAccess(username, db)
    else:
        print('Define actions, read or write!')

    connection.close()
except:
    print("Something went wrong!")
