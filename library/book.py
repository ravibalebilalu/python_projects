class Book:
    def __init__(self,title,author,isbn,quantity) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

    def display(self):
        print(f"""
                    title: {self.title}
                    author: {self.author}
                    isbn: {self.isbn}
                    quantity: {self.quantity}
             """)
    def __str__(self) -> str:
        return self.title
