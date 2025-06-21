# Check if a number is an Armstrong number

# Check if a number is an Armstrong number using loop

num = int(input("Enter a number: "))
original_num = num

# Count the number of digits
n = 0
temp = num
while temp > 0:
    temp = temp // 10
    n += 1

# Calculate sum of digits raised to the power n
temp = num
result = 0
while temp > 0:
    digit = temp % 10
    result += digit ** n
    temp = temp // 10

# Check and print result
if result == original_num:
    print(original_num, "is an Armstrong number.")
else:
    print(original_num, "is not an Armstrong number.")
