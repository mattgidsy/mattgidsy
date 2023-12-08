LETTERS = 'ABCDEFGH'
VOWELS = 'AEIOU'

guess1 = 'tAbLe'
guess_cl = 'le'
words = ["apple", "table", "chair", "house", "mouse", "plant", "bread", "water", "earth", "music"]

# Creating a list of tuples
word_tuples = [(word, list(word)) for word in words]
possible_tups = []
# Printing the result
# for (word, letters) in word_tuples:
#     if "n" == letters[3]:
#         if (word,letters) not in possible_tups:
#             possible_tups.append((word,letters))

#print(possible_tups)
# def find_upper():
#     index = -1
#     for char in guess1:
#         index += 1
#         if char.isupper():
#             print(index)

# find_upper()

def check_correct_place(guess, guess_cl):
    for index, char in enumerate(guess):
        if char.isupper():
            print(index) 
            
check_correct_place(guess1,guess_cl)