from book import Book
from author import Author
from library import Library
from user_interface import UserInterface

book1 = Book("book1","author1","isbn1",10)
book2 = Book("book2","author2","isbn2",12)
book3 = Book("book3","author3","isbn3",5)

 
author1 = Author("author1",[book1,book2])
author2 = Author("autho2",[book3])


library = Library()
 

userInterface = UserInterface()
signal = 0
while signal != 6:

    signal = userInterface.library_options()
    if signal == 1:
        library.add_book()
    elif signal == 2:
        library.remove_book()
    elif signal== 3:
        library.serach_book()
    elif signal == 4:
        library.display_books()
    elif signal == 5:
        library.display_authors()

 

 


 





