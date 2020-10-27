## Hadoop

#### Run Hadoop cluster on docker container
```
docker-compose -f docker-compose.yaml up -d
```

#### Upload files to hadoop using curl [[1]](https://knox.apache.org/books/knox-0-6-0/user-guide.html) [[2]](https://hadoop.apache.org/docs/r1.0.4/webhdfs.html#CREATE)
```
curl -i -k -u guest:guest-password -X GET \
    'https://localhost:8443/gateway/sandbox/webhdfs/v1/<path_in_hdfs_to_be_uploaded>?op=CREATE&overwrite=true'

curl -i -k -u guest:guest-password -X GET \
    '{Value of Location header from command response above}'
    
``` 

#### Deploy and Configure a Single-Node Hadoop Cluster
> Learnt from Linux Academy and Steps to follow [[1]](https://github.com/hisrarul/history/blob/master/hadoop/hadoop_single_node_cluster.md)
