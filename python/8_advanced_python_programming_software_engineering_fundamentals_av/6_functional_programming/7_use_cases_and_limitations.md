## Use cases and limitations of functional programming

Uses:
* Geared towards mathematics expressions
* Suitable for machine learning
* Function-Centric, functions are first class citizens
* Promotes optimization in the execution of code
* Promotes lazy evaluation of code.
* Defining neutral networks since neural network can be elaborated computational graph
* Big data pipeline since big data pipeline could include fetching data from multiple sources, under different transmission. There is a huge scope for parallelisation of these transformation across the multiple processors. Thus making computation efficient.
* Machine learning pipelines

Limitations:
* Python merely supports functional programming
* No parallelisation in pure python
* Since no optimization graph, Recursion is expensive

So why using python for functional programming
* Tensorflow, Pytorch(C++, Lua provides optimisation)
* Pyspark (Scala provides optimisation)

#### Question: Is python able to take advantage of functional programming?
No, since Python does not allow multiprocessing by itself, therefore functional programming is not beneficial in Python by itself.
