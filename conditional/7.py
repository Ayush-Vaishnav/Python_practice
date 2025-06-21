#grading system

m= int(input("Enter marks: "))

if (m<=100) and (m>=90):
    print("A")

elif (m<=89) and (m>=80):
    print("B")

elif (m<=79) and (m>=70):
    print("C")

elif (m<=69) and (m>=60):
    print("D")

elif (m<=59) and (m>=50):
    print("E")

else:
    print("You need to reappear")