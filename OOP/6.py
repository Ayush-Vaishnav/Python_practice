'''
CLASS VARIABLE
add a class variable to Car that keeps track of the numbers of cars created
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
    
Car("tata", "Safari")
Car("tata", "Nexon")

print(Car.total_car)