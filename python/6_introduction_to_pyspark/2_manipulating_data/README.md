## Data manipulation

#### Creating columns
In this chapter, you'll learn how to use the methods defined by Spark's DataFrame class to perform common data operations.

Let's look at performing column-wise operations. In Spark you can do this using the .withColumn() method, which takes two arguments. First, a string with the name of your new column, and second the new column itself.

The new column must be an object of class Column. Creating one of these is as easy as extracting a column from your DataFrame using df.colName.

Updating a Spark DataFrame is somewhat different than working in pandas because the Spark DataFrame is immutable. This means that it can't be changed, and so columns can't be updated in place.

Thus, all these methods return a new DataFrame. To overwrite the original DataFrame you must reassign the returned DataFrame using the method like so:

df = df.withColumn("newCol", df.oldCol + 1)
The above code creates a DataFrame with the same columns as df plus a new column, newCol, where every entry is equal to the corresponding entry from oldCol, plus one.

To overwrite an existing column, just pass the name of the column as the first argument!

Remember, a SparkSession called spark is already in your workspace.

```python
# Create the DataFrame flights
flights = spark.table("flights")

# Show the head
flights.show()

# Add duration_hrs
flights = flights.withColumn("duration_hrs", flights.air_time / 60)
```

#### SQL in a nutshell
As you move forward, it will help to have a basic understanding of SQL. A more in depth look can be found here.

A SQL query returns a table derived from one or more tables contained in a database.

Every SQL query is made up of commands that tell the database what you want to do with the data. The two commands that every query has to contain are SELECT and FROM.

The SELECT command is followed by the columns you want in the resulting table.

The FROM command is followed by the name of the table that contains those columns. The minimal SQL query is:

SELECT * FROM my_table;
The * selects all columns, so this returns the entire table named my_table.

Similar to .withColumn(), you can do column-wise computations within a SELECT statement. For example,

SELECT origin, dest, air_time / 60 FROM flights;
returns a table with the origin, destination, and duration in hours for each flight.

Another commonly used command is WHERE. This command filters the rows of the table based on some logical condition you specify. The resulting table contains the rows where your condition is true. For example, if you had a table of students and grades you could do:

SELECT * FROM students
WHERE grade = 'A';
to select all the columns and the rows containing information about students who got As.

#### SQL in a nutshell (2)
Another common database task is aggregation. That is, reducing your data by breaking it into chunks and summarizing each chunk.

This is done in SQL using the GROUP BY command. This command breaks your data into groups and applies a function from your SELECT statement to each group.

For example, if you wanted to count the number of flights from each of two origin destinations, you could use the query

SELECT COUNT(*) FROM flights
GROUP BY origin;
GROUP BY origin tells SQL that you want the output to have a row for each unique value of the origin column. The SELECT statement selects the values you want to populate each of the columns. Here, we want to COUNT() every row in each of the groups.

It's possible to GROUP BY more than one column. When you do this, the resulting table has a row for every combination of the unique values in each column. The following query counts the number of flights from SEA and PDX to every destination airport:

SELECT origin, dest, COUNT(*) FROM flights
GROUP BY origin, dest;
The output will have a row for every combination of the values in origin and dest (i.e. a row listing each origin and destination that a flight flew to). There will also be a column with the COUNT() of all the rows in each group.

Remember, a more in depth look at SQL can be found here.

What information would this query get? Remember the flights table holds information about flights that departed PDX and SEA in 2014 and 2015. Note that AVG() function gets the average value of a column!

SELECT AVG(air_time) / 60 FROM flights
GROUP BY origin, carrier;

#### Filtering Data
Now that you have a bit of SQL know-how under your belt, it's easier to talk about the analogous operations using Spark DataFrames.

Let's take a look at the .filter() method. As you might suspect, this is the Spark counterpart of SQL's WHERE clause. The .filter() method takes either an expression that would follow the WHERE clause of a SQL expression as a string, or a Spark Column of boolean (True/False) values.

For example, the following two expressions will produce the same output:

flights.filter("air_time > 120").show()
flights.filter(flights.air_time > 120).show()
Notice that in the first case, we pass a string to .filter(). In SQL, we would write this filtering task as SELECT * FROM flights WHERE air_time > 120. Spark's .filter() can accept any expression that could go in the WHEREclause of a SQL query (in this case, "air_time > 120"), as long as it is passed as a string. Notice that in this case, we do not reference the name of the table in the string -- as we wouldn't in the SQL request.

In the second case, we actually pass a column of boolean values to .filter(). Remember that flights.air_time > 120 returns a column of boolean values that has True in place of those records in flights.air_time that are over 120, and False otherwise.

Remember, a SparkSession called spark is already in your workspace, along with the Spark DataFrame flights.

* Use the .filter() method to find all the flights that flew over 1000 miles two ways:
	* First, pass a SQL string to .filter() that checks whether the distance is greater than 1000. Save this as long_flights1.
	* Then pass a column of boolean values to .filter() that checks the same thing. Save this as long_flights2.
* Use .show() to print heads of both DataFrames and make sure they're actually equal!
```python
# show flights dataframe

flights.show()
+----+-----+---+--------+---------+--------+---------+-------+-------+------+------+----+--------+--------+----+------+
|year|month|day|dep_time|dep_delay|arr_time|arr_delay|carrier|tailnum|flight|origin|dest|air_time|distance|hour|minute|
+----+-----+---+--------+---------+--------+---------+-------+-------+------+------+----+--------+--------+----+------+
|2014|   12|  8|     658|       -7|     935|       -5|     VX| N846VA|  1780|   SEA| LAX|     132|     954|   6|    58|
|2014|    1| 22|    1040|        5|    1505|        5|     AS| N559AS|   851|   SEA| HNL|     360|    2677|  10|    40|
|2014|    3|  9|    1443|       -2|    1652|        2|     VX| N847VA|   755|   SEA| SFO|     111|     679|  14|    43|
|2014|    4|  9|    1705|       45|    1839|       34|     WN| N360SW|   344|   PDX| SJC|      83|     569|  17|     5|
|2014|    3|  9|     754|       -1|    1015|        1|     AS| N612AS|   522|   SEA| BUR|     127|     937|   7|    54|
|2014|    1| 15|    1037|        7|    1352|        2|     WN| N646SW|    48|   PDX| DEN|     121|     991|  10|    37|
|2014|    7|  2|     847|       42|    1041|       51|     WN| N422WN|  1520|   PDX| OAK|      90|     543|   8|    47|
|2014|    5| 12|    1655|       -5|    1842|      -18|     VX| N361VA|   755|   SEA| SFO|      98|     679|  16|    55|
|2014|    4| 19|    1236|       -4|    1508|       -7|     AS| N309AS|   490|   SEA| SAN|     135|    1050|  12|    36|
|2014|   11| 19|    1812|       -3|    2352|       -4|     AS| N564AS|    26|   SEA| ORD|     198|    1721|  18|    12|
|2014|   11|  8|    1653|       -2|    1924|       -1|     AS| N323AS|   448|   SEA| LAX|     130|     954|  16|    53|
|2014|    8|  3|    1120|        0|    1415|        2|     AS| N305AS|   656|   SEA| PHX|     154|    1107|  11|    20|
|2014|   10| 30|     811|       21|    1038|       29|     AS| N433AS|   608|   SEA| LAS|     127|     867|   8|    11|
|2014|   11| 12|    2346|       -4|     217|      -28|     AS| N765AS|   121|   SEA| ANC|     183|    1448|  23|    46|
|2014|   10| 31|    1314|       89|    1544|      111|     AS| N713AS|   306|   SEA| SFO|     129|     679|  13|    14|
|2014|    1| 29|    2009|        3|    2159|        9|     UA| N27205|  1458|   PDX| SFO|      90|     550|  20|     9|
|2014|   12| 17|    2015|       50|    2150|       41|     AS| N626AS|   368|   SEA| SMF|      76|     605|  20|    15|
|2014|    8| 11|    1017|       -3|    1613|       -7|     WN| N8634A|   827|   SEA| MDW|     216|    1733|  10|    17|
|2014|    1| 13|    2156|       -9|     607|      -15|     AS| N597AS|    24|   SEA| BOS|     290|    2496|  21|    56|
|2014|    6|  5|    1733|      -12|    1945|      -10|     OO| N215AG|  3488|   PDX| BUR|     111|     817|  17|    33|
+----+-----+---+--------+---------+--------+---------+-------+-------+------+------+----+--------+--------+----+------+

# Filter flights by passing a string
long_flights1 = flights.filter("distance > 1000")

# Filter flights by passing a column of boolean values
long_flights2 = flights.filter(flights.distance > 1000)

# Print the data to check they're equal
long_flights1.show()
long_flights2.show()
```

#### Selecting
The Spark variant of SQL's SELECT is the .select() method. This method takes multiple arguments - one for each column you want to select. These arguments can either be the column name as a string (one for each column) or a column object (using the df.colName syntax). When you pass a column object, you can perform operations like addition or subtraction on the column to change the data contained in it, much like inside .withColumn().

The difference between .select() and .withColumn() methods is that .select() returns only the columns you specify, while .withColumn() returns all the columns of the DataFrame in addition to the one you defined. It's often a good idea to drop columns you don't need at the beginning of an operation so that you're not dragging around extra data as you're wrangling. In this case, you would use .select() and not .withColumn().

Remember, a SparkSession called spark is already in your workspace, along with the Spark DataFrame flights.

* Select the columns "origin", "dest", and "carrier" using the df.colName syntax and then filter the result using both of the filters already defined for you (filterA and filterB) to only keep flights from SEA to PDX. Save this as selected2.
```python
# Select the first set of columns
selected1 = flights.select("tailnum", "origin", "dest")

# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)

# Define first filter
filterA = flights.origin == "SEA"

# Define second filter
filterB = flights.dest == "PDX"

# Filter the data, first by filterA then by filterB
selected2 = temp.filter(filterA).filter(filterB)
```

#### Selecting II
Similar to SQL, you can also use the .select() method to perform column-wise operations. When you're selecting a column using the df.colName notation, you can perform any column operation and the .select() method will return the transformed column. For example,

`flights.select(flights.air_time/60)`

returns a column of flight durations in hours instead of minutes. You can also use the .alias() method to rename a column you're selecting. So if you wanted to .select() the column duration_hrs (which isn't in your DataFrame) you could do

`flights.select((flights.air_time/60).alias("duration_hrs"))`

The equivalent Spark DataFrame method .selectExpr() takes SQL expressions as a string:

`flights.selectExpr("air_time/60 as duration_hrs")`

with the SQL as keyword being equivalent to the .alias() method. To select multiple columns, you can pass multiple strings.

* Create a table of the average speed of each flight both ways.
	* Calculate average speed by dividing the distance by the air_time (converted to hours). Use the .alias() method name this column "avg_speed". Save the output as the variable avg_speed.
	* Select the columns "origin", "dest", "tailnum", and avg_speed (without quotes!). Save this as speed1.
	* Create the same table using .selectExpr() and a string containing a SQL expression. Save this as speed2.
```python
# Define avg_speed
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")

# Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)

# Create the same table using a SQL expression
speed2 = flights.selectExpr("origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")
```

#### Aggregating
All of the common aggregation methods, like .min(), .max(), and .count() are GroupedData methods. These are created by calling the .groupBy() DataFrame method. You'll learn exactly what that means in a few exercises. For now, all you have to do to use these functions is call that method on your DataFrame. For example, to find the minimum value of a column, col, in a DataFrame, df, you could do

```df.groupBy().min("col").show()```

This creates a GroupedData object (so you can use the .min() method), then finds the minimum value in col, and returns it as a DataFrame.

* Find the length of the shortest (in terms of distance) flight that left PDX by first .filter()ing and using the .min() method. Perform the filtering by referencing the column directly, not passing a SQL string.
* Find the length of the longest (in terms of time) flight that left SEA by filter()ing and using the .max() method. Perform the filtering by referencing the column directly, not passing a SQL string.
```python
# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()

# Find the longest flight from SEA in terms of air time
flights.filter(flights.origin == "SEA").groupBy().max("air_time").show()
```

#### Aggregating II
To get you familiar with more of the built in aggregation methods, here's a few more exercises involving the flights table!

Remember, a SparkSession called spark is already in your workspace, along with the Spark DataFrame flights.

* Use the .avg() method to get the average air time of Delta Airlines flights (where the carrier column has the value "DL") that left SEA. The place of departure is stored in the column origin. show() the result.
* Use the .sum() method to get the total number of hours all planes in this dataset spent in the air by creating a column called duration_hrs from the column air_time. show() the result.
```python
# Average duration of Delta flights
flights.filter(flights.carrier == "DL").filter(flights.origin == "SEA").groupBy().avg("air_time").show()

# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()
```

#### Grouping and Aggregating I
Part of what makes aggregating so powerful is the addition of groups. PySpark has a whole class devoted to grouped data frames: pyspark.sql.GroupedData, which you saw in the last two exercises.

You've learned how to create a grouped DataFrame by calling the .groupBy() method on a DataFrame with no arguments.

Now you'll see that when you pass the name of one or more columns in your DataFrame to the .groupBy() method, the aggregation methods behave like when you use a GROUP BY statement in a SQL query!

Remember, a SparkSession called spark is already in your workspace, along with the Spark DataFrame flights.

* Create a DataFrame called by_plane that is grouped by the column tailnum.

* Use the .count() method with no arguments to count the number of flights each plane made.

* Create a DataFrame called by_origin that is grouped by the column origin.

* Find the .avg() of the air_time column to find average duration of flights from PDX and SEA.
```python
# Group by tailnum
by_plane = flights.groupBy("tailnum")

# Number of flights each plane made
by_plane.count().show()

# Group by origin
by_origin = flights.groupBy("origin")

# Average duration of flights from PDX and SEA
by_origin.avg("air_time").show()
```

#### Grouping and Aggregating II
In addition to the GroupedData methods you've already seen, there is also the .agg() method. This method lets you pass an aggregate column expression that uses any of the aggregate functions from the pyspark.sql.functions submodule.

This submodule contains many useful functions for computing things like standard deviations. All the aggregation functions in this submodule take the name of a column in a GroupedData table.

Remember, a SparkSession called spark is already in your workspace, along with the Spark DataFrame flights. The grouped DataFrames you created in the last exercise are also in your workspace.

* Import the submodule pyspark.sql.functions as F.

* Create a GroupedData table called by_month_dest that's grouped by both the month and dest columns. Refer to the two columns by passing both strings as separate arguments.

* Use the .avg() method on the by_month_dest DataFrame to get the average dep_delay in each month for each destination.

* Find the standard deviation of dep_delay by using the .agg() method with the function F.stddev().
```python
# Import pyspark.sql.functions as F
import pyspark.sql.functions as F

# Group by month and dest
by_month_dest = flights.groupBy("month", "dest")

# Average departure delay by month and destination
by_month_dest.avg("dep_delay").show()

# Standard deviation of departure delay
by_month_dest.agg(F.stddev("dep_delay")).show()
```

#### Joining
Another very common data operation is the join. Joins are a whole topic unto themselves, so in this course we'll just look at simple joins. If you'd like to learn more about joins, you can take a look here.

A join will combine two different tables along a column that they share. This column is called the key. Examples of keys here include the tailnum and carrier columns from the flights table.

For example, suppose that you want to know more information about the plane that flew a flight than just the tail number. This information isn't in the flights table because the same plane flies many different flights over the course of two years, so including this information in every row would result in a lot of duplication. To avoid this, you'd have a second table that has only one row for each plane and whose columns list all the information about the plane, including its tail number. You could call this table planes

When you join the flights table to this table of airplane information, you're adding all the columns from the planes table to the flights table. To fill these columns with information, you'll look at the tail number from the flights table and find the matching one in the planes table, and then use that row to fill out all the new columns.

Now you'll have a much bigger table than before, but now every row has all information about the plane that flew that flight!

#### Joining II
In PySpark, joins are performed using the DataFrame method .join(). This method takes three arguments. The first is the second DataFrame that you want to join with the first one. The second argument, on, is the name of the key column(s) as a string. The names of the key column(s) must be the same in each table. The third argument, how, specifies the kind of join to perform. In this course we'll always use the value how="leftouter".

The flights dataset and a new dataset called airports are already in your workspace.

* Examine the airports DataFrame by calling .show(). Note which key column will let you join airports to the flights table.
* Rename the faa column in airports to dest by re-assigning the result of airports.withColumnRenamed("faa", "dest") to airports.
* Join the flights with the airports DataFrame on the dest column by calling the .join() method on flights. Save the result as flights_with_airports.
* The first argument should be the other DataFrame, airports.
	* The argument on should be the key column.
	* The argument how should be "leftouter".
* Call .show() on flights_with_airports to examine the data again. Note the new information that has been added.
```python
airports.show()
+----+--------------------+----------------+-----------------+----+---+---+
|dest|                name|             lat|              lon| alt| tz|dst|
+----+--------------------+----------------+-----------------+----+---+---+
| 04G|   Lansdowne Airport|      41.1304722|      -80.6195833|1044| -5|  A|
| 06A|Moton Field Munic...|      32.4605722|      -85.6800278| 264| -5|  A|
| 06C| Schaumburg Regional|      41.9893408|      -88.1012428| 801| -6|  A|
| 06N|     Randall Airport|       41.431912|      -74.3915611| 523| -5|  A|
| 09J|Jekyll Island Air...|      31.0744722|      -81.4277778|  11| -4|  A|
| 0A9|Elizabethton Muni...|      36.3712222|      -82.1734167|1593| -4|  A|
| 0G6|Williams County A...|      41.4673056|      -84.5067778| 730| -5|  A|
| 0G7|Finger Lakes Regi...|      42.8835647|      -76.7812318| 492| -5|  A|
| 0P2|Shoestring Aviati...|      39.7948244|      -76.6471914|1000| -5|  U|
| 0S9|Jefferson County ...|      48.0538086|     -122.8106436| 108| -8|  A|
| 0W3|Harford County Ai...|      39.5668378|      -76.2024028| 409| -5|  A|
| 10C|  Galt Field Airport|      42.4028889|      -88.3751111| 875| -6|  U|
| 17G|Port Bucyrus-Craw...|      40.7815556|      -82.9748056|1003| -5|  A|
| 19A|Jackson County Ai...|      34.1758638|      -83.5615972| 951| -4|  U|
| 1A3|Martin Campbell F...|      35.0158056|      -84.3468333|1789| -4|  A|
| 1B9| Mansfield Municipal|      42.0001331|      -71.1967714| 122| -5|  A|
| 1C9|Frazier Lake Airpark|54.0133333333333|-124.768333333333| 152| -8|  A|
| 1CS|Clow Internationa...|      41.6959744|      -88.1292306| 670| -6|  U|
| 1G3|  Kent State Airport|      41.1513889|      -81.4151111|1134| -4|  A|
| 1OH|     Fortman Airport|      40.5553253|      -84.3866186| 885| -5|  U|
+----+--------------------+----------------+-----------------+----+---+---+

# Examine the data
airports.show()

# Rename the faa column
airports = airports.withColumnRenamed("faa", "dest")

# Join the DataFrames
flights_with_airports = flights.join(airports, on="dest", how="leftouter")

# Examine the new DataFrame
flights_with_airports.show()
```
