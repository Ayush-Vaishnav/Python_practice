#print multiplication for a given n upto n, skip 5th iteration

n =int(input("Enter number: "))
for i in range(1,11):
    if i ==5:
        continue
    print(f"{n} X {i} = {n*i}")