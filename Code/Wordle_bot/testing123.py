#open the file containing a list of 5 letter words
with open("Code\Wordle_bot\sample_list.txt") as guess_list:
    lines = guess_list.readlines()

#iterate through the word list (this one contains 5 letter words for wordle)   
#create word tuples to use for parsing ie: ('apple', ['a','p','p','l','e'])
word_list = [word.strip() for word in lines]
word_tuples = [(word, list(word)) for word in word_list]
possible_guess_lst = []
possible_tups = []





def filter_excluded_letter(guess, guess_cl):
    global possible_tups
    temp_tups = []

    # Create the list of excluded letters without using list comprehension
    excluded_letters = []
    for letter in guess:
        if letter.islower() and letter not in guess_cl:
            excluded_letters.append(letter)
    print(f"excluded letters:{excluded_letters}")
    
    # Create 2 lists of tuples, containing the indexed characters of the incorrect guess positions and the correct guess positions      
    correct_positions = []
    for index, char in enumerate(guess):
        if char not in guess_cl and char.isupper():
            correct_positions.append((index, char.lower()))
    print(f"correct_positions:{correct_positions}")
    
    #search possible_tups for excluded letters but not excluding letters in in correct position
    for word, letters in possible_tups:
        for index, char in enumerate(word):
            if (index,char) not in correct_positions and char not in excluded_letters:
                
                temp_tups.append((word,letters))
                
    possible_tups = temp_tups
    
guess = "guAva"
guess_cl = ""
filter_excluded_letter(guess, guess_cl)
