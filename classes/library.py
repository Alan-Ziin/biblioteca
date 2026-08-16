class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        for duplicate in self.books:
            if duplicate == book:
                return print("Erro, o livro já existe\n")
        self.books.append(book)


    def show_books(self):
        if len(self.books) == 0:
            return print("The bookcase is empty\n")
        else:
            print("Books in bookcase")
            for l in self.books:
                print(f"Name of Book: {l.titulo}\tActor of Book: {l.autor}\tPublication year of Book: {l.ano_publicacao}\n")

            
    def remove_books(self, book):
        for t in self.books:
            if t == book:
                print(f"#################\nRemoving {book.titulo}\n#################\n")
                self.books.remove(t)


    def len_bookcase(self):
        result = len(self.books)
        if result == 0:
            print("The bookcase is empty\n")
            return result
        else:
            print(f"Have {result} books in bookcase.\n")
            return result