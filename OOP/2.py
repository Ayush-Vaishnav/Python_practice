'''
add method to the car class that displys the full name of 
car(brand and model)
'''

#we are adding functionality

class Car:
    def __init__(self, brand, model): #brand and model is parameters which the user has provided
        self.brand = brand #self. variables are the variables inside the class
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"




my_Car= Car("Toyota", "LC300")
print(my_Car.brand)
print(my_Car.model)
print(my_Car.full_name()) #we're using paranthesis because we added a function and not a variable, the above two are variables