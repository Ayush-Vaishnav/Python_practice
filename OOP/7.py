'''
STATIC METHOD
(a method which is availaible to class but not instance)
add a static method to the car class that returns a general description of a car
'''

class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self): #getter
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or diesel"
    
    @staticmethod #decorator
    def general_description():#when we use static method, we don't need to use (self)
        return "Cars are means of transport"
    
my_car = Car("Tata", "Safari")
#print(my_car.general_description())
print(Car.general_description())