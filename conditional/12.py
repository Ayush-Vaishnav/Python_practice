#Profit or Loss. Input cost price and selling price, and print whether 
# there’s profit, loss, or no change

a= int(input("Enter cost price: "))
b= int(input("Enter selling price: "))


if a>b:
    print(f"Its a loss of {a-b}Rs.")

elif b>a:
    print(f"Its a profit of {b-a}")

else:
    print("no change")