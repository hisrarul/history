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

## Add your own SSL certificates to Open Distro for Elasticsearch
+ [Detailed Steps](https://github.com/hisrarul/history/blob/master/elastic-stack/renew_certificates.md)
