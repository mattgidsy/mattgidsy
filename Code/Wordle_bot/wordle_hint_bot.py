##### wordle helper by inquiz #####

#open the file containing a list of 5 letter words
with open("Code\Wordle_bot\guess_list.txt") as guess_list:
    lines = guess_list.readlines()
    
word_list = [word.strip() for word in lines]
word_tuples = [(word, list(word)) for word in word_list]
possible_guess_lst = []
possible_tups = []

#Need to write 4 searches
#correct letter(s)
#correct letter(s) placement
#excluded letter(s)
#incorrect placement
               
def check_correct_place(guess,guess_cl):
    
    # Create a list of (lowercase letter, index) tuples for the guessed letters
    guessed_positions = [(char.lower(), index) for index, char in enumerate(guess) if char.isupper()]

    for word, letters in word_tuples:
        # Check if all guessed letters are in the correct positions
        if all((g, i) in guessed_positions and g == letters[i] for g, i in guessed_positions) and (word, letters) not in possible_tups:
            possible_tups.append((word, letters))

                                  
#this needs to be re-worked to use the tuples list
def check_correct_letter(guess, guess_cl):
    guess_letters = list(guess_cl)
    for word in word_list:
        # Check if at least one of the specified letters is present in the word
        if all(letter in word for letter in guess_letters):
            if word not in possible_guess_lst:
            # If true, append the word to the filtered list if it's not there
                possible_guess_lst.append(word)

def possible_guess_results():
    if possible_guess_lst == []:
        try_again = input("\nHow do I say this? \nI have failed you, there are no possible answers.\nTry again? [Y/N]: ")
        if try_again == "Y" or try_again == 'y':
            get_started()
        else:
            quit()
    else:
        print(possible_guess_lst)

def get_started():
    print("\n   ###### Welcome to Wordle_Helper_Bot! ###### \n\nInput all incorretly positioned letters in lowercase \n   Input correctly positioned letters in UPPERCASE")
    print("\n   ###### Welcome to Wordle_Helper_Bot! ######")
    guess1 = input("\nInput your first guess:\n")
    guess1_cl = input("\nWhich letters are in the word but out of position?:\n")
    check_correct_place(guess1,guess1_cl)
    #check_correct_letter(guess1,guess1_cl)
    print(possible_tups)
    #possible_guess_results()    


get_started()