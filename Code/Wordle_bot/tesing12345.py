def read_word_list(file_path):
    with open(file_path) as guess_list:
        lines = guess_list.readlines()
    return [word.strip() for word in lines]

def create_word_tuples(word_list):
    return [(word, list(word)) for word in word_list]

def check_correct_position(guess, possible_tups):
    if any(letter.isupper() for letter in guess):
        guessed_positions = [(char.lower(), index) for index, char in enumerate(guess) if char.isupper()]
        return [(word, letters) for word, letters in possible_tups if all((g, i) in guessed_positions and g == letters[i] for g, i in guessed_positions)]
    return possible_tups

def check_correct_letter(guess_cl, possible_tups):
    guess_letters = list(guess_cl)
    return [(word, letters) for word, letters in possible_tups if all(char in word for char in guess_letters)]

def possible_guess_results(possible_tups):
    if not possible_tups:
        try_again = input("\nHow do I say this? \nI have failed you, there are no possible answers.\nTry again? [Y/N]: ")
        return try_again.lower() == "y"
    else:
        possible_results = [word for word, _ in possible_tups]
        print(possible_results)
        return False

def get_started():
    print("\n   ###### Welcome to Wordle_Helper_Bot! ###### \n\nInput all incorrectly positioned letters in lowercase \n   Input correctly positioned letters in UPPERCASE")
    print("\n   ###### Welcome to Wordle_Helper_Bot! ######")

    word_list = read_word_list("Code\Wordle_bot\sample_list.txt")
    word_tuples = create_word_tuples(word_list)
    possible_tups = []

    while True:
        guess1 = input("\nInput your first guess:\n")
        guess1_cl = input("\nWhich letters are in the word but out of position?:\n")

        possible_tups = check_correct_position(guess1, possible_tups)
        possible_tups = check_correct_letter(guess1_cl, possible_tups)

        if possible_guess_results(possible_tups):
            break

get_started()