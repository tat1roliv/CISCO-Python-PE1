wordWithoutVowels = ""
userWord = input("Please Enter a word: ")
userWord = userWord.upper()
for letter in userWord:
    if letter == 'A':
        word = letter
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        wordWithoutVowels+=letter

print(wordWithoutVowels)

#solution-2
wordWithoutVowels = ""
userWord = input("Please Enter a word: ")

# make a copy of userWord
output = userWord

# replace vowels
vowels = 'aAeEiIoOuU'
for letter in vowels:
    output = output.replace(letter, '') # replace letter with empty string

print(output)
