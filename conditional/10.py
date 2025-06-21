#triangle validator- take 3 side, sum of 2 should be greatre than 3

# a = int(input("Enter no."))
# b = int(input("Enter no."))
# c = int(input("Enter no."))

# if (a+b>c):
#     print("verified")

# elif(b+c>a):
#     print("verified")

# elif (c+a>a):
#     print("verified")

# else:
#     print("INVALID OPERATION")

a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))

if (a + b > c) and (b + c > a) and (c + a > b):
    print("Triangle is valid")
else:
    print("Triangle is NOT valid")
