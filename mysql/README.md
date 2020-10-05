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


## Run mysql and adminer using docker compose
```
docker-compose -f docker-compose-mysql.yaml up -d
```
