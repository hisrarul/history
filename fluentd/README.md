## Fluentd

#### Run on docker container
```
docker run -p 24220:24220 -p 24224:24224 -v ~/practice_minikube/fluentd:/fluentd/etc -e FLUENTD_CONF=docker.conf fluent/fluentd:stable
```

#### Send json data to fluentd container using curl
```
curl -X POST -d 'json={"hi":"mom", "severity":"superbad"}' http://localhost:24220/test/ing
```

#### Run container with fluentd driver
```
docker run -P -d --log-driver=fluentd nginx
```
