# Electricity Bill Calculator
# Take total units and calculate bill based on the slab:

# First 100 units: ₹5/unit
# Next 100 units: ₹7/unit
# Above 200 units: ₹10/unit

# units = int(input("Enter units burnt: "))
# a=100

# if units<=100:
    
#     b=units*5
#     print(f"bill is Rs.{b}")

# elif units>=101 and units <=199:
#     b= (units-a)*7

# else :
#     print("INVALID")

units = int(input("Enter units consumed: "))

bill = 0

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7

else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print(f"Your total electricity bill is Rs. {bill}")
