##Ref 
#https://pypi.org/project/PyMySQL/
#https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html

import pymysql.cursors

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
            # print(createUser)
            cursor.execute(createUser)
        connection.commit()
    
    except:
        print("Error creating MySQL user: {}".format(username))

    finally:
        connection.close()

createUser('israrul', 'israrul123')
