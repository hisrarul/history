## MYSQL 5.7.1x

#### Check version of mysql
```SELECT @@version;```

#### Create username
```CREATE USER 'yourUsername' IDENTIFIED BY 'yourPassword';```

#### Grant write access
```GRANT SELECT, INSERT, UPDATE, CREATE, CREATE VIEW, SHOW VIEW, TRIGGER ON `yourDbName`.* TO 'yourUsername'```

#### Grant read access
```GRANT SELECT ON `yourDbName`.* TO 'yourUsername'```

#### Revoke write access
```REVOKE SELECT, INSERT, UPDATE, CREATE, CREATE VIEW, SHOW VIEW, TRIGGER ON `yourDbName`.* FROM 'yourUsername';```

#### Change password 
```ALTER USER 'user'@'hostname' IDENTIFIED BY 'yourNewPassword';``` [Know more](https://dev.mysql.com/doc/refman/8.0/en/resetting-permissions.html)


#### Grant access to multiple tables starting with a prefix 'foo'
```
SELECT   CONCAT('GRANT SELECT , INSERT, UPDATE, DELETE ON database_name.', TABLE_NAME, ' to ''username''@''%'';')
FROM     INFORMATION_SCHEMA.TABLES
WHERE    TABLE_SCHEMA = 'database_name'        #check schema name
  AND TABLE_NAME LIKE 'foo_%';
  
#copy the output and execute them as sql command
```

## Run mysql and adminer using docker compose
```
docker-compose -f docker-compose-mysql.yaml up -d
```

#### Delete rows from table
```
DELETE FROM `<table_name>`
WHERE ((`id` = '1') OR (`id` = '8'));
```


#### MySQL dump and restore to another logical database
```bash

###
# ERROR 1227 (42000)
# /*!50003 CREATE*/ /*!50017 DEFINER=`databaseUserNameOld`@`%`*/ /*!50003 TRIGGER `database_name_1`.tagging_after_insert AFTER INSERT ON tagging FOR EACH ROW
###

sed -i 's/database_name_1/database_name_2/' database_name_1.sql
sed -i 's#DEFINER=`databaseUserNameOld`/DEFINER=`databaseUserNameNew`#g' database_name_1.sql

log_bin_trust_function_creators = 1

mysqldump -h database-endpoint.rds.amazonaws.com --databases database_name_1 --set-gtid-purged=OFF -u databaseUserNameOld -p > database_name_1.sql
mysql -h database-endpoint.rds.amazonaws.com -D database_name_2 -u databaseUserNameNew -p < database_name_1.sql
```


#### Modify colum of a table with Auto increment
```sql
ALTER TABLE `table_name`
CHANGE `column_name` `column_name` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;
```
