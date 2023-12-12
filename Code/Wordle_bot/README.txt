this bot is made to help assist in solving wordle word puzzles.
you will input your guesses and the bot will give you possible answers for you to choose for your next guess.

Basic logic Outline 12/9

1. Ask for the word guessed, ask user to capitalize words in the correct position
2. input the guessed word
3. Ask for the correct letters that are out of position
4. input guessed letters that are out of position
5. create a tuple_list as a list of tuples (word, list of letters)  from words on the  the word_list
6. create empty possible_tups list
7. correct position search (guess, guess_cl)
	1. if no capitalized letters,
		1. pass 
	2. if capitalized letters and possible_tups is empty:
		1. search for the correct letter index 
		2. search tuple_list for words with the same letter at the same index
		3. append the words to possible_tups
	3. if capitalized words and possible_tups has tups
		1. search for the correct letter index 
		2. search possible_tups for words with the same letter at the same index
		3. append the words to possible_tups
8. correct letter search (guess, guess_cl)
	1. if guess_cl is empty
		1. pass 
	2. if possible_tups is empty:
		1. search tuple_list for words with correct letters
			1. append words with correct letters to tups list
	3. else:
		1. search possible_tups for words with correct letters
9. excluded letter search:
	1. excluded letters = guess - captital letters - correct letter #maybe needs to be global
	2. if possible_tups is empty:
		1. search tuple_list for words without excluded letters
	3. else:
		1. search possible_tups for words without excluded letters
10. wrong position search:
	1. find letters in the incorrect indexed position (correct letters position) #global variable to keep track of guess letter position
		1. search possible_tups for words without letters in the incorrectly indexed positions
11. print a list of possible words to guess 
12. repeat until there is only one possible word left in possible_tups