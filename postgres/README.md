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


#### Postgres dump and restore directly to another container or pod
```bash
POSTGRES_PASSWORD='<enter_password>'
PGPASSWORD="$POSTGRES_PASSWORD" pg_dump -t <table_name_in_rds> -h <rds_instance_endpoint_url> -U <user_name> <db_in_rds> | PGPASSWORD="$POSTGRES_PASSWORD" psql -h <postgres_pod_svc_name> -U <user_name_in_pod> -p 5432 <db_name_in_pod>
```


#### Create app user in postgres with rbac
```bash
CREATE ROLE "super_role" WITH SUPERUSER CREATEDB CREATEROLE;

CREATE ROLE "admin_role" WITH CREATEDB;

CREATE ROLE "viewer_role";

CREATE USER "<user_thanos>" WITH PASSWORD '<user_password>';

CREATE USER "<user_thor>" WITH PASSWORD '<user_password>';

# Grant super role to internal admin user
GRANT "super_role" to "<internal_admin_user>";

# Grant admin role to user thanos
GRANT "admin_role" to "<user_thanos>";

GRANT "admin_role" to "<user_thor>";

# Alter owner
ALTER DATABASE <db_name_1> OWNER TO admin_role;

# Grant connect access on databases to admin_role
GRANT CONNECT, CREATE, TEMPORARY ON DATABASE  "<db_name_1>" TO "admin_role";
GRANT CONNECT, CREATE, TEMPORARY ON DATABASE  "<db_name_2>" TO "admin_role";

# Grant usage of public schema to admin role
GRANT USAGE ON SCHEMA public to "admin_role";

# Grant usage access of all sequences in public schema to admin role
GRANT USAGE, SELECT, UPDATE ON ALL SEQUENCES IN SCHEMA public TO "admin_role";

# Grant write access on all tables to admin role
GRANT SELECT, INSERT, DELETE, UPDATE, TRUNCATE, REFERENCES, TRIGGER ON ALL TABLES IN SCHEMA public TO "admin_role";

# Grant usage access on other schema 
GRANT USAGE ON SCHEMA <other_schema_name> to "admin_role";

# Grant usage access of all sequences in other schema to admin role
GRANT USAGE, SELECT, UPDATE ON ALL SEQUENCES IN SCHEMA <other_schema_name> TO "admin_role";

# Grant write access on all table in other schema to admin role
GRANT SELECT , INSERT, DELETE, UPDATE, TRUNCATE, REFERENCES, TRIGGER ON ALL TABLES IN SCHEMA <other_schema_name> TO "admin_role";

# Alter default privileges in public schema and grant read access to admin and viewer role
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO admin_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON SEQUENCES TO viewer_role;

## Grant read access to viewer_role

# Grant usage access on public schema to viewer role
GRANT USAGE ON SCHEMA public to "viewer_role";

# Grant usage access on all sequences in public schema to viewer role
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO "viewer_role";

# Grant read access on all tables in public schema to viewer role
GRANT SELECT ON ALL TABLES IN SCHEMA public TO "viewer_role";
```
