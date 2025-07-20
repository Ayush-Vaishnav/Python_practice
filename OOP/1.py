'''
create a car class with attributes like brand and model,
then create an instance of this class
'''

class Car:
    def __init__(self, brand, model): #brand and model is parameters which the user has provided
        self.brand = brand #self. variables are the variables inside the class
        self.model = model

my_Car= Car("Toyota", "LC300")
print(my_Car.brand)
print(my_Car.model)

my_new_car = Car("BMW", "M340i")
print(my_new_car.brand)
print(my_new_car.model)