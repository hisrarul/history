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

