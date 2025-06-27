#max of three numbers

def max_of_three(a,b,c):
    if a>b and a>c:
        return (f'{a} is greater than {b} and {c}')

    elif b>a and b>c:
        return (f'{b} is greater than {a} and {c}')

    else:
        return (f'{c} is greater than {a} and {b}')

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print(max_of_three(a,b,c))
#always make sure that in function always return something
#before return we used print there, which did'nt give any error
#but it was not appropriate too