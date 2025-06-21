#check if a number is divisible by both 5 and 11

n = int(input("Enter number: "))

if (n%5==0) and (n%11==0):
    print("no is divisible")
else:
    print("No is not divisible")