'''
fun with **kwargs
create a fun that accepts any no of keywords and prints them in format key: value
'''

#kwargs = key word args

def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="iron man", power="laser",enemy = 'ultron')
