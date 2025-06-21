# Count the number of words in a sentence

# Count the number of words in a sentence using loop

sentence = input("Enter a sentence: ")

word_count = 0
in_word = False

for char in sentence:
    if char != ' ':
        if not in_word:
            word_count += 1
            in_word = True
    else:
        in_word = False

print("Number of words:", word_count)
