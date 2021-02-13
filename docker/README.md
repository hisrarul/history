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

#### Different between CMD and ENTRYPOINT
```
Containers are designed to run specific and then exit.
#Build docker image
docker build -t docker-sleep .

#Here, the value of sleep is hard coded so container will run for 5 sec and exit.
#We don't have option to change the sleep time duruing execution **docker run docker-sleep sleep 10**
FROM ubuntu
CMD ["sleep", "5"]

#To change the sleep time during **docker run docker-sleep 10**, we use entrypoint. It allow us to append argument in the command for e.g(docker run docker-sleep 10)
#Problem, if we don't pass sleep time in the command it will through error
FROM ubuntu
ENTRYPOINT ["sleep"]

#To solve above problem, we can use both cmd and entrypoint
FROM ubuntu
ENTRYPOINT ["sleep"]
CMD ["5"]

To overwrite the entrypoint we can use it in the cli
docker run --entrypoint sleep2.0 docker-sleep 10
```
