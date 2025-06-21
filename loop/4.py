#Calculate the sum of numbers from 1 to n

n= int(input("Enter number: "))
total = 0
for n in range (1,n+1):
    
    total+=n #total=total+n
print(f'sum is {total}')