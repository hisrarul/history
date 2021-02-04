## Postgres Database

#### Start postgres db instance on docker using cli
```
sudo docker run \ 
    --restart always \
    --name posttest \
    -p 5432:5432 \
    -v /mnt/data/postgres/:/var/lib/postgresql/data/ \
    -e POSTGRES_PASSWORD=yourpassword \
    -d postgres:11.7
```

#### Start postgres db instance using docker-compose and access via adminer

Filename: stack.yaml

```
version: '3.1'
services:
  postgres_db:
    image: postgres:11.7
    container_name: posttest
    network_mode: bridge
    ports:
      - 5432:5432
    environment:
      POSTGRES_PASSWORD: password
    volumes:
      - /mnt/data/postgres/:/var/lib/postgresql/data/
  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
```

docker-compose -f stack.yaml up

#### Create users in postgres database

``` CREATE USER "yourusername" WITH PASSWORD 'yourpassword';```

#### Grant access to tables in schema other than public
```
GRANT USAGE ON SCHEMA otherthanpublicschema TO "yourusername";
GRANT SELECT ON ALL TABLES IN SCHEMA otherthanpublicschema TO "yourusername";
GRANT SELECT ON ALL TABLES IN SCHEMA public TO "yourusername";
```

#### Default permission on tables of public schema
When you delete your table XYZ and create table with the same name, the user lose permission on that table. In such cases, default permission is very useful to retain the access of user in new table XYZ.
```
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES to "yourusername";
```

#### [Grant read access to single table](https://tableplus.com/blog/2018/04/postgresql-how-to-create-read-only-user.html)
```
CREATE USER "yourUsername" WITH PASSWORD 'yourPassword';
GRANT CONNECT ON DATABASE yourDbName TO "yourUsername";
GRANT USAGE ON SCHEMA yourSchemaName TO "yourUsername";
GRANT SELECT ON yourTableName TO "yourUsername";
```

#### Postgres database dump and restore
```
#https://www.postgresql.org/docs/9.4/backup-dump.html
pg_dump -h endpoint -U username -d dbname -W > dumpfile
psql -h endpoint -U username -d dbname -W dbname < dumpfile
```

#### Postgres Role based authentication
```
#only owner of the database can grant the permission or change the owner who has permission.
CREATE USER "username" WITH PASSWORD "yourpassword";
CREATE ROLE roleviewer;
GRANT roleviewer to username;
GRANT USAGE ON SCHEMA public to roleviewer;
GRANT SELECT ON ALL TABLES IN SCHEMA public to viewer;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO roleviewer;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON SEQUENCES TO roleviewer;

#permission on tables present other than in public schema
GRANT USAGE ON SCHEMA otherthanpublicschema to roleviewer;
GRANT SELECT ON ALL TABLES IN SCHEMA otherthanpublicschema to viewer;
ALTER DEFAULT PRIVILEGES IN SCHEMA otherthanpublicschema GRANT SELECT ON TABLES TO roleviewer;
ALTER DEFAULT PRIVILEGES IN SCHEMA otherthanpublicschema GRANT SELECT ON SEQUENCES TO roleviewer;

#some other cases
#https://dba.stackexchange.com/questions/117109/how-to-manage-default-privileges-for-users-on-a-database-vs-schema/117661#117661
ALTER DEFAULT PRIVILEGES FOR USER username IN SCHEMA public GRANT SELECT ON TABLES TO roleviewer;
ALTER DEFAULT PRIVILEGES FOR ROLE role-name IN SCHEMA public GRANT SELECT ON SEQUENCES TO roleviewer;
```

#### Change table owner
```
# check owner of tables in other schema
\dt otherthanpublicschema.;

# Alter owner of table in other schema, after executing below command new owner can grant the permission to other roles or users.
ALTER TABLE otherthanpublicschema.table_name OWNER TO newuserOrrole;

OR

ALTER TABLE <tablename> OWNER TO <username>
```

#### Alter schema
```
ALTER SCHEMA name RENAME TO newname
ALTER SCHEMA name OWNER TO newowner

# Check schema permission
SELECT *, "oid" FROM "pg_namespace" LIMIT 50
```

#### All about sequence
```
SELECT * FROM information_schema.sequences;
```

#### Summary of Access Privileges
Ref : https://www.postgresql.org/docs/13/ddl-priv.html
|Object Type |	All Privileges | Default PUBLIC Privileges | psql Command |
|------|---------|--------|---------|
| DATABASE	| CTc	| Tc	| \l |
| DOMAIN	| U	| U	| \dD+ |
| FUNCTION or PROCEDURE | X	| X	| \df+|
FOREIGN DATA WRAPPER	| U	| none	| \dew+
FOREIGN SERVER	| U	| none	| \des+
LANGUAGE	| U	| U	| \dL+
LARGE OBJECT	| rw |	none	 
SCHEMA	| UC	| none	| \dn+
SEQUENCE | rwU	| none	| \dp
TABLE (and table-like objects)	| arwdDxt |	none |	\dp
Table column	| arwx |	none |	\dp
TABLESPACE	| C	| none	| \db+
TYPE	| U	| U	| \dT+
