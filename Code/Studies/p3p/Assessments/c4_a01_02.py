class AppleBasket:
    def __init__(self,color:str, qty:int):
        self.apple_color = color
        self.apple_quantity = qty
    def increase(self):
        self.apple_quantity += 1
        return self.apple_quantity
    def __str__(self):
        return f"A basket of {self.apple_quantity} {self.apple_color} apples."
        
basket1 = AppleBasket("green",4)
print(basket1)
basket1.increase()
print(basket1)        
        