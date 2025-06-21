#leap year checker 

n = int(input("Enter year: "))

if (n % 400 == 0):
    print("Leap year")
elif (n % 100 == 0):
    print("Not a leap year")
elif (n % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")
