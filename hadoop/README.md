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

#### Take the Hadoop backup to s3 bucket
```
#List the files in hdfs
hadoop fs -ls hdfs://<hadoop_url>:<hadoop_path>/dir/sub-dir/

#Copy the directories of hdfs to s3 bucket
hadoop distcp hdfs://<hadoop_url>:<hadoop_path>/dir/sub-dir/ s3a://<s3-bucket-name>/<folder-s3-bucket>/
```
