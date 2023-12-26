#open the file containing a list of 5 letter words
with open("Code\Wordle_bot\guess_list.txt") as guess_list:
    lines = guess_list.readlines()

#iterate through the word list (this one contains 5 letter words for wordle)   
#create word tuples to use for parsing ie: ('apple', ['a','p','p','l','e'])
word_list = [word.strip() for word in lines]
#word_list = [(word, list(word)) for word in word_list]
possible_words = []

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
    
answer = "slAte"
filter_correct_position(answer)
print(possible_words)