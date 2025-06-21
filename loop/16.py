# Print a pattern like this:
# 1
# 12
# 123
# 1234

# Print the pattern

# rows = 4  # You can also take input from user using int(input())

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     print()  # Move to the next line after each row

#user input version.......

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

