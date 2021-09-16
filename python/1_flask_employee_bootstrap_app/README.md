## Deploy Flask Application
<ol>
  <li>
    <h4>Write a basic python application with any backend database</h4>
  </li>
  <li>
    <h4>
      Dockerize it with Nginx as a frontend proxy server to python app.
    </h4>
  </li>
  <li>
    <h4>
      Write an Ansible playbook to deploy on any public cloud
    </h4>
  </li>
</ol>

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

Referred: https://www.youtube.com/watch?v=XTpLbBJTOM4&t=1583s