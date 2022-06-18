## Naming Conventions

* Using relevant variable names
* Numbers are never used by themselves 
* How to be meaningful: Variable
    * Characteristic or Property?
        ```python
        def slow_down(current_speed):
            if current_speed > 5:
                return current_speed - 5
            else:
                return 0
        ```
    * What is being stored in that variable?
        ```python
        def factorial(value):
            final_factorial = 1
            for number in range(1, value+1):
                final_factorial = final_factorial * number
            return final_factorial
        ```
    * Part of expression as numerator or denominator.
        ```python
        def t_statustic(mu1, mu2, sig1, sig2, n1, n2):
            t_numerator = mu1 - mu2
            t_denominator = ((s1**2)/n1 + (s2**2)/n2) ** 0.5
            return t_numerator/t_denominator
        ```
* How to be meaningful: Functions
    * Verb: if mutating the inputs
        ```python
        def removing_gaussian_outliers(data, n_std):
            avg, std = data.mean(), data.std()
            return data[(data < (avg + (n_std*std))) & (data > (avg - (n_std*std)))]
        ```
    * Noun: no mutation happens
        ```python
        def num_outlier(data, criteria='gaussian', n=3):
            if criteria =="gaussian":
                low = len(data[data < (data.mean() - (n*data.std()))])
                high = len(data[data > (data.mean() + (n*data.std()))])
                tot = low+high
                return low, high,  tot
            
            elif criteria == 'whisker':
                low = len(data[data < data.quantile(0.25)-(1.5*(data.quantile(0.75)-data.quantile(0.25)))])
                high = len(data[data > data.quantile(0.75) +  (1.5 *(data.quantile(0.75)-data.quantile(0.25)))])
                tot = low+high
                return low, high, tot
        ```
#### Naming Functions and Variables
* Variables and Functions are named similarly
* Function_name, VariableName: Not recommended
* function_name, variableName: recommended
* Constants are declared using uppercase
    