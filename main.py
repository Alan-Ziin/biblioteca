from classes import Book, Library

book_robert = Book("O cachorro","Alan","2015")

bookcase = Library()
bookcase.add_books(book_robert)
bookcase.show_books()