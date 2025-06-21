#Character Type Checker

a = input("Enter a character: ")

if len(a) != 1:
    print("Please enter only one character.")
elif a.isupper():
    print("It is an uppercase letter.")
elif a.islower():
    print("It is a lowercase letter.")
elif a.isdigit():
    print("It is a digit.")
else:
    print("It is a special character.")
