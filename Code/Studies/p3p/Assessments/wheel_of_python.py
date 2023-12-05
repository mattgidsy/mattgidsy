import random
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

class WOFPlayer():
    prizeMoney = 0
    prizes = []
    
    def __init__(self, name):
        self.name = name

    def addMoney(self, amt):
        self.prizeMoney += amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        self.prizes.append(self.prize)
    
    def __str__(self):
        return f"{self.name} (${self.prizeMoney})"

class WOFHumanPlayer(WOFPlayer):
    
    def getMove(self, category, obscuredPhrase, guessed):
        answer = input(f"{self.name} has ${self.prizeMoney} \n \nCategory: {category} \nPhrase: {obscuredPhrase} \nGuessed: {guessed} \n \nGuess a letter, phrase, or type 'exit' or 'pass': ")
        return answer
    
class WOFComputerPlayer(WOFHumanPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
    
    def smartCoinFlip(self):
        if random.randint(1,10) > self.difficulty:
            return False
        else:
            return True
    def getPossibleLetters(self,guessed):
        guess_lst = []
        if self.prizeMoney < VOWEL_COST:
            for c in LETTERS:
                if c in guessed and c not in VOWELS:
                    return 'pass'
                else:
                    guess_lst.append(c)
                return guess_lst
        else:
            for c in LETTERS:
                if c not in guessed:
                    guess_lst.append(c)
            return guess_lst
    def getMove(self, category, obscuredPhrase, guessed):
        if self.getPossibleLetters(guessed) == None:
            return 'pass'
        else:
            if self.smartCoinFlip() == False:
                letters = [letter for letter in LETTERS]
                return random.choice(letters)
            else:
                for char in reversed(self.SORTED_FREQUENCIES): 
                    if char in self.getPossibleLetters(guessed):
                        return char
                    
                 
                
            
    