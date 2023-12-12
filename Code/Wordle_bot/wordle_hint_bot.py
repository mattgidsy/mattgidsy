#open the file containing a list of 5 letter words
with open("Code\Wordle_bot\guess_list.txt") as guess_list:
    lines = guess_list.readlines()

    
word_list = [word.strip() for word in lines]
word_tuples = [(word, list(word)) for word in word_list]
possible_guess_lst = []
possible_tups = []

#Need to write 4 searches
#correct letter(s) placement
#correct letter(s)
#excluded letter(s)
#incorrect placement
               
# def check_guessed_position(guess,guess_cl):
#    guessed_position = [(index, letter.lower()) for index, letter in enumerate(guess)]
#    return guessed_position
    
def check_correct_position(guess,guess_cl):
    # Create a list of  letter, index) tuples for the guessed letters
    if any(letter.isupper() for letter in guess) and len(possible_tups) == 0:
        guessed_positions = [(char.lower(), index) for index, char in enumerate(guess) if char.isupper()]
        for word, letters in word_tuples:
            # Check if all guessed letters are in the correct positions
            if all((g, i) in guessed_positions and g == letters[i] for g, i in guessed_positions):
                possible_tups.append((word, letters))
    elif any(letter.isupper() for letter in guess) and len(possible_tups) > 0:
        guessed_positions = [(char.lower(), index) for index, char in enumerate(guess) if char.isupper()]
        for word, letters in possible_tups:
            # Check if all guessed letters are in the correct positions
            if all((g, i) in guessed_positions and g == letters[i] for g, i in guessed_positions):
                possible_tups.append((word, letters))
    else: 
        pass
        
def check_correct_letter(guess, guess_cl):
    guess_letters = list(guess_cl)
    global possible_tups
    temp_tup_list = []
    if len(possible_tups) == 0:
        for word, letters in word_tuples:
            # Check if at least one of the specified letters is present in the word
            if all(char in word for char in guess_letters):
                if word not in possible_tups:
                # If true, pend the word to the filtered list if it's not there
                    possible_tups.append((word,letters))
    else:
        #create a new list and replace possible tups 
        for word, letters in possible_tups:
            # Check if at least one of the specified letters is present in the word
            if all(char in word for char in guess_letters):
                #if word not in possible_tups:
                # If true, append the word to the filtered list if it's not there
                temp_tup_list.append((word,letters))
        possible_tups = temp_tup_list
                                         
def possible_guess_results():
    if len(possible_tups) == 0:
        try_again = input("\nHow do I say this? \nI have failed you, there are no possible answers.\nTry again? [Y/N]: ")
        if try_again == "Y" or try_again == 'y':
            get_started()
        else:
            quit()
    else:
        possible_results = []
        for word, letters in possible_tups:
            possible_results.append(word)
        print(possible_results)
            

def get_started():
    print("\n   ###### Welcome to Wordle_Helper_Bot! ###### \n\nInput all incorretly positioned letters in lowercase \n   Input correctly positioned letters in UPPERCASE")
    print("\n   ###### Welcome to Wordle_Helper_Bot! ######")
    guess1 = input("\nInput your first guess:\n")
    guess1_cl = input("\nWhich letters are in the word but out of position?:\n")
    #code works for either but not both together. brain is fried, will fix in the morning. maybe inf loop?
    #check_upper(guess1, guess1_cl)
    check_correct_position(guess1,guess1_cl)
    check_correct_letter(guess1,guess1_cl)
    possible_guess_results()  
     
get_started()