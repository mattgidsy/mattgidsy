def get_user_input():
    guessed_word = input("Enter the guessed word: ").upper()
    correct_positions = input("Enter correct letters in uppercase: ")
    guessed_letters = input("Enter guessed letters out of position: ")

    return guessed_word, correct_positions, guessed_letters

def create_tuple_list(word_list):
    return [(word, list(word)) for word in word_list]

def correct_position_search(guess, guess_cl, tuple_list, possible_tups):
    if not guess_cl:
        return

    guessed_positions = [(char.lower(), index) for index, char in enumerate(guess) if char.isupper()]

    if not possible_tups:
        # Search for correct letter index
        # Search tuple_list for words with the same letter at the same index
        # Append words to possible_tups
        pass
    else:
        # Search for correct letter index
        # Search possible_tups for words with the same letter at the same index
        # Append words to possible_tups
        pass

def correct_letter_search(guess_cl, tuple_list, possible_tups):
    if not guess_cl:
        return

    if not possible_tups:
        # Search tuple_list for words with correct letters
        # Append words with correct letters to possible_tups
        pass
    else:
        # Search possible_tups for words with correct letters
        # Append words to possible_tups
        pass

def excluded_letter_search(guess, guess_cl, possible_tups):
    excluded_letters = set(guess) - set(guess_cl.upper())  # assuming guess is a string
    if not excluded_letters:
        return

    if not possible_tups:
        # Search tuple_list for words without excluded letters
        # Append words without excluded letters to possible_tups
        pass
    else:
        # Search possible_tups for words without excluded letters
        # Append words to possible_tups
        pass

def wrong_position_search(correct_positions, possible_tups):
    # Find letters in the incorrect indexed position (correct letters position)
    # Search possible_tups for words without letters in the incorrectly indexed positions
    pass

def main():
    word_list = ["apple", "table", "chair", "house", "mouse", "plant", "bread", "water", "earth", "music"]
    possible_tups = []
    tuple_list = create_tuple_list(word_list)

    while True:
        guessed_word, correct_positions, guessed_letters = get_user_input()

        correct_position_search(guessed_word, correct_positions, tuple_list, possible_tups)
        correct_letter_search(correct_positions, tuple_list, possible_tups)
        excluded_letter_search(guessed_word, correct_positions, possible_tups)
        wrong_position_search(correct_positions, possible_tups)

        # Display possible_tups or take further actions

if __name__ == "__main__":
    main()