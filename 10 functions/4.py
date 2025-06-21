#craete a funcction that return area and circumference given only radius
import math

def calc (radius):
    area= math.pi *radius **2
    circum= 2* math.pi * radius
    return area, circum

radius = int(input("Enter radius: "))
area, circum = calc(radius)

print(f"area is {area:.2f} and circumference is {circum:.2f}")