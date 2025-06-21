#smallest of three no

a= int(input("Enter no1. "))
b= int(input("Enter no2. "))
c= int(input("Enter no3. "))

if (a<b and a<c):
   print(f"{a} is smaller than {b} and {c}")

elif (b<a and b<c):
   print(f"{b} is smaller than {a} and {c}")

elif (c<a and c<b): 
   print(f"{c} is smaller than {b} and {a}")

else:
   print(0)