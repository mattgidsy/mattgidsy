LETTERS = 'ABCDEFGH'
VOWELS = 'AEIOU'

guessed = ['B','C','D','F','G','H']

guess_lst = []
if 2 < 250:
    for c in LETTERS:
        if c in guessed and c not in VOWELS:
            print('pass')
    print(guess_lst)

