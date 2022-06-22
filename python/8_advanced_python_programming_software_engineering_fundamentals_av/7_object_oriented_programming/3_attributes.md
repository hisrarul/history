## Attributes

* Attributes are the data stored inside the class or instance.


#### Types of Attributes
* In Object Oriented Programming, we have
    * Class Attributes: Shared between all objects of this class
    * Instance attributes: Belongs to one and only one object

#### Quick recap
Instance            <--- Car 1:
Instance Variables  <--- Car Number: 1922   ---> Attribute
Instance Variables  <--- Fuel Type: Petrol  ---> Attribute
Instance Variables  <--- Fuel Capacity: 35 L   ---> Attribute
Instance Variables  <--- Torque: 200 Nm   ---> Attribute


#### Instance and Class Attribute
```python
# defining a class called 'Cars'
class Cars:
    # defining class variable and attribute
    num_wheels = 4
    year_manufacture = 2020

    # defining instance variables
    def __init__(self, number, fuel_type, capacity, torque):

        # initialize instance attributes
        self.number = number
        self.fuel_type = fuel_type
        self.capacity = capacity
        self.torque = torque

# creating car_1 and car_2 instances
# defining instance attributes
car_1 = Cars("RJ04 1717", "Petrol", "35 Litres", 200)
car_2 = Cars("DL04 1968", "Disel", "30 Litres", 250)

car_1.fuel_type
car_2.capacity
```

#### Question: What is the difference between instance attributes and class attributes?
Instance attributes are unique to individual instances while class attributes are commom for all instances.

* Class variables and attributes are defined within a class but before the init function.

* Instance variable and attributes are defined within the init function.




