## Types of Inheritance

* Single
* MultiLevel
* Multiple
* Hierarchical

#### Single
Parent Class ---> Child Class

#### MultiLevel
Parent Class ---> Child Class ---> Child Class

Base Class ---> Intermediate Class ---> Derived Class

```python
# Base Class
class Vehicles:
    def __init__(self, number, exshowroom_price):
        self.number = number
        self.exshowroom_price = exshowroom_price

# Intermediate class
class Cars(Vehicles):
    def __init__(self, number, exshowroom_price, n_passenger)
    self.n_passenger = n_passenger

# Derived class
class ElectricCars(Cars):
    def __init__(self, number, exshowroom_price, n_passenger, charger_type)
    self.charger_type = charger_type
```

```python
vehicle_1 = Vehicles("RJ05 1232", 500000)
car_1 = Cars("DL09 2294", 7500000, 5)
ecar_1 = ElectricCars("DL12 9994", 200000, 5, "RCA")
```


#### Multiple Inheritance
Parent Class, Parent Class ---> Child Class

| Parent Class | Parent Class | Registering Car |
| Vehicle specifications | Cost Calculation | Registering Car |
| Vehicle number, Fuel type, Fuel capacity, Power | Ex-showroom, road tax, insurance | Vehicle details, on road price |

```python
# Parent Class 1 - storing Vehicle specifications
class VehicleSpecs:
    def __init__(self, number, fuel_type, fuel_capacity, power):
        self.number = number
        self.fuel_type = fuel_type
        self.fuel_capacity = fuel_capacity
        self.power = power
```


```python
# Parent Class 2 - Cost Calculation
class CostCalc:
    # class variables
    tax_percent = 0.07
    insurance_percent = 0.12
    registration_charge = 0.1

    def __init__(self, ex_showroom):
        self.ex_showroom = ex_showroom
    
    def on_road_price(self):
        cost_of_registration = self.exshowroom * self.registration_charge
        tax_added = self.ex_showroom * self.tax_percent
        cost_of_insurance = self.ex_showroom * self.insurance_percent
        return self.ex_showroom + cost_of_registration + cost_of_insurance + tax_added
```

```python
class CarRegistration(VehicleSpecs, CostCalc):
    def __init__(self, number, fuel_type, fuel_capacity, power, ex_showroom):
        VehicleSpecs.__init__(self, number, fuel_type, fuel_capacity,power)
        CostCalc.__init__(self, ex_showroom)

car_1 = CarRegistration("DL 4545", "Petrol", 35, 190, 500000)

car_1.on_road_price()

car_1.fuel_capacity
```

#### Hierarchical

Parent Class ---> Child Class, Child Class

```python
# Parent Class 1 - storing Vehicle specifications
class VehicleSpecs:
    def __init__(self, number, ex_showroom,):
        self.number = number
        self.ex_showroom = ex_showroom


# Child Class 1 - Cars
class Cars(VehicleSpecs):
    def __init__(self, number, ex_showroom, fuel_type, fuel_capacity, power):
        super().__init__(number, ex_showroom)
        self.fuel_type = fuel_type
        self.fuel_capacity = fuel_capacity


# Child Class 2 - Ebikes
class Ebike(VehicleSpecs):
    def __init__(self, number, ex_showroom, charger_type):
        super().__init__(number, ex_showroom)
        self.charger_type = charger_type

car_1 = Cars("DL12 6767", 500000, "petrol", 30)

ebike_1 = Ebike("DL12 6767", 200000, "RCA")
```

