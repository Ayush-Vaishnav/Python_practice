#even or odd

def is_even(num):
    if num%2==0:
        return True
    else:
        return False

num= int(input('Enter no: '))
print(is_even(num))
