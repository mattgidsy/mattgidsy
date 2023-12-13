#open the file containing a list of 5 letter words
with open("Code\Wordle_bot\guess_list.txt") as guess_list:
    lines = guess_list.readlines()

#iterate through the word list (this one contains 5 letter words for wordle)   
#create word tuples to use for parsing ie: ('apple', ['a','p','p','l','e'])
word_list = [word.strip() for word in lines]
word_tuples = [(word, list(word)) for word in word_list]
possible_guess_lst = []
possible_tups = []

#Need to write 4 searches for wordle solving
#correct letter(s) placement
#correct letter(s)
#excluded letter(s)
#incorrect placement

def filter_incorrect_positions(guess, guess_cl):
    global possible_tups

    # Create a list of tuples (letter, index) for each letter in guess_cl and its corresponding index in guess
    guess_cl_positions = [(char, index) for index, char in enumerate(guess) if char in guess_cl]

    # If there are letters to check in guess_cl and possible_tups is not empty
    if guess_cl_positions and possible_tups:
        new_possible_tups = []

        for word, letters in possible_tups:
            # Check if any of the letters in guess_cl_positions matches the same position in the word
            # If so, we exclude this word from the new list
            if not any(word[index] == char for char, index in guess_cl_positions):
                new_possible_tups.append((word, letters))

        # Update possible_tups with the filtered list
        possible_tups = new_possible_tups
        
def filter_excluded_letter(guess, guess_cl):
    global possible_tups

    excluded_letters = [letter for letter in guess if letter.islower() and letter not in guess_cl]

    # Create a new list with tuples that do not contain any of the excluded letters
    possible_tups = [(word, letters) for word, letters in possible_tups if not any(char in word for char in excluded_letters)]       
    
def filter_correct_position(guess): 
    global possible_tups
    temp_tup_list = []
    #check if there are any uppercase letters and if possible_tups is empty
    if any(letter.isupper() for letter in guess) and len(possible_tups) == 0:
        #index the guessed word's letters for parsing
        guessed_positions = [(char.lower(), index) for index, char in enumerate(guess) if char.isupper()]
        #search word_tuples
        for word, letters in word_tuples:
            # Check if all guessed letters are in the correct positions
            if all((g, i) in guessed_positions and g == letters[i] for g, i in guessed_positions):
                possible_tups.append((word, letters))
    elif any(letter.isupper() for letter in guess) and len(possible_tups) > 0:
        guessed_positions = [(char.lower(), index) for index, char in enumerate(guess) if char.isupper()]
        #if word not in possible_tups append to a temp list and replace global list to deduce
        for word, letters in possible_tups:
            if all((g, i) in guessed_positions and g == letters[i] for g, i in guessed_positions):
                temp_tup_list.append((word, letters))
        possible_tups = temp_tup_list
    else: 
        pass
        
def filter_correct_letter(guess_cl):
    guess_letters = list(guess_cl)
    # I know it's yucky to use global but I don't know another way.
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
                #if word not in possible_tups append to a temp list and replace global list to deduce
                temp_tup_list.append((word,letters))
        possible_tups = temp_tup_list
                                         
def possible_guess_results():
    if len(possible_tups) == 0:
        try_again = input("\nHow do I say this? \nI have failed you, there are no possible answers.\nTry again? [Y/N]: ")
        if try_again == "Y" or try_again == 'y':
            get_started()
        else:
            quit()
    elif len(possible_tups) == 1:
        possible_results = [word for word, _ in possible_tups]
        print(f"   *:.Congratuations!.:*\n\n {possible_results} is your answer! \n        ... right?")
        quit()
    else:
        possible_results = []
        for word, letters in possible_tups:
            possible_results.append(word)
        print(possible_results)
        
def ask_guess():
    for i in range(5):
        guess = input("\nInput your 5 letter guess:\n")
        if guess == "quit":
            quit()
        guess_cl = input("\nWhich letters are in the word but out of position?:\n")
        if guess_cl == 'quit':
            quit()
        filter_correct_position(guess)
        filter_correct_letter(guess_cl)
        filter_excluded_letter(guess, guess_cl)
        filter_incorrect_positions(guess, guess_cl)
        possible_guess_results()

def get_started():
    print("\n   ###### Welcome to Wordle_Helper_Bot! ###### \n\nInput all incorretly positioned letters in lowercase \n   Input correctly positioned letters in UPPERCASE\n      Type 'quit' to exit")
    print("\n   ###### Welcome to Wordle_Helper_Bot! ######")
    ask_guess() 
 
get_started()