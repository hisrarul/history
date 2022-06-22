## Inheritance

#### Let's take an example
Storing the following information
* Vehicle Number
* Engine Capacity
* Ex showroom Cost

Storing additional information
* Charger Type
* Charging Cost

#### Defining Classes
```python
class Cars:
    def __init__(self, number, fuel_capacity, exshowroom_price):
        self.number = number
        self.fuel_capacity = fuel_capacity
        self.exshowroom_price = exshowroom_price
```

Creating another class Electric_Cars with some additional parameters
```python
class Electric_Cars:
    def __init__(self, number, fuel_capacity, exshowroom_price, charger_type, charging_cost):
        self.number = number
        self.fuel_capacity = fuel_capacity
        self.exshowroom_price = exshowroom_price
        self.charger_type = charger_type
        self.charging_cost = charging_cost
```

We can in above code that there is repetition of code in both of the class. To avoid that we use the concept of inheritance i.e. we can inherit the information from `Cars` to `Electric_Cars` class.

```python
class Cars:
    def __init__(self, number, fuel_capacity, exshowroom_price):
        self.number = number
        self.fuel_capacity = fuel_capacity
        self.exshowroom_price = exshowroom_price

class Electric_Cars(Cars):      # class name in parameter
    def __init__(self, number, fuel_capacity, exshowroom_price, charger_type, charging_cost):
        super().__init__(number, fuel_capacity, exshowroom_price)       # inherit using super()
        self.charger_type = charger_type
        self.charging_cost = charging_cost
```



