'''
List Sum with Condition:

Write a function sum_except_13(lst) that returns the sum of the list but skips
any number that is 13 and the number immediately after it
'''

def sum_except_13(lst):
    total = 0
    i = 0 #index
    while i < len(lst):
        if lst[i] == 13:
            i += 2  # skip 13 and the next number
        else:
            total += lst[i]
            i += 1
    return total

# Input: user enters space-separated numbers
user_input = input("Enter numbers separated by space: ")
numbers = [int(x) for x in user_input.split()]

print("Sum:", sum_except_13(numbers))

'''
THINGS I LEARNT:
due to while loop program was running continuosly for i and it was checking
again and again for new value of i for if/else

for loop doesnt allow to skip instead it runs automatically, you can skip value
but not its index or next value

whereas while loop allows manual control making skipping easy
'''