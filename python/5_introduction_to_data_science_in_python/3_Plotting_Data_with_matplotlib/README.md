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
