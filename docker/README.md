## Steps

#### Make sure that docker compose is up and running. Otherwise install using below command
curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

#### Change directory to `docker` folder

#### Build the image
`docker-compose build`

#### Run the container
`docker-compose up`


#### Accessing private repository in npm ci in Docker
```
ssh-keygen -f id_rsa (generate in current dir)
key=$(cat id_rsa)
docker build -f Dockerfile_nodejs_package --build-arg SSH_KEY="$key" -t ssh-test .
```
