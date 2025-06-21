#Find the sum of digits of a number

n =int(input("Enter number: "))
total =0

while n>0:
    digit =n%10
    total+= digit
    n=n//10 #removes last no

print(total)


'''
when you enter a no eg 456, it will divide by 10 remove 6 store it in total then
//10 cuts the last no i.e.6, now it will again start the loop for 45 and same process
happens everytime until nothings left

'''