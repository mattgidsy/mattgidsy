def filter_list_by_correct_position(word_list, guess, correct_position) -> list:
    ...
    return filtered_list

def filter_list_by_guess(word_list, guess, correct_position, correct_letter) -> list:
    filtered = filter_list_by_correct_position(word_list, guess, correct_position)
    filtered = filter_list_by_correct_letter(word_list, guess, correct_letter)
    ...
    return filtered

def basic_test():
    pre_list = ["games", "round"]
    filtered_list = filter_list_by_guess(pre_list, "r", [True,])
    assert(len(filtered_list) == 1)
    assert filtered_list == ["games"]
    
def game():
    game_won = False
    word_list = init_word_list()
    while not game_won:
        structured_guess = read_user_input()
        guess, correct_position, correct_letter = parse_structured_guess(structured_guess)
        word_list = filter_list_by_guess(word_list, guess, correct_position, correct_letter)
        print(word_list)
        
        
"Sl.ate"