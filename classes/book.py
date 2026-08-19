class Book:
    def __init__(self, titulo, autor, ano_publicacao, idBook):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.idBook = idBook

    def __eq__(self, value):
        return self.titulo == value.titulo and self.autor == value.autor and self.ano_publicacao == value.ano_publicacao

    def __str__(self):
        return f'Book ID: {self.idBook}\nTitle:{self.titulo}\nActor:{self.autor}\nYear Publication:{self.ano_publicacao}'