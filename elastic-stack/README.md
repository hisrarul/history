## Elastic Stack

### Create elasticsearch pod
```
kubectl create -f https://github.com/hisrarul/history/blob/master/elastic-stack/elasticsearch.yaml
kubectl get pod elastic-search -n elastic-stack -o yaml
```


### Create kibana pod
```
kubectl create -f https://github.com/hisrarul/history/blob/master/elastic-stack/kibana.yaml
kubectl get pod kibana -n elastic-stack -o yaml
```

### Create application pod to generate logs
```
kubectl create -f https://github.com/hisrarul/history/blob/master/elastic-stack/es-app.yaml
kubectl get pod app -n elastic-stack -o yaml
```

### Add a sidecar to send the log of container to Elasticsearch
```
kubectl create -f https://github.com/hisrarul/history/blob/master/elastic-stack/es-sidecar.yaml
```

## Backup and Restore in Elasticsearch

#### Take backup in form of snapshot in elasticsearch
```
PUT /_snapshot/your_s3_respository/your_backup_name/?pretty
{
  "indices": "index1, index2 ",
  "ignore_unavailable": true,
  "include_global_state": false
}
```

## Change replica count

#### Create template for replica count
```
#It is applicable on new indices starting with security-auditlog
curl -XPUT -k -u 'username:password' https://localhost:9200/_template/zeroreplicas -H 'Content-Type: application/json' -d '{"template" : "*", "index_patterns": ["security-auditlog-*"], "settings" : { "number_of_shards": 1, "number_of_replicas" : 0 } }}'
```

#### Change the replica count for existing index
```
curl -X PUT -k -u "$ELASTIC_USERNAME:$ELASTIC_PASSWORD"  https://localhost:9200/security-auditlog-2017.10.30/_settings -H 'Content-Type: application/json' -d '{ "index": {"number_of_replicas": 0 } }'
```

#### Error: Request entity too large
```
    #Add this value in kibana.yml
    server.maxPayloadBytes: 10000000
```

## Add your own SSL certificates to Open Distro for Elasticsearch
+ [Detailed Steps](https://github.com/hisrarul/history/blob/master/elastic-stack/renew_certificates.md)
