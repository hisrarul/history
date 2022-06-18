## Functools

* Higher order functions and operations
* Returns a function or take another function as an argument
    * `reduce()`: reducing iterable to a single cumulative value
        values = [10, 2, 21, 7, 1, 9, 15]
        It is similar to accumulate function where it will try to reduce to 65.
    * `lru_cache()`: memoizing callable and returns the stored value
        e.g. building a function to calculate factorial
        1! = 1
        2! = 1*2
        3! = 1*2*3
        4! = 1*2*3*4
        We can see that there is a repetition of calculation i.e. 1*2. Now, if it has already calculate 1*2*3 then it will not calculate it again. In such cases, it save computation and make operation faster.
        `lru_cache` can store input and output values which are frequently used later in the program.
    
    * partial(): returs partial function which freezes some arguments of a function.

#### Jupyter labs
Applying a two argument function (from left to right) to the first two items of the iterable object.
```python
import functools

amount = [1100, 2450, 1330, 900]

# syntax --> reduce(function, iterable)
functools.reduce(lambda a, b: a + b, amount)
```

We can insert any function here:
```python
def calculate_prod(x, y):
    return x * y

functools.reduce(calculate_prod, amount)
```

```python
data = ["Python", "Advanced", "Programming"]

functools.reduce(lambda a, b: a + " " + b, data)
```

#### lru_cache()
Memorizing callable and returns the stored value if the function is called with the same arguments again. It can save time when an expensive or I/O bound function is periodically called with the same arguments.

```python
# function without lru_cache
def calc_uncached_factorial(n):
    if n <= 1:
        return 1
    return n * calc_uncached_factorial(n - 1)
```

```python
# evaluate the performance of the unached function
%timeit calc_uncached_factorial(10)
```

```python
# function with lru_cache
@functools.lru_cache(maxsize=None)
def calc_uncached_factorial(n):
    if n <= 1:
        return 1
    return n * calc_uncached_factorial(n - 1)
```

```python
# evaluate the performance of the unached function
%timeit calc_uncached_factorial(10)
```

Note: LRU cache should only be used when you want to reuse previously computed values.

#### Partial()
Used for partial function application which "freeze" some portion of a function's arguments

```python
# initial function
def calc_total_saving(a, b, c, x):
    return a + b + c + x

# partial function that a,b,c fixed
part_func = functools.partial(calc_total_saving, 30000, 250000, 400000)

part_func(100000)
```

#### Application: functools
Broadcating Function in Pytorch Library

```python
# Check whether the op enable broadcasting, and whether it is supported by ONNX
# If dims1 and dims2 are different, then broadcast is True
# We always assume the combination of dims1 and dims2 is broadcastable.
# The following types of broadcasting are supported by ONNX:
#     1) Only one element in dims2 such as dims2 = [1, 1]
#     2> dims2 is suffix of dims1, such as dims1 = [2, 3, 4] and dims2 = [3, 4]
# Details can be found here: https://github.com/onnx/onnx/blob/main/docs/Operators.md#Gemm
def check_onnx_broadcast(dims1, dims2):
    broadcast = False
    supported = True
    len1 = len(dims1)
    len2 = len(dims2)
    numel1 = reduce(lambda x, y: x * y, dims1)
    numel2 = reduce(lambda x, y: x * y, dims2)
    if len1 < len2:
        broadcast = True
        if numel2 != 1:
            supported = False
        elif len1 > len2:
            broadcast = True
            if numel2 != 1 and dims1[len1 - len2] != dims2:
                supported = False
        else:
            if dims1 != dims2:
                broadcast = True
                if numel2 != 1:
                    supported = False
```

#### Applications 2: functools
```python
@functools.lru_cache()
def logging_base_dir() -> str:
    meta_dir = os.getcwd()
    base_dir = os.path.join(meta_dir, "nightly", "log")
    os.makedirs(base_dir, exist_ok=True)
    return base_dir

@functools.lru_cache()
def logging_run_dir() -> str:
    cur_dir = os.path.join(
        logging_base_dir(),
        "{}_{}".format(datetime.datetime.now().strftime(DATETIME_FORMAT), uuid.uuid1()),
    )
    os.makedirs(cur_dir, exist_ok=True)
    return cur_dir
```

#### Application 3: functools
In this example, the density is fixed and matrix value is changing.
```python
def test_basic_property_of_sparse_random_matrix(random_matrix):
    check_input_with_sparse_random_matrix(random_matrix)
    random_matrix_dense = functools.partial(random_matrix, density=1.0)
    check_zero_mean_and_unit_norm(random_matrix_dense)
```


