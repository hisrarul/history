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
