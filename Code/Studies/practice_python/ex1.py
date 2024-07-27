class User:
    def __init__(self, name, bday):
        self.name = name
        self.bday = bday
    
    def hundred_yr_calc(self):
        year = int(self.bday[-4:])
        hundred = year + 100
        print(f" The great Zoltar says that you, {user.name}, will turn 100 years old in {hundred} ")
        
    
        
players = int(input("how many people do we have here?\n"))

for i in range(players):
    name = input("What is your name?\n")
    bday = input("What is your birthday (mm/dd/yyyy)\n")
    user = User(name,bday)
    user.hundred_yr_calc()
    copies = int(input("How many copies of your fortune would you like?\n"))
    for i in range(copies):
        user.hundred_yr_calc()

print("\nThanks for playing!")       