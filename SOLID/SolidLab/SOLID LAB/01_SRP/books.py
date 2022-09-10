class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def __repr__(self):
        return 'twa e'


class Library:
    def __init__(self, books: Book):
        self.books = books

    def find_book(self, title):
        if self.books.title == title:
            return self.books
        return 'ne e twa'



