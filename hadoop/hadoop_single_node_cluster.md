## Deploy and Configure a Single-Node Hadoop Cluster

#### Install Java
```
yum install java-1.8.0-openjdk -y
```

#### Deploy Hadoop
```
curl -O http://mirrors.gigenet.com/apache/hadoop/common/hadoop-2.9.2/hadoop-2.9.2.tar.gz
tar -xvzf hadoop-2.9.2.tar.gz
mv hadoop-2.9.2 hadoop
```

#### Configure JAVA_HOME
```
which java
ls -l /etc/alternatives/java
ls -l /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.262.b10-0.el7_8.x86_64/jre/bin/java

## update java home path
vi hadoop/etc/hadoop/hadoop-env.sh
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.262.b10-0.el7_8.x86_64/jre
```

#### Configure core hadoop
```
## update core-site.xml file
vi hadoop/etc/hadoop/core-site.xml

<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>
```

#### Configure HDFS
```
## Set the default block replication to 1
vi hadoop/etc/hadoop/hdfs-site.xml

<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
</configuration>
```

#### Set up passwordless SSH Access to localhost
```
ssh-keygen
cat ~/.ssh/id_rsa.pub >>  ~/.ssh/authorized_keys
```

#### Format the filesystem 
```
## Format the DFS
hadoop/bin/hdfs namenode -format
```

#### Start Hadoop
```
## Start the namenode and datanode
hadoop/sbin/start-dfs.sh
```

#### Download and copy the latin text to hadoop
```
curl -O https://raw.githubusercontent.com/linuxacademy/content-hadoop-quick-start/master/latin.txt
hadoop/bin/hdfs dfs -mkdir -p /user/home_directory

## save the latin.txt as latin file in hadoop
hadoop/bin/hdfs dfs -put latin.txt latin
```

#### Examine the latin.txt with mapreduce
```
## Calculate the average length of the words  in latin file
cat hadoop/bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.9.2.jar wordmean latin latin_wordmean_output

## examine your wordmean job output files
hadoop/bin/hdfs dfs -cat latin_wordmean_output/*
```
