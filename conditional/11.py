#Calculator with Menu

a = float(input("Enter first number: "))
o = input("Enter operation (+, -, *, /): ")
b = float(input("Enter second number: "))

if o == "+":
    print(f"Sum is {a + b}")

elif o == "-":
    print(f"Subtraction is {a - b}")

elif o == "*":
    print(f"Multiplication is {a * b}")

elif o == "/":
    if b == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(f"Division is {a / b}")

else:
    print("Invalid operation")
