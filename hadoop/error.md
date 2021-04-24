## Error

#### 1. requested data length 123300162 is longer than maximum configured RPC length 101372499.
or 
#### 2. Safe mode is ON

#### 3. HDFS stays in safe mode because of reported blocks not reaching 0.9990 of total blocks
```
Ref: https://community.pivotal.io/s/article/Hadoop-NameNode-Stuck-in-Safe-Mode-because-of-Error-Requested-Data-Length-is-Longer-than-Maximum-Configured-RPC-Length?language=en_US
https://www.systutorials.com/hdfs-stays-in-safe-mode-because-of-reported-blocks-not-reaching-0-9990-of-total-blocks/

1. hdfs dfsadmin -report
2. hdfs dfsadmin -safemode get
3. Reconfigure the cluster by adding the following lines to core-site.xml

 <property>
     <name>ipc.maximum.data.length</name>
     <value>123300162</value>
 </property>
 
4. Reboot the cluster
5. Once, namenode out of safemode then run fsck and delete/move corrupted files
hdfs fsck / -files -blocks -locations >> /hadoop/dfs/name/fsck_output_$(date +%d%m%y).txt
 ```
 
