#https://www.aeio.win/answers.txt
#https://www.aeio.win/guesses.txt
# LETTERS = 'ABCDEFGH'
# VOWELS = 'AEIOU'

# guess1 = 'tAbLe'
# guess_cl = 'le'
# words = ["apple", "table", "chair", "house", "mouse", "plant", "bread", "water", "earth", "music"]

# # Creating a list of tuples
# word_tuples = [(word, list(word)) for word in words]
# possible_tups = []
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

# def check_correct_place(guess, guess_cl):
#     for index, char in enumerate(guess):
#         if char.isupper():
#             print(index) 
            
# check_correct_place(guess1,guess_cl)

def check_correct_place(guess):
    possible_tups = []
    
    # Create a list of (lowercase letter, index) tuples for the guessed letters
    guessed_positions = [(char.lower(), index) for index, char in enumerate(guess) if char.isupper()]

    for word, letters in word_tuples:
        # Check if all guessed letters are in the correct positions
        if all((g, i) in guessed_positions and g == letters[i] for g, i in guessed_positions):
            possible_tups.append((word, letters))
                    
    return possible_tups

# Example usage:
words = ["slate", "slide", "sound", "salad"]
word_tuples = [(word, list(word)) for word in words]

guess = "SlatD"
result = check_correct_place(guess)
print(result)
# print(possible_tups)

# def find_upper():
#     index = -1
#     #find a way to deal with more than 1 uppercase
#     for char in guess1:
#         index += 1
#         if char.isupper():
#             return index

#original
# def check_correct_place(guess, guess_cl):
#     for index, char in enumerate(guess):
#         if char.isupper():
#             for word,letters in word_tuples:
#                  if char.lower() == letters[index]:
#                      possible_tups.append((word,letters))
                     
#chat modified
# def check_correct_place(guess):
#     possible_tups = []
    
#     # Create a list of (lowercase letter, index) tuples for the guessed letters
#     guessed_positions = [(char.lower(), index) for index, char in enumerate(guess) if char.isupper()]

#     for word, letters in word_tuples:
#         # Check if all guessed letters are in the correct positions
#         if all((g, i) in guessed_positions and g == letters[i] for g, i in guessed_positions):
#             possible_tups.append((word, letters))
                    
#     return possible_tups