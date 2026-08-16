from classes import Book, Library

book_robert = Book("Cachorro","Robbert","2015")
book_duda = Book("Gato","Duda","2025")
book_leoncio = Book("Papagaio","Leoncio","2016")

bookcase = Library()

bookcase.add_books(book_robert)
bookcase.add_books(book_robert)

bookcase.add_books(book_duda)
bookcase.add_books(book_leoncio)

bookcase.show_books()
bookcase.len_bookcase()

bookcase.remove_books(book_robert)
bookcase.show_books()

bookcase.len_bookcase()
