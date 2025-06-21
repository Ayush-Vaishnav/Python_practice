#palindrome checker

# using for loop
# text = input("Enter text: ")
# is_palindrome = True  # Assume it's a palindrome

# for i in range(len(text) // 2):
#     if text[i] != text[-(i + 1)]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print("It's a palindrome!")
# else:
#     print("Not a palindrome.")


#using while loop
text = input("Enter text: ")
left = 0
right = len(text) - 1
is_palindrome = True

while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

