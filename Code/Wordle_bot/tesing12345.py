
def filter_excluded_letter(guess, guess_cl):
    global possible_tups
    temp_tups = []

    # Create the list of excluded letters without using list comprehension
    excluded_letters = []
    for letter in guess:
        if letter.islower() and letter not in guess_cl:
            excluded_letters.append(letter)
            
    # Create 2 lists of tuples, containing the indexed characters of the incorrect guess positions and the correct guess positions      
    incorrect_guess_positions = []
    correct_positions = []
    for index, char in enumerate(guess):
        if char not in guess_cl and char.islower():
            incorrect_guess_positions.append((index, char))
        elif char not in guess_cl and char.isupper():
            correct_positions.append((index, char.lower()))
    
    for word, letter in possible_tups:
        
    # Iterate over each tuple in possible_tups
    for word, letters in possible_tups:
        # Check if the word contains any excluded letter
        contains_excluded = False
        for char in excluded_letters:
            if char in word:
                contains_excluded = True
                break  # Break the inner loop if an excluded letter is found

        # Add the tuple to temp_tups if it does not contain any excluded letter
        if not contains_excluded:
            temp_tups.append((word, letters))

    # Reassign possible_tups to the filtered list
    possible_tups = temp_tups

def filter_incorrect_positions(guess, guess_cl):
    global possible_tups

    # Create the list of tuples (index, letter) for each letter in guess_cl and its corresponding index in guess
    guess_cl_positions = []
    for index, char in enumerate(guess):
        if char in guess_cl:
            guess_cl_positions.append((index, char))  # Storing as (index, char)

    # If there are letters to check in guess_cl and possible_tups is not empty
    if guess_cl_positions and possible_tups:
        temp_tups_list = []

        for word, letters in possible_tups:
            # Initialize a flag to indicate a match
            match = False
            for index, char in guess_cl_positions:  # Adjusted order here
                # Check if any of the letters in guess_cl_positions matches the same position in the word
                if word[index] == char:
                    match = True
                    break  # Break the loop if a match is found

            # Add the tuple to temp_tups_list if there is no match
            if not match:
                temp_tups_list.append((word, letters))

        # Update possible_tups with the filtered list
        possible_tups = temp_tups_list
    else:
        pass

def filter_excluded_letter(guess, guess_cl):
    global possible_tups
    temp_tups = []

    # Create the list of excluded letters without using list comprehension
    excluded_letters = []
    for letter in guess:
        if letter.islower() and letter not in guess_cl:
            excluded_letters.append(letter)

    # Iterate over each tuple in possible_tups
    for word, letters in possible_tups:
        # Check if the word contains any excluded letter
        contains_excluded = False
        for char in excluded_letters:
            if char in word:
                contains_excluded = True
                break  # Break the inner loop if an excluded letter is found

        # Add the tuple to temp_tups if it does not contain any excluded letter
        if not contains_excluded:
            temp_tups.append((word, letters))

    # Reassign possible_tups to the filtered list
    possible_tups = temp_tups
