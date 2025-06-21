#Count the number of vowels in a given string

vowels = 'aeiou'
count = 0

q = input("Enter a string: ").lower()  # lower() to count uppercase vowels too

for char in q:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")
