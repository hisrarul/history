## Object Oriented Programming

* Group all the data and code with a single structure (Class)
* All data is stored as Classes and objects
* Modular and Organised code
* Easier to reuse code and reduces redundant code blocks
* Follows a Bottom-Up approach
* A program can have multiple classes.

#### Question: Difference between instance variables and instance attributes
* Instance variables are the variable names and instance attributes are value assigned to the instance variable

#### Class and Object
In python, class can be created using `class` keyword.

```python
%load_ext lab_black

# defining a class called 'Cars'
class Cars:

    # defining instance variables
    def __init__(self, number, fuel_type, capacity, torque):

        # initialize instance attributes
        self.number = number
        self.fuel_type = fuel_type
        self.capacity = capacity
        self.torque = torque
    
# create object or instance (car_1) of class Cars
car_1 = Cars("RJ06 1719", "Petrol", "35 Litres", 200)
car_1.fuel_type
```

#### Self attribute (__init__)
* When you create a new object of a class, Python automatically calls the __init__() method to initialize the object's attributes.



