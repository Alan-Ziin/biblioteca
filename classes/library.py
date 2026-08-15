class Library:
    def __init__(self):
        self.books = []

    def add_books(self, livro):
        self.books.append(livro)

    def show_books(self):
        for l in self.books:
            print(f"Name of Book: {l.titulo}\nActor of Book: {l.autor}\nPublication year of Book: {l.ano_publicacao}")
