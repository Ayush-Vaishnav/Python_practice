# Display this pattern using nested loops:

# A
# B B
# C C C
# D D D D

# Print the alphabet pattern

rows = 4  # You can change this or take input from user

for i in range(1, rows + 1):
    char = chr(64 + i)  # 65 = 'A', 66 = 'B', etc.
    for j in range(i):
        print(char, end=' ')
    print()
