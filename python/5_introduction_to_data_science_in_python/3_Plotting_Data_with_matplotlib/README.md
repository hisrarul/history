## Creating line plots

#### From DataFrame to Visualization
| letter_index      | letter | frequency     |
| :---        |    :----:   |          ---: |
| 1      | A       | 7.38   |
| 2   | B        | 1.09      |
| 3      | C       | 2.46   |
| 4   | D        | 4.10      |

#### Introducing Matplotlib
```python
from matplotlib import pyplot as plt
plt.plot(x_values, y_values)
plt.show()

# plt
plt.plot(dataframe.column_name_1, dataframe.column_name_2)

# Multiple lines
plt.plot(data1.x_values, data1.y_values)

plt.plot(data2.x_values, data2.y_values)

plt.show()
```

#### Adding text to plots
```python
plt.xlabel("Letter")

plt.ylabel("Frequency")

plt.title("Ransom Note Letters")

# Label anywhere before
plt.show()
```

#### Legends
```python
plt.plot(aditya.days, aditya.cases, label="Aditya")

plt.plot(deshaun.days, deshaun.cases, label="Deshaun")

plt.plot(mengfei.days, mengfei.cases, label="Mengfei")

plt.legend()
```

#### Arbitrary text
```python
plt.text(xcoord, ycoord, "Text Message")
plt.text(5, 9, "Unusually low H frequency")
```

#### Modifying text
* Changing the font size
```python
plt.title("Plot title", fontsize = 20)
```
* Change font color
```python
plt.legend(color="green")
```

#### Exercise: Adding floating text
Officer Deshaun is examining the number of hours that he worked over the past six months. The number for June is low because he only had data for the first week. Help Deshaun add an annotation to the graph to explain this.
```python
# Create plot
plt.plot(six_months.month, six_months.hours_worked)

# Add annotation "Missing June data" at (2.5, 80)

# plt.annotate("Missing June data", xy=(2.5, 80))

plt.text(2.5, 80, "Missing June data")

# Display graph
plt.show()
```

#### Styling graphs
```python
# Changing the color
plt.plot(x, y1, color="tomato")
plt.plot(x, y1, color="orange")

# Changing line width
plt.plot(x, y1, linewidth=2)

# Changing line style
plt.plot(x, y1, linestyle='-')
plt.plot(x, y1, linestyle='--')
plt.plot(x, y1, linestyle='-.')
plt.plot(x, y1, linestyle=':')

# Adding markers
plt.plot(x, y1, marker='x')
plt.plot(x, y1, marker='s')
plt.plot(x, y1, marker='o')
plt.plot(x, y1, marker='d')
plt.plot(x, y1, marker='*')
plt.plot(x, y1, marker='h')

# Setting a style
plt.style.use('fivethirtyeight')
plt.style.use('ggplot')
plt.style.use('seaborn')
plt.style.use('default')
```

#### Exercise: Tracking crime statistics
Sergeant Laura wants to do some background research to help her better understand the cultural context for Bayes' kidnapping. She has plotted Burglary rates in three U.S. cities using data from the Uniform Crime Reporting Statistics.

She wants to present this data to her officers, and she wants the image to be as beautiful as possible to effectively tell her data story.

Recall:

You can change linestyle to dotted (':'), dashed('--'), or no line ('').
You can change the marker to circle ('o'), diamond('d'), or square ('s').

* Change the color of Phoenix to "DarkCyan".
* Make the Los Angeles line dotted.
* Add square markers to Philadelphia.
```python
# Change the color of Phoenix to `"DarkCyan"`
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix", color="DarkCyan")

# Make the Los Angeles line dotted
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle=":")

# Add square markers to Philedelphia
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker="s")

# Add a legend
plt.legend()

# Display the plot
plt.show()
```

#### Exercise: Identifying Bayes' kidnapper
We've narrowed the possible kidnappers down to two suspects:

Fred Frequentist (suspect1)
Gertrude Cox (suspect2)
The kidnapper left a long ransom note containing several unusual phrases. Help DataCamp by using a line plot to compare the frequency of letters in the ransom note to samples from the two main suspects.

Three DataFrames have been loaded:

ransom contains the letter frequencies for the ransom note.
suspect1 contains the letter frequencies for the sample from Fred Frequentist.
suspect2 contains the letter frequencies for the sample from Gertrude Cox.
Each DataFrame contain two columns letter and frequency.
* Plot the letter frequencies from the ransom note. The x-values should be ransom.letter. The y-values should be ransom.frequency. The label should be the string 'Ransom'. The line should be dotted and gray.
```python
# dataframe
print(ransom)
    Unnamed: 0  letter_index letter  frequency identity
0            0             1      A       7.38   Ransom
1            1             2      B       1.09   Ransom
2            2             3      C       2.46   Ransom
3            3             4      D       4.10   Ransom
4            4             5      E      12.84   Ransom
5            5             6      F       1.37   Ransom
6            6             7      G       1.09   Ransom
7            7             8      H       3.55   Ransom
8            8             9      I       7.65   Ransom
9            9            10      J       0.00   Ransom
10          10            11      K       3.01   Ransom
11          11            12      L       3.28   Ransom
12          12            13      M       2.46   Ransom
13          13            14      N       7.38   Ransom
14          14            15      O       6.83   Ransom
15          15            16      P       7.65   Ransom
16          16            17      Q       0.00   Ransom
17          17            18      R       4.92   Ransom
18          18            19      S       4.10   Ransom
19          19            20      T       6.28   Ransom
20          20            21      U       4.37   Ransom
21          21            22      V       1.09   Ransom
22          22            23      W       2.46   Ransom
23          23            24      X       0.00   Ransom
24          24            25      Y       4.64   Ransom
25          25            26      Z       0.00   Ransom

# x should be ransom.letter and y should be ransom.frequency
plt.plot(ransom.letter, ransom.frequency,
         # Label should be "Ransom"
         label="Ransom",
         # Plot the ransom letter as a dotted gray line
         linestyle=':', color='gray')

# Display the plot
plt.show()
```

* Plot a line for the data in suspect1. Use a keyword argument to label that line 'Fred Frequentist').
```python
# dataframe
    Unnamed: 0  letter_index letter  frequency   identity
26           0             1      A       7.24  Suspect 1
27           1             2      B       0.01  Suspect 1
28           2             3      C       3.03  Suspect 1
29           3             4      D       4.04  Suspect 1
30           4             5      E      13.49  Suspect 1
31           5             6      F       1.97  Suspect 1
32           6             7      G       0.64  Suspect 1
33           7             8      H       3.02  Suspect 1
34           8             9      I       7.66  Suspect 1
35           9            10      J       0.01  Suspect 1
36          10            11      K       2.98  Suspect 1
37          11            12      L       4.28  Suspect 1
38          12            13      M       2.25  Suspect 1
39          13            14      N       9.28  Suspect 1
40          14            15      O       7.57  Suspect 1
41          15            16      P       8.41  Suspect 1
42          16            17      Q       0.01  Suspect 1
43          17            18      R       4.04  Suspect 1
44          18            19      S       4.53  Suspect 1
45          19            20      T       5.04  Suspect 1
46          20            21      U       2.37  Suspect 1
47          21            22      V       1.03  Suspect 1
48          22            23      W       2.32  Suspect 1
49          23            24      X       0.95  Suspect 1
50          24            25      Y       3.05  Suspect 1
51          25            26      Z       0.79  Suspect 1

# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')

# X-values should be suspect1.letter
# Y-values should be suspect1.frequency
# Label should be "Fred Frequentist"
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')

# Display the plot
plt.show()
```

* Plot a line for the data in suspect2 (labeled 'Gertrude Cox').
```python
# dataframe
print(suspect2)
    Unnamed: 0  letter_index letter  frequency   identity
52           0             1      A      8.167  Suspect 2
53           1             2      B      1.492  Suspect 2
54           2             3      C      2.782  Suspect 2
55           3             4      D      4.253  Suspect 2
56           4             5      E     12.702  Suspect 2
57           5             6      F      2.228  Suspect 2
58           6             7      G      2.015  Suspect 2
59           7             8      H      6.094  Suspect 2
60           8             9      I      6.966  Suspect 2
61           9            10      J      0.153  Suspect 2
62          10            11      K      0.772  Suspect 2
63          11            12      L      4.025  Suspect 2
64          12            13      M      2.406  Suspect 2
65          13            14      N      6.749  Suspect 2
66          14            15      O      7.507  Suspect 2
67          15            16      P      1.929  Suspect 2
68          16            17      Q      0.095  Suspect 2
69          17            18      R      5.987  Suspect 2
70          18            19      S      6.327  Suspect 2
71          19            20      T      9.056  Suspect 2
72          20            21      U      2.758  Suspect 2
73          21            22      V      0.978  Suspect 2
74          22            23      W      2.360  Suspect 2
75          23            24      X      0.150  Suspect 2
76          24            25      Y      1.974  Suspect 2
77          25            26      Z      0.074  Suspect 2

# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency,
         label='Fred Frequentist')

# X-values should be suspect2.letter
# Y-values should be suspect2.frequency
# Label should be "Gertrude Cox"
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')

# Display plot
plt.show()
```

* Label the x-axis (Letter) and the y-axis (Frequency), and add a legend.
```python
# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')

# Add x- and y-labels
plt.xlabel("Letter")
plt.ylabel("Frequency")

# Add a legend
plt.legend()

# Display plot
plt.show()
```