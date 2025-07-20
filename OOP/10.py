'''
MULTIPLE INHERITANCE
create two class, Battery and Engine, and let the ElectricCar class inherit
from both, demonstrating multiple inheritance
'''

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self): #getter
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) #super allows us to access init of the upper class
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

class Battery:
    def battery_info(self):
        return "Thsi is battery"

class Engine:
    def Engine_info(self):
        return "This is engine"

class ElectricCar2(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar2("Tesla", "model s")
print(my_new_tesla.Engine_info())
print(my_new_tesla.battery_info())
