## Deploy Flask Application

#### Run Docker compose
```bash
docker-compose up --build --force-recreate
```

#### Create table for the first time

<ol>
  <li>Copy the container id from the command: <b>docker ps</b></li>
  <li>Exec to web container using cli: docker run -it <b>web container id</b> /bin/bash</li>
  <li>Run python script using <b>python create_table.py</b></li>
</ol>