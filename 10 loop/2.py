#calc sum of even no given upto n

n = int(input("Enter number- "))
sum =0

for i in range (1,n+1):
    if i%2==0:
        sum+=1

print("the print is of the", sum)


#to print sum of values of number

n = int(input("Enter number: "))
sum = 0

for i in range (0, n+1):
    if i %2==0:
        sum+=i

print("Sum of values is ", sum)