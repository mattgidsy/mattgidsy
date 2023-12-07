##### wordle helper by inquiz #####

#open the file containing a list of 5 letter words
with open("sample_list.txt") as guess_list:
    lines = guess_list.readlines()
    
word_list = [word.strip() for word in lines]
word_tuples = [(word, list(word)) for word in word_list]

possible_guess_lst = word_list[:10]

class GetPossibleGuesses:
    
    def __init__(self,  ):
        
    
    

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
    GetPossibleGuesses
    possible_guess_results()    



get_started()