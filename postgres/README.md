## Postgres Database

#### Start postgres db instance on docker using cli
```
sudo docker run \ 
    --restart always \
    --name posttest \
    -p 5432:5432 \
    -v /mnt/data/postgres/:/var/lib/postgresql/data/ \
    -e POSTGRES_PASSWORD=password \
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

##### Now, we can access postgres database from the browser.
