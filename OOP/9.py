'''
CLASS INHERITANCE AND INSTANCE() FUNCTION
demonstrate the use of instance() to check if my_tesla is an instance of Car and ElectricCar
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
#print(my_tesla.__brand)
# print(my_tesla.get_brand())

# print(my_tesla.fuel_type())

# safari = Car("tata", "Safari")
# print(safari.fuel_type())

print(isinstance(my_tesla, Car)) #will give valur in true or false
print(isinstance(my_tesla, ElectricCar))