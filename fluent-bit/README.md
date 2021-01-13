## Fluent-bit


#### error: {"index":{"_index":"kubernetes_cluster-xxxx.xx.xx","_type":"_doc","_id":"xxxxxxxxxxxxxx","status":400,"error":{"type":"mapper_parsing_exception","reason":"Could not dynamically add mapping for field [app.kubernetes.io/instance]. Existing mapping for [kubernetes.labels.app] must be of type object but found [text]."}}}
Ref [[1]](https://coralogix.com/log-analytics-blog/elasticsearch-mapping-exceptions-the-complete-guide/) [[2]](https://discuss.elastic.co/t/filebeats-auto-mapping-of-kubernetes-labels-causing-big-issues/154718/9)
```
1. If your index is not important stored in elasticsearch then delete the indices using DEV tool in kibana
DELETE kubernetes_cluster-xxxx*

2. Check the indices again. Fluent-bit will again start sending the data to elasticsearch from today's date.
GET _cat/indices/kubernetes_cluster-xxxx*
```
