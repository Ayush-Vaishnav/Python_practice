#prime checker

def is_prime(n):
    if n<=1:
        return "invalid"
    
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True
        
n = int(input("Enter no: "))
print(is_prime(n))