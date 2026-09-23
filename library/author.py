class Author:
    def __init__(self,name,books_written=[]) -> None:
        self.name = name
        self.books_written = books_written
    def display(self):
        print( f"Name:{self.name}")
        print(f"Books written by {self.name}:")
        for book in self.books_written:
            print(book)