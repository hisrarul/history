## Different Types of Plots

#### Making a scatter plot
```python
plt.scatter(df.age, df.height)

plt.xlabel('Age (in months')
plt.ylabel('Height (in inches)')

plt.show()

# keyword arguments
plt.scatter(df.age, df.height, color='green', marker='s')

# changing marker transparency
plt.scatter(df.x_data, df.y_data, alpha=0.1)
```

#### Exercise: Charting cellphone data
We know that Freddy Frequentist is the one who kidnapped Bayes the Golden Retriever. Now we need to learn where he is hiding.

Our friends at the police station have acquired cell phone data, which gives some of Freddie's locations over the past three weeks. It's stored in the DataFrame cellphone. The x-coordinates are in the column 'x' and the y-coordinates are in the column 'y'.

The matplotlib module has been imported under the alias plt.

* Display the first five rows of the DataFrame and determine which columns to plot
* Create a scatter plot of the data in cellphone.
```python
print(cellphone)
      Unnamed: 0           x          y
0              0   28.136519  39.358650
1              1   44.642131  58.214270
2              2   34.921629  42.039109
3              3   31.034296  38.283153
4              4   36.419871  65.971441
5              5   47.753390  32.368487
6              6   17.547226  61.427741
7              7   51.042230  54.128275
8              8   52.381297  58.634855
9              9   48.603323  31.903506
10            10   23.617035  53.454882
11            11   30.820994  74.304990
12            12   56.469151  42.933859
13            13   64.155852  49.071143
14            14    9.454737  63.815709
15            15   43.196988  64.477585
16            16   41.953967  69.860938
17            17   62.048784  54.023277
18            18   41.040148  53.347365
19            19   40.687668  42.136996
20            20   24.733568  47.016831
21            21   37.834816  33.076629
22            22   56.627763  59.305950
23            23   16.595418  60.329872
24            24   42.683366  48.364455
25            25   43.329045  67.829819
26            26   24.879793  57.458169
27            27   37.371988  46.554562
28            28   48.192002  69.054392
29            29   19.699196  49.575103
...          ...         ...        ...
5970        5970   78.556912  70.616885
5971        5971   94.866579  70.572275
5972        5972   61.477313  64.906872
5973        5973   68.269081  48.244643
5974        5974   76.830515  60.083930
5975        5975   71.213079  51.501263
5976        5976   67.797364  72.141596
5977        5977   84.775554  57.727075
5978        5978   72.195754  74.759540
5979        5979   76.188414  48.701758
5980        5980   49.573288  79.248780
5981        5981   91.225878  84.590906
5982        5982   96.916408  62.901599
5983        5983   83.033405  82.352978
5984        5984   74.079877  50.622003
5985        5985  103.935389  64.735322
5986        5986   85.921113  55.048755
5987        5987   99.814886  42.055751
5988        5988   59.457974  63.795269
5989        5989   64.453959  62.135542
5990        5990   63.826069  74.532680
5991        5991   89.128920  52.280483
5992        5992  105.782603  63.614850
5993        5993   79.312178  75.710945
5994        5994   89.911392  55.985041
5995        5995   89.504755  50.933208
5996        5996   90.501140  73.148402
5997        5997   95.042642  56.907865
5998        5998   86.683062  63.580406
5999        5999   67.694722  72.967664

# Explore the data
print(cellphone.head())

# Create a scatter plot of the data from the DataFrame cellphone
plt.scatter(cellphone.x, cellphone.y)

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()
```

#### Making a bar chart
|precinct|pets_abducted|
|--------|-------------|
|Farmburg|10|
|Cityvile|15|
|Saburbia|9|

```python
# Vertical bar
plt.bar(df.precinct, df.pets_abducted)
plt.ylabel('Pet Abductions')
plt.show()

# Horizontal bar
plt.barh(df.precinct, df.pets_abducted)
plt.ylabel('Pet Abductions')
plt.show()

# Adding error bars
plt.bar(df.precinct, df.pets_abducted, yerr=df.error)
plt.ylabel('Pet Abductions')
plt.show()
```

#### Stacked bar charts
* Display total number in bar
```python
plt.bar(df.percinct, df.dog)

# dog at bottom
plt.bar(df.percinct, df.cat, bottom=df.dog)
plt.bar(df.percinct, df.dog)

# label
plt.bar(df.precinct, df.dog, label='Dog')
plt.bar(df.precinct, df.cat, label='Cat')
plt.legend()
plt.show()
```

#### Exercise: Build a simple bar chart
Officer Deshaun wants to plot the average number of hours worked per week for him and his coworkers. He has stored the hours worked in a DataFrame called hours, which has columns officer and avg_hours_worked. Recall that the function plt.bar() takes two arguments: the labels for each bar, and the height of each bar. Both of these can be found in our DataFrame.

* Create a bar chart of the column avg_hours_worked for each officer from the DataFrame hours.
```python
# dataframe hours
    officer  avg_hours_worked  std_hours_worked
0  Deshaun                45                 3
1  Mengfei                33                 9
2   Aditya                42                 5

# Display the DataFrame hours using print
print(hours)

# Create a bar plot from the DataFrame hours
plt.bar(hours.officer, hours.avg_hours_worked)

# Display the plot
plt.show()
```

* Use the column `std_hours_worked` (the standard deviation of the hours worked) to add error bars to the bar chart.
```python
# Display the DataFrame hours using print
print(hours)

# Create a bar plot from the DataFrame hours
plt.bar(hours.officer, hours.avg_hours_worked,
        # Add error bars
        yerr=hours.std_hours_worked)

# Display the plot
plt.show()
```

#### Making a histogram
A histogram visualizes the distribution of values in a dataset. To create a histogram, we place each piece of data into a bin. In this example, we have divided our data into four bins: 1 - 10 mm, 11 - 20 mm, 21 - 30 mm, and 31 - 40 mm. The histogram tells us how many pieces of data (or pieces of gravel) fall into each of those bins.
```python
# histogram with matplotlib
plt.hist(gravel.mass)

plt.show()

# Changing bins
plt.hist(data, bins=nbins)
plt.hist(gravel.mass, bins=40)

plt.hist(data, range=(xmin, xmax))
plt.hist(gravel.mass, range=(50, 100))
```

#### Normalizing
* Unnormalized bar plot
```python
plt.hist(male_weight)
plt.hist(female_weight)
```

* Sum of bar area = 1
```python
plt.hist(male_weight, density=True)
plt.hist(female_weight, density=True)
```

#### Exercise: Modifying histograms
Let's explore how changes to keyword parameters in a histogram can change the output. Recall that:

range sets the minimum and maximum datapoints that we will include in our histogram.
bins sets the number of points in our histogram.
We'll be exploring the weights of various puppies from the DataFrame puppies. matplotlib has been loaded under the alias plt.
* Create a histogram of the column weight from the DataFrame puppies.
```python
# datafram of puppies
print(puppies)
        weight     breed
0     9.791698       pug
1    11.698426       pug
2     5.988439   pitbull
3    14.200483    poodle
4    17.199590    poodle
5    30.568480  labrador
6    10.352059       pug
7    41.208306    poodle
8    31.434719  labrador
9    32.700659  labrador
10   11.974843       pug
11   14.989869    poodle
12   50.304485    poodle
13   22.370633    poodle
14   50.116002   pitbull
15   23.194739       pug
16   11.827824    poodle
17   33.664047  labrador
18   10.148582   pitbull
19   42.845698    poodle
20   16.680948  labrador
21   41.154044    poodle
22   20.915376  labrador
23   47.615408       pug
24   44.057144       pug
25   14.410642       pug
26   26.392809       pug
27   28.926925  labrador
28   19.203344  labrador
29    9.058862   pitbull
..         ...       ...
970  14.831229   pitbull
971  27.329951  labrador
972  20.861557    poodle
973  12.090609  labrador
974  25.719396    poodle
975  22.941661       pug
976  43.269264    poodle
977  24.567219  labrador
978  11.429526   pitbull
979  48.464511  labrador
980  24.087777       pug
981   6.641902   pitbull
982  11.858043  labrador
983  29.322764   pitbull
984  26.292346    poodle
985  32.553864       pug
986  40.095147       pug
987  12.181510   pitbull
988   7.796300       pug
989   7.861745   pitbull
990  25.994989   pitbull
991   7.893405    poodle
992  18.296132    poodle
993  13.342466   pitbull
994  22.398066    poodle
995  12.249446   pitbull
996  12.749816    poodle
997  45.315652   pitbull
998  21.959184    poodle
999  22.997926   pitbull

# Create a histogram of the column weight
# from the DataFrame puppies
plt.hist(puppies.weight)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()
```

* Change the number of bins to 50.
```python
# Change the number of bins to 50
plt.hist(puppies.weight,
        bins=50)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()
```

* Change the range to start at 5 and end at 35.
```python
# Change the range to start at 5 and end at 35
plt.hist(puppies.weight,
        range=(5, 35))

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()
```