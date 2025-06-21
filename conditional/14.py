#Palindrome Checker: Input a string and check if it reads the same backward

a= input("Enter string: ")#this is for string input


b= a[::-1]#this reverses the string

if a==b:
    print("Yes it is a palindrome")

else:
    print("Not a palindrome")