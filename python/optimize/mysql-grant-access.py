import pymysql.cursors
import argparse
import sys
import random
import string

parser = argparse.ArgumentParser(description='Create mysql access.')
parser.add_argument('dbEndpoint', help='Enter url of the database.')
parser.add_argument('dbLoginUser', help='Enter username to login database who have grant permission.')
parser.add_argument('dbLoginPassword', help='Enter password to login database.')
parser.add_argument('action', help='Enter action, options: create/read/write/createread/createwrite/reset/del')
parser.add_argument('username', help='Enter username to create or provide access to.')
parser.add_argument('--dbName', nargs='+', help='Enter databases name seperated with spaces e.g. "--db prod non-prod".')
args = parser.parse_args()

connection = pymysql.connect(host=args.dbEndpoint,
                             user=args.dbLoginUser,
                             password=args.dbLoginPassword,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def createUser(username, querynum=0, updatenum=0, connection_num=0):
    try:
        with connection.cursor() as cursor:
            password = get_password_str(14)
            createUser = "CREATE USER '{}'@'%' IDENTIFIED BY '{}';".format(username, password)
            cursor.execute(createUser)
            print("User '{}' has create successfully with password '{}'".format(username, password))
    except:
        print("Error creating MySQL user: '{}'".format(username))


def delUser(username, querynum=0, updatenum=0, connection_num=0):
    try:
        with connection.cursor() as cursor:
            createUser = "DROP USER '{}'@'%';".format(username)
            cursor.execute(createUser)
            print("User '{}' deleted successfully!".format(username))
    except:
        print("Error deleting MySQL user: {}".format(username))


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
                        print("'{}', user exist!".format(username))
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
        with connection.cursor() as cursor:
            for dbName in dbList:
                sql = "GRANT SELECT ON `{}`.* TO '{}'@'%';".format(dbName, username)
                cursor.execute(sql)
                print("Read access has been granted on '{}' to user '{}'".format(dbName, username))
    except:
        print('Unable to provide read access!')


def writeAccess(username, dbList):
    try:
        with connection.cursor() as cursor:
            for dbName in dbList:
                sql = "GRANT SELECT, INSERT, UPDATE, CREATE, DELETE, DROP, REFERENCES, INDEX, ALTER, EXECUTE, CREATE VIEW, SHOW VIEW, ALTER ROUTINE, TRIGGER ON `{}`.* TO '{}'@'%'".format(dbName, username)
                cursor.execute(sql)
                print("Write access has been granted on '{}' to user '{}'".format(dbName, username))
    except:
        print('Unable to provide write access!')


def alterPassword(username):
    try:
        # Check user existence
        checkUser(username)
        password = get_password_str(14)
        with connection.cursor() as cursor:
            sql = "ALTER USER '{}'@'%' IDENTIFIED BY '{}';".format(username, password)
            cursor.execute(sql)
            print("User '{}' new password '{}'".format(username, password))
    except:
        print("Unable to reset password for user, '{}'!".format(username))


def get_password_str(length):
    letters = string.ascii_lowercase
    password_str = ''.join(random.choice(letters) for i in range(length))
    return password_str


try: 
    if args.action == 'create':
        createUser(args.username)

    elif args.action == 'read':
        readAccess(args.username, args.dbName)

    elif args.action == 'write':
        writeAccess(args.username, args.dbName)

    elif args.action == 'createread':
        createUser(args.username)
        readAccess(args.username, args.dbName)

    elif args.action == 'createwrite':
        createUser(args.username)
        writeAccess(args.username, args.dbName)
    
    elif args.action == 'pdreset':
        alterPassword(args.username)

    elif args.action == 'del':
        delUser(args.username)

    else:
        print(parser.parse_args(['-h']))

    connection.close()
except:
    print("Something went wrong!")
