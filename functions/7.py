#fibonacci series

def fibonacci(n):
    a,b = 0,1
    series= []

    for _ in range(n):
        series.append(a)
        a,b=b,a+b

    return series

n= int(input("Enter number: "))
print(fibonacci(n))

'''
a=0 and b=1 are the already decided number
we created [] empty list to store values in it
we will keep adding number using append() and it adds current value of a
(a,b=b,a+b) a becomes b and b becomes sum of old a+b

WHAT I LEARNT SO FAR...
i can use _ in such situations, before i was using i
'''