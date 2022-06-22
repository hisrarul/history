#### Defininf Parent and Child Class
1. Inheriting the init function from parent class.

```python
%load_ext lab_black
```

```python
# Creating Parent Class
class Cars:
    # defining init method
    def __init__(self, number, fuel_capacity, exshowroom_price):
        self.number = number
        self.fuel_capacity = fuel_capacity
        self.exshowroom_price = exshowroom_price
```

```python
# Creating Child Class
class ElectricCars(Cars):
    # defining init method
    def __init__(self, number, fuel_capacity, exshowroom_price):
        # inheriting from parent class
        super().__init__(number, fuel_capacity, exshowroom_price)
```

```python
# creating instance car_1 and ecar_1
car_1 = Cars("RJ04 1230", "24 Litres", "500000")
ecar_1 = ElectricCars("DL12 3321", "15 Litres", 860000)

car_1.exshowroom_price
```

2. Inheriting the init function from parent class and initialising more attributes.
```python
# Creating Parent Class
class Cars:
    # defining init method
    def __init__(self, number, fuel_capacity, exshowroom_price):
        self.number = number
        self.fuel_capacity = fuel_capacity
        self.exshowroom_price = exshowroom_price
```

```python
# Creating Child Class
class ElectricCars(Cars):
    # defining init method
    def __init__(self, number, fuel_capacity, exshowroom_price):
        # inheriting from Class Cars
        super().__init__(number, fuel_capacity, exshowroom_price)
        self.charger_type = charger_type
        self.charging_cost = charging_cost
```

```python
# creating instance car_1 and ecar_1
car_1 = Cars("RJ04 1230", "24 Litres", "500000")
ecar_1 = ElectricCars("DL12 3321", "15 Litres", 860000, "CCS", "39 units")

ecar_1.charger_type

car_1.charger_type      # get error

car_1.exshowroom_price

```

3. Inheriting method from parent class
```python
# Creating Parent Class
class Cars:
    # class variable
    registration_charges = 0.5

    # defining init method
    def __init__(self, number, fuel_capacity, exshowroom_price):
        self.number = number
        self.fuel_capacity = fuel_capacity
        self.exshowroom_price = exshowroom_price
    
    # method to calculate on road price
    def on_road_price(self):
        cost_of_registration = self.exshowroom_price * self.registration_charges
        return self.exshowroom_Price + cost_of_registration
```

```python
# Creating Child Class
class ElectricCars(Cars):
    # defining init method
    def __init__(self, number, fuel_capacity, exshowroom_price):
        # inheriting from Class Cars
        super().__init__(number, fuel_capacity, exshowroom_price)
        self.charger_type = charger_type
        self.charging_cost = charging_cost
```


```python
# creating instance car_1 and ecar_1
car_1 = Cars("RJ04 1230", "24 Litres", "500000")
ecar_1 = ElectricCars("DL12 3321", "15 Litres", 860000, "CCS", "39 units")

car_1.on_road_price()

# using parent class method to calc price
ecar.on_road_price()
```

3. Different Class Attributes for parent and child class
```python
# Creating Parent Class
class Cars:
    # class variable
    registration_charges = 0.5

    # defining init method
    def __init__(self, number, fuel_capacity, exshowroom_price):
        self.number = number
        self.fuel_capacity = fuel_capacity
        self.exshowroom_price = exshowroom_price
    
    # method to calculate on road price
    def on_road_price(self):
        cost_of_registration = self.exshowroom_price * self.registration_charges
        return self.exshowroom_Price + cost_of_registration
```

```python
# Creating Child Class
class ElectricCars(Cars):
    # class variable
    registration_charges = 0.12

    # defining init method
    def __init__(self, number, fuel_capacity, exshowroom_price):
        # inheriting from Class Cars
        super().__init__(number, fuel_capacity, exshowroom_price)
        self.charger_type = charger_type
        self.charging_cost = charging_cost
```

```python
# creating instance car_1 and ecar_1
car_1 = Cars("RJ04 1230", "24 Litres", "500000")
ecar_1 = ElectricCars("DL12 3321", "15 Litres", 860000, "CCS", "39 units")

car_1.on_road_price()

# using parent class method to calc price
ecar.on_road_price()
```


#### Benefits of using inheritance
* Allows code reusability
* Provides clean and readable code

