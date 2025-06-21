'''
uniqueness checker, check if all the elements
are unique, if duplicate found exit the loop
and print the duplicate
'''
items = ["apple", "banana" , "orange","apple","mango" ]
unique = set()


for item in items:
    if item in unique:
        print("duplicate", item)
        break
    unique.add(item)