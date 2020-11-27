## Hadoop Basic Learning
```
# ls
# mkdir
# copytolocal
# copyfromlocal
# cp
# Ddfs.replication=2
# chmod
```

#### Listing root directory
```hadoop fs -ls /```

#### Listing default to home directory
```
hadoop fs -ls
hadoop fs -ls /user/hirwuser150430
```

#### Create a directory in HDFS
```
hadoop fs -mkdir hadoop-test1
```

#### Copy from local fs to HDFS
```
hadoop fs -copyFromLocal  /hirw-starterkit/hdfs/commands/dwp-payments-april10.csv hadoop-test1
```

#### Copy from HDFS to local
```
hadoop fs -copyToLocal hadoop-test1/dwp-payments-april10.csv .
hadoop fs -ls hadoop-test1
```

#### Copy a file from one folder to another
```
hadoop fs -cp hadoop-test1/dwp-payments-april10.csv hadoop-test2
```

#### Move a file from one folder to another
```
hadoop fs -mv hadoop-test1/dwp-payments-april10.csv hadoop-test3
```

#### Check replication
```hadoop fs -ls hadoop-test3```

#### Change or set replication factor
```
hadoop fs -Ddfs.replication=2 -cp hadoop-test2/dwp-payments-april10.csv hadoop-test2/test_with_rep2.csv
hadoop fs -ls hadoop-test2
hadoop fs -ls hadoop-test2/test_with_rep2.csv
```

#### Change permission
```
hadoop fs -chmod 777 hadoop-test2/test_with_rep2.csv
```

#### Filesystem check - Requires admin previliges
```
sudo -u hdfs hdfs fsck /user/hirwuser150430/hadoop-test2 -files -blocks -locations 
sudo -u hdfs hdfs fsck /user/hirwuser150430/hadoop-test3 -files -blocks -locations 
sudo -u hdfs hdfs fsck /user/ubuntu/input/yelp/yelp_academic_dataset_review.json -files -blocks -locations

# the blocks are getting saved in local filesystem which admin defines in /etc/hadoop/conf/hdfs-site.xml
```

#### Delete dir/files in HDFS
```
hadoop fs -rm hadoop-test2/test_with_rep5.csv
hadoop fs -rm -r hadoop-test1
hadoop fs -rm -r hadoop-test2
```
