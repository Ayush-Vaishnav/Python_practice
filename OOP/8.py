'''
PROPERTY DECORATORS
use a property decorator in the Car to make the model attribute read-only
'''

class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model #we made it pvt here
        Car.total_car += 1

    def get_brand(self): #getter
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or diesel"
    
    @staticmethod #decorator
    def general_description():#when we use static method, we don't need to use (self)
        return "Cars are means of transport"
    
    @property #this is a property which not everyone can access, to use it you must access it with particular method only
    def model(self):
        return self.__model #model access
    
my_car = Car("Tata", "Safari")
my_car.__model = "city"
#print(my_car.general_description())
#print(my_car.__model)
print(my_car.model)