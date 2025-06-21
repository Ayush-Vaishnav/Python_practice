#reverse a string using loop
a = 'Python'
reversed = ''

for char in a:
    reversed= char + reversed

print(reversed)

'''

First char: 'P' → reversed = 'P'

Next char: 'y' → reversed = 'y' + 'P' = 'yP'

Then 't' → reversed = 't' + 'yP' = 'tyP'

Then 'h' → reversed = 'h' + 'tyP' = 'htyP'

'''