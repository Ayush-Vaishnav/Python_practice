#Print Fibonacci series up to n terms

# Print Fibonacci series up to n terms

n = int(input("Enter number of terms: "))

a, b = 0, 1 #a=0 and b=1, first two fibonacci series
count = 0

while count < n: #loop runs n times 
    print(a, end=' ')
    a, b = b, a + b
    count += 1
