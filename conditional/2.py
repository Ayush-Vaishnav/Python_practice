#test if no is +ve, -ve or 0

while True:
    n= int(input("Enter no: "))
    if (n==0):
        print("No is zero")
    elif (n>0):
        print(f"{n} is +ve")
    else:
        print(f"{n} is -ve")