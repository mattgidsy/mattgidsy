# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

#     If the number is a multiple of 4, print out a different message.
#     Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
class Game:
    def __init__(self, answer:str) -> str:
        self.answer = answer
        
    def parse(self) -> int:
        try:
           self.answer = int(self.answer)
        except:
            print("Please only use integers.")
            start_game()
    
def start_game():           
    while True:
        game = Game()
        game.answer = input("Type 'quit' to exit.\nPick a number(0-100) and recieve a fortune\n")

        if num == "quit":
            print("Game Over\n\n")
            quit()
        elif int(num) % 4 == 0:
            print("Zoltar predicts you will weather all four seasons of change.\n")
        elif int(num) == 2:
            print("Zoltar believes that you are an even match\n")
        else:
            print("Zoltar finds you to be unique, one of a kind.\n")
            


        
    