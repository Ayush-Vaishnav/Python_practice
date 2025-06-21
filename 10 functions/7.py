'''
fun with *arg
write a function that takes variable no. of arguments and return their sum

'''

def add_all (*args):
    print(args)
    return sum(args)

print(add_all(1,3,5,6,7))