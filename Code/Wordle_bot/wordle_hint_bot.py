#open the file containing a list of 5 letter words
with open("Code\Wordle_bot\guess_list.txt") as guess_list:
    lines = guess_list.readlines()

#iterate through the word list (this one contains 5 letter words for wordle)   
word_list = [word.strip() for word in lines]
possible_words = []

#filter letters that were correct but out of position, remove words with the correct letter's old position
def filter_incorrect_positions(guess, guess_cl):
    global possible_words

    # Create the list of tuples (index, letter) for each letter in guess_cl and its corresponding index in guess
    guess_cl_positions = []
    for index, char in enumerate(guess):
        if char in guess_cl:
            guess_cl_positions.append((index, char))  # Storing as (index, char)

    # If there are letters to check in guess_cl and possible_words is not empty
    if guess_cl_positions and possible_words:
        temp_possible_words = []

        for word in possible_words:
            # Initialize a flag to indicate a match
            match = False
            for index, char in guess_cl_positions:  # Adjusted order here
                # Check if any of the letters in guess_cl_positions matches the same position in the word
                if word[index] == char:
                    match = True
                    break  # Break the loop if a match is found

            # Add the tuple to temp_possible_words if there is no match
            if not match:
                temp_possible_words.append((word))

        # Update possible_words with the filtered list
        possible_words = temp_possible_words
    else:
        pass

def filter_excluded_letter(guess, guess_cl):
    global possible_words
    temp_possible_words = []

    # Create the list of excluded letters
    excluded_letters = []
    for letter in guess:
        if letter.islower() and letter not in guess_cl:
            excluded_letters.append(letter)
            
    #create a list of tuples containing the correct letters and their indexed positions    
    correct_positions = []
    for index, char in enumerate(guess):
        if char not in guess_cl and char.isupper():
            correct_positions.append((index, char.lower()))
    
    #filter through possible words ignoring letters in the correct positions. allows for repeat letters
    for word in possible_words:
        contains_excluded = False
        for index,char in enumerate(word):
             if (index,char) not in correct_positions and char in excluded_letters:
                 contains_excluded = True
                 break # Break the inner loop if an excluded letter is found
             
        # Add the tuple to temp_possible_words if it does not contain any excluded letter
        if not contains_excluded:
            temp_possible_words.append(word)
    possible_words = temp_possible_words

    
def filter_correct_position(guess): 
    global possible_words
    temp_possible_list = []
    #check if there are any uppercase letters and if possible_words is empty
    if any(letter.isupper() for letter in guess) and len(possible_words) == 0:
        #index the guessed word's letters for parsing
        guessed_positions = [(index, char.lower()) for index, char in enumerate(guess) if char.isupper()]
        #search word_list
        for word in word_list:
            # Check if all guessed letters are in the correct positions
            if all((i,c) in guessed_positions and c == word[i] for i,c in guessed_positions):
                possible_words.append(word)
    elif any(letter.isupper() for letter in guess) and len(possible_words) > 0:
        guessed_positions = [(index, char.lower()) for index, char in enumerate(guess) if char.isupper()]
        #if word not in possible_words append to a temp list and replace global list to deduce
        for word in possible_words:
            if all((i,c) in guessed_positions and c == word[i] for i,c in guessed_positions):
                temp_possible_list.append(word)
        possible_words = temp_possible_list
    else: 
        pass
        
def filter_correct_letter(guess_cl):
    # I know it's yucky to use global but I don't know another way.
    global possible_words
    guess_letters = list(guess_cl)
    temp_possible_list = []
    if len(possible_words) == 0:
        for word in word_list:
            # Check if at least one of the specified letters is present in the word
            if all(char in word for char in guess_letters):
                if word not in possible_words:
                # If true, append the word to the filtered list if it's not there
                    possible_words.append(word)
                    
    else:
        #create a new list and replace possible tups 
        for word in possible_words:
            # Check if at least one of the specified letters is present in the word
            if all(char in word for char in guess_letters):
                #if word not in possible_words append to a temp list and replace global list to deduce
                temp_possible_list.append(word)
        possible_words = temp_possible_list
                                         
def possible_guess_results():
    if len(possible_words) == 0:
        try_again = input("\nHow do I say this? \nI have failed you, there are no possible answers.\nTry again? [Y/N]: ")
        if try_again == "Y" or try_again == 'y':
            get_started()
        else:
            quit()
    elif len(possible_words) == 1:
        possible_results = possible_words
        print(f"   *:.Congratuations!.:*\n\n {possible_results} is your answer! \n        ... right?")
        quit()
    else:
        possible_results = []
        for word in possible_words:
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