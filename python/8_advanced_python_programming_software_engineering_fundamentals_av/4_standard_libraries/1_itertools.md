## Python standard library: Itertools

* Collection of functions creating iterators for efficient looping
* Some of the popularly used functions are:
    * `filterfalse()` returns elements of seq where condition is false
    * `permutation()`: returns all possible orderings
    * `accumulate()`: returns accumulated results

#### filterfalse
Make an iterator that filters elements from iterable returning only those for which the predicate is False.

Income values:
| 10,000 | 22,100 | 12,000 | 7000 | 15000 | 90,000 | 45,000 |

Condition: Income < 20,000

It will give the output which will not met the condition.
Filterfalse Output: [22100, 90000, 45000]

```python
# income values for a set of people
income = [20000, 50000, 440000, 72000, 18000]

# using for loop
result = []
for i in income:
    if i >= 50000:
        result.append(i)
```

```python
# using itertools
results = itertools.filterfalse(lambda x: x < 50000, income)
list(results)
```

#### permutation / product()
Make an iterator that returns all possible combination of elements.

Different Cities
| Noida | Gurugram | Delhi | Agra |

Find all the combination of cities given the start and destination. For eg with 2 cities (N-G) or with 3 cities (N-G-D)

Start - Destination
Permutation (repeat = 2): N-G, N-D, N-A, G-N, G-D, G-A
Permutation (repeat = 3): N-G-D, N-G-A, N-D-A, N-D-G

```python
A = ['Jazz', 'Spurs', 'Warriors']
a_product = list(itertools.product(A, repeat=2))
a _product
```

```python
A = ['Jazz', 'Spurs', 'Warriors']
B = ['Nets', 'Bucks']
ab_product = list(itertools.product(A, B))
ab_product
```

#### accumulate
Make an iterator that returns accumulated sums, or accumulated results of specified function

```python
data = [5, 2, 6, 4, 5, 9, 1]

# using itertools
list(itertools.accumulate(data))
```

#### Other functions
| Examples | Results |
| product('ABCD', repeat =2) | AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD |
| permutation('ABCD', 2) | AB AC AD BA BC BD CA CB CD DA DB DC |
| combinations('ABCD', 2) | AB AC AD BC BD CD |
| combinations_with_replacement('ABCD', 2) | AA AB AC AD BB BC BD CC CD DD |


#### Applications 1: itertools
An end-to-end project on time series analysis and forecasting

<h4>Time series forecasting with ARIMA</h4>
We are going to apply one of the most commonly used method for time series forecasting known as ARIMA which stands for autoregressive integrated moving average.

ARIMA models are denoted with the notation *ARIMA(p, d, q)*. These three parameters acccount for seasonality, trend, and noise in data:

```python
p = d = q = range(0, 2)     #3 hyperparameters
pdq = list(itertools.product(p, d, q))    # calc all possible combination of p, d and q using product func
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA')
print('SARIMAX: {} x {}'.format(pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2]))
```

#### Applications: itertools
Pytorch graph module

```python
if node.op == "call_module" or node.op == "get_attr":
    # A list of strings representing the different parts
    # of the path. For e.g. `foo.bar.baz` gives us
    # ["foo", "bar", "baz"]
    fullpath = node.target.split(".")

    # if we're looking at multiple parts of a path, join
    # join them with a dot. Otherwise, return that single
    # element without doing anything to it.

    def join_fn(x: str, y: str) -> str:
        return '.'.join([x, y] if y else [x])

    # Progressively college all the names of intermediate
    # modules. For example, if we have the target
    # `foo.bar.baz`, we'll add `foo`, `foo.bar` and
    # `foo.bar.baz` to the list

    for path in itertools.accumulate(fullpath, join_fn):
        used.append(path)
```