#factorial

def factorial (n):
    if n==1 or n==0:
        return 1
    else:
        count = 1
        for i in range(1,n+1):
            count = count * i
        return count
        
n = int(input('enter n: '))
print(factorial(n))

'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
        #here, factorial made it a recursive function due to
        which we don't need to call it again and again

        
it is not that efficient for large value of n
'''