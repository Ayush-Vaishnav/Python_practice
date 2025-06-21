#count how many no are +ve

numbers = [1,-2,3, -4, 5,6 ,-7,-8,9,10]

positive =0
for num in numbers:
    if num > 0:
        positive+=1

print("Final count of +ve no is ", positive)