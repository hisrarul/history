## Methods and its Types

* Methods are functions associated with classes
* Methods are functions defined within a class in OOP.

Power (KW) = Torque(Nm) * Speed(RPM) / 9550

```python
# defining a method to calculate power
def power_calc(self):
    return (self.torque * self.speed)/9550
```

#### 2.1 Regular Methods
```python
# defining a class called 'Cars'
class Cars:

    # defining class variable and attribute
    speed_rpm = 1800

    # defining instance variables
    def __init__(self, number, fuel_type, capacity, torque):

        # initialize instance attributes
        self.number = number
        self.fuel_type = fuel_type
        self.capacity = capacity
        self.torque = torque

    # defining a method to calculate power
    def power_calc(self):
        return (self.torque * self.speed_rpm)/9950

car_1 = Cars("RJ06 1749", "Petrol", "23 Litres", 200)
car_1.power_calc()
Cars.speed_rpm = 2000
```

#### Types of Methods
* Methods are functions associated with classes
* Methods can also be of four types:
    * Instance Method
    * Class Method
    * Static Method
    * Special Methods

#### Instance Method
Take instance as an input
```python
# defininf a method
def power_calc(self):
    return (self.torque * self.speed_rpm)/9550
```

#### Class Method
Take class as an input
```python
# defining a class called 'Cars'
class Cars:

    # defining class variable and attribute
    speed_rpm = 1800

    # defining instance variables
    def __init__(self, number, fuel_type, capacity, torque):

        # initialize instance attributes
        self.number = number
        self.fuel_type = fuel_type
        self.capacity = capacity
        self.torque = torque

    # defining a method to calculate power
    def power_calc(self):
        return (self.torque * self.speed_rpm)/9950

    # defining a class method to alter speed value
    @classmethod
    def set_speed(cls, speed):
        cls.speed_rpm = speed

car_1 = Cars("RJ06 1749", "Petrol", "23 Litres", 200)
car_1.power_calc()

# change value of class
Cars.set_speed(2100)
```

#### Static Method
Neither instance nor class as input
```python
# defining a class called 'Cars'
class Cars:

    # defining class variable and attribute
    speed_rpm = 1800

    # defining instance variables
    def __init__(self, number, fuel_type, capacity, torque):

        # initialize instance attributes
        self.number = number
        self.fuel_type = fuel_type
        self.capacity = capacity
        self.torque = torque

    # defining a static method for price calculation
    @staticmethod
    def fuel_cost(price_per_litre, tank_capacity):
        return price_per_litre * tank_capacity
```


#### Special Method
* Providing existing operators with user defined meaning
* Special methods are set of pre-defined methods
* Surrounded by a double underscores (Example: __init__)
* Special methods are used for 'operator overloading'.


#### What is Operator Overloading?
* Providing existing operators with user defined meanings
```python
class Cars:

    # defining instance variables
    def __init__(self, owner, number, cost):

        # initialize instance attributes
        self.owner = owner
        self.number = number
        self.cost = cost
    
    # special method to add costs
    def __add__(first, second):
        return first.cost + second.cost

    def __len__(self):
        return len(self.owner)

# creating instances
car_1 = Cars("Aishwarya", "RJ06 1332", 500000)
car_1 = Cars("Sharoon", "DL09 2949", 750000)

car_1 + car_2   # try with or without add method

len(car_2)      # try with or without len method
```



#### Question: What will be the output of the following code block
```python
class message:
    def __init__(self, a):
        self.a = a
    
    def display(self):
        print(self.a)
    
msg_1 = message('Hello')
msg_1.display()

# answer
"Hello" is displayed
```

