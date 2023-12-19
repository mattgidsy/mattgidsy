guess = "guAva"
guess_cl = ""

incorrect_guess_positions = []
correct_positions = []
for index, char in enumerate(guess):
    if char not in guess_cl and char.islower():
        incorrect_guess_positions.append((index, char))
    elif char not in guess_cl and char.isupper():
        correct_positions.append((index, char.lower()))
        
print(incorrect_guess_positions)
print(correct_positions)