#create a recursive function to calc factorial of a number

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))  

'''
so it will run continously until it hits base condition 0 and 1, either condition
is hit it will give 1 and it will multiply by 1,  i.e. either of 1 condition hits first
it will get multiplied by the base value which is getting returned and not the no itself
here it is return 1, so it will get * by 1
'''