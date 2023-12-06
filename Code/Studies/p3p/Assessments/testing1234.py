LETTERS = 'ABCDEFGH'
VOWELS = 'AEIOU'

guessed = ['B','C','D','F','G','H']

guess_lst = []
if 2 < 250:
    for c in LETTERS:
        if c in guessed and c not in VOWELS:
            print('pass')
    print(guess_lst)

guess_lst = []
        no_guess = []
        if self.prizeMoney < VOWEL_COST:
            for c in LETTERS:
                if c in guessed:
                    no_guess.append(c)
                elif c in VOWELS:
                    no_guess.append(c) 
            return no_guess