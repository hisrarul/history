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

#### Using kibana dashboard
```
GET _cat/indices

GET logstash-2020.12.28/_settings

PUT logstash-2020.12.28/_settings 
{
  "index": {
    "number_of_replicas" : "0"
  }
}
```
---

### Error: Request entity too large
```
#Add this value in kibana.yml
server.maxPayloadBytes: 10000000
```
---

### Error: kibana is loading or wazuh plugin is not showing security and integrity events
+ [Detailed solution](https://github.com/hisrarul/history/blob/master/wazuh/README.md)
---

### Add your own SSL certificates to Open Distro for Elasticsearch
+ [Detailed Steps](https://github.com/hisrarul/history/blob/master/elastic-stack/renew_certificates.md)
---

### Check index pattern in .kibana 
```
GET .kibana_1/_search?_source=false&size=4
{
  "query": {
    "exists": {
      "field": "index-pattern"
    }
  }
}
```

### Error: [2019-03-26T16:40:43,447][WARN ][o.e.m.j.JvmGcMonitorService] [fycetJG] [gc][527283] overhead, spent [763ms] collecting in the last [1s]
Ref: [[1]](https://discuss.elastic.co/t/warn-message-elasticsearch/173975/3) [[2]](https://www.elastic.co/guide/en/elasticsearch/reference/current/tasks.html)
```
Possible solution: 
1. Increase the heap size from jvm.option
2. List the task and take appropriate action. GET _tasks?group_by=parents
``` 

#### [error] [out_es] could not pack/validate JSON response
Ref: [[1]](https://github.com/fluent/fluent-bit/issues/2078)
```
PUT _cluster/settings
{
    "persistent": {
        "action.auto_create_index": "true" 
    }
}
```
