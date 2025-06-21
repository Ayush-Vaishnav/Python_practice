#keep asking the user for input until they enter a no b/w 1 and 10

while True:
    a = int(input("Enter number: "))  # Takes user input and converts it to integer
    if 1 <= a <= 10:                  # Checks if the number is between 1 and 10 (inclusive)
        print('thanks')              # If yes, prints 'thanks'
    else:
        print("Sorry")              # If not, prints 'Sorry'
