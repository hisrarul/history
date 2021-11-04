## Spark

#### Hadoop
Data processing problems were alleviated by the advent of Hadoop. Mapreduce is like pushing square peg through a round whole (meaning Hadoop is very restrictive in design and has narrow focus on batch processing). This led to new API in Big data mental model each attempting to solve different problem. For e.g.
1. To process streaming data at scale then we can use complementary library called Storm.
2. Get rid of some of the cruft around the MapReduce boilerplate so you might turn to Scalding.
3. Query data easily using Hive.
4. There are other too such as mahout, Apache Drill, HBASE, Flume, Apache Giraph

#### Spark
Spark solves above problems and it is a unified solution for big data. Also SDK for the many different means of processing. The high level spark components:
1. Spark Core
2. Spark SQL
3. Spark Streaming
4. MLib (Machine learning)
5. GraphX (graph)
6. DataFrames/Datasets

#### Read text file into RDD
```scala
<!-- Open spark shell using spark-shell command -->
val textFile = sc.textFile("file:///opt/spark/README.md")
textFile.first

<!-- textFile value to map each line of the file, spitting it into an array of space delimited words and flattening the resultant sequence of string arrays into a single long sequence -->
val tokenizedFileData = textFile.flatMap(line=>line.split(" "))

<!-- Convert sequence by counting each word into a key value pair where the word is the key and value is the count -->
val countPrep = tokenizedFileData.map(word=>(word, 1))

<!-- Reduce the values down to a single count for each key -->
val counts = countPrep. reduceByKey((accumValue, newValue)=>accumValue + newValue)

<!-- Sorting our list of word and _2 means access objects in the second position of a tuple. -->
val sortedCounts = counts.sortBy(kvPair=>kvPair._2, false)

<!-- Write action to a file -->
sortedCounts.saveAsTextFile("file:///opt/spark/PluralSightData/ReadMeWordCount")

<!-- CountByValue combines the map and reduce by key into one well-named method -->
tokenizedFileData.countByValue
```

#### Install SBT on Linux
```bash
# https://www.scala-sbt.org/1.x/docs/Installing-sbt-on-Linux.html
sudo apt-get update
sudo apt-get install apt-transport-https curl gnupg -yqq
echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | sudo tee /etc/apt/sources.list.d/sbt_old.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo -H gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/scalasbt-release.gpg --import
sudo chmod 644 /etc/apt/trusted.gpg.d/scalasbt-release.gpg
sudo apt-get update
sudo apt-get install sbt
```

#### Run and Initialize the project
```bash
# https://docs.scala-lang.org/getting-started/index.html
sbt new scala/hello-world.g8

# update libraryDependencies
libraryDependencies += "org.apache.spark" %% "spark-core" % "3.2.0" % "provided"

# run command
sbt
~run

```

#### Resources
[1](https://adamdrake.com/command-line-tools-can-be-235x-faster-than-your-hadoop-cluster.html)
[2](https://www.chrisstucchio.com/blog/2013/hadoop_hatred.html)
[3](https://spark.apache.org/docs/latest/)
[4. Book Learning Spark](https://www.oreilly.com/library/view/learning-spark/9781449359034/)
[5](https://github.com/apache/spark)

