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

#### Grant read access to single table
* [Referenced](https://tableplus.com/blog/2018/04/postgresql-how-to-create-read-only-user.html)
```
CREATE USER "yourUsername" WITH PASSWORD 'yourPassword';
GRANT CONNECT ON DATABASE yourDbName TO "yourUsername";
GRANT USAGE ON SCHEMA yourSchemaName TO "yourUsername";
GRANT SELECT ON yourTableName TO "yourUsername";
```
