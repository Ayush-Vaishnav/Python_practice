#simple calculator

def calculator(operation, n1, n2): #changes made earlier we wre not using n1 and n2 inside
    if operation =='add':
        return n1 + n2
    elif operation =='sub':
        return n1-n2
    elif operation =='multi':
        return n1*n2
    elif operation =='div':
        return n1/n2
    
while True:
    n1 = int(input("Enter number1: "))
    operation = input("Enter add, sub,multi,div: ")
    n2 = int(input("Enter number2: "))
    print(calculator(operation,n1,n2))

    '''
    after putting n1 and n2 inside, we can call it anytime directly
    and makes the code modular and we also made changes in print
    section in last earlier we were just using print(operation) but
    now we are using print(calculator(operation,n1,n2))
    '''