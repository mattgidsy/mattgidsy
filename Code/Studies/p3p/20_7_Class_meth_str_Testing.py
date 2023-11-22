class Cereal:
    def __init__(self, name, brand, fiber):
        self.n = name
        self.b = brand
        self.f = fiber
    def __str__(self):
        return f"{self.n} cereal is produced by {self.b} and has {self.f} grams of fiber in every serving!"

c1 = Cereal("Corn Flakes", "Kellogg's", '2')
c2 = Cereal('Honey Nut Cheerios', 'General Mills', '3')

print(c1)
print(c2)