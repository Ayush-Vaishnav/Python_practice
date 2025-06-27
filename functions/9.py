#palindrome checker

def palindrome_checker(p):
    if p == p[::-1]:
        return "palindrome"
    else:
        return 'not a palindrome'
    
p = input("Enter the word: ")
print(palindrome_checker(p))


'''
basic logic is used, string slicing
'''