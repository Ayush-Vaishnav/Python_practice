#given a string, find first non repated character

a= 'teeteracdacd'

for char in a:
    if a.count(char) == 1:
        print("Char is: ", char)
        break #better optimization 