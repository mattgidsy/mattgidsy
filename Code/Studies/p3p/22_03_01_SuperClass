class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f'"{self.title}" by {self.author}'

class EBook(Book):
    def __init__(self, title, author, size):
        Book.__init__(self, title, author)
        self.size = size
    def __str__(self):
        return f'"{self.title}" by {self.author} |{self.size} KB|'

## alternate way of super
class PaperBook(Book):
    def __init__(self, title, author, numPages):
        super().__init__(title, author)
        self.numPages = numPages
    def __str__(self):
        return f'"{self.title}" by {self.author} |{self.numPages} pgs|'
        

myBook = Book('The Odyssey', 'Homer')
myEBook = EBook('Way of Kings', 'Brandon Sanderson', 512)
myPaperBook = PaperBook('Dragon Reborn', 'Robert Jordan', 600)

print(myBook)
print(myEBook)
print(myPaperBook)

