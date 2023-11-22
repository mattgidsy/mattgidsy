class BankAccount:
    def __init__(self,name:str, ammount:float):
        self.name = name
        self.amt = ammount
    def __str__(self) -> str:
        return f"Your account, {self.name}, has {self.amt} dollars."

t1 = BankAccount("Bob",100)
print(t1)