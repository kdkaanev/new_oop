class Book:
    def __init__(self,name ,author , pages):
        self.name = name
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.name}{self.author}{self.pages}"


book = Book('swfw', 'gfdgf', 200)
print(book)