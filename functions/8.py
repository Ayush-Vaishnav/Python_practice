#count vowels

def count_vowels(s):
    count =0
    for char in s:
        if char.lower() in ('a', 'e', 'i', 'o', 'u'):
            count+=1
    return count
        
    
# print(count_vowels("vaishnav"))
s = input("Enter name: ")
print(count_vowels(s))

'''
we used .lower() to convert any given input to lowercase
indentation should be used correctly for return
'''