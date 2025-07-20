'''
INCAPSULATION
modify the car class to encapsulate the brand attribute, making it 
private, and provide a getter method to it
'''

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self): #getter
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) #super allows us to access init of the upper class
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
#print(my_tesla.__brand)
print(my_tesla.get_brand())

'''
when we use double underscore before any varibale it means that
it is now private, which means you can access it inside class but cannot
access it when any object is made, in order to access it we have to use
getter function
'''