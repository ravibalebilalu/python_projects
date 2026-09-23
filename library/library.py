from book import Book
from author import Author
class Library:
    def __init__(self) -> None:
        self.book_shelf = []

    def add_book(self):
        title = input("Enter title:\t")
        author_name = input("Enter author name:\t")
        isbn = input("Enter isbn \t")
        
        author = Author(name=author_name)

        while True:
            
            quantity = input("Enter quantity:\t")
            if quantity.isdigit():
                book =  Book(title,author,isbn,int(quantity))
                self.book_shelf.append(book)
                author.books_written.append(book)
                print([book.title for book in author.books_written if author_name == book.author.name])
                
                break
            else:
                print("Quantity must be a positive whole number. Please try again.")

        

             

    def remove_book(self):
        if self.book_shelf:
            while True:
                try:
                    book_title = input("Enter book title\t")
                    book = [book for book in self.book_shelf if book.title == book_title][0]
                    self.book_shelf.remove(book)
                    print(f"{book} is removed from shelf")
                    break
                except Exception:
                    print("Ensure book title")
        else:
            print("Book shelf is empty!")

    def serach_book(self ):
        while True:
            
            try:
                book_title = input("Enter book title:\t")
                for book in self.book_shelf:
                    if book.title == book_title.strip() or book.author.name ==book_title.strip():
                        print(f"Book {book.title} by {book.author.name} is found!")
                        return book
                raise ValueError("Book not found!")
            except ValueError:
                print("Not found!")
                return None

    def display_books(self):
        if self.book_shelf:
            for book in self.book_shelf:
                print(f"Title: {book.title}")
                print(f"Author: {book.author.name}")
                print(f"Isbn: {book.isbn}")
                print(f"Quantity: {book.quantity}")
                print("---------------------------------------------------------")
        else:
            print("There is no books! Consider adding some......")

    def display_authors(self):
        print("Author's list from library:")
        authors = [ book.author.name  for book in self.book_shelf]
            
        authors = list(set(authors))
        for author in authors:
            print(f"Author: {author}")
            print("Books written:")
            for book in self.book_shelf:
                if book.author.name == author:
                    print(book.title)
            print("---------------------------------------------------------")
