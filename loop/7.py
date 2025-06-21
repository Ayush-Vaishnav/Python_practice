#Reverse a number using a loop

n = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10          # get the last digit
    rev = rev * 10 + digit  # build the reversed number
    n = n // 10             # remove the last digit

print(f"Reversed number: {rev}")
