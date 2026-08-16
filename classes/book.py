class Book:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __eq__(self, value):
        return self.titulo == value.titulo and self.autor == value.autor and self.ano_publicacao == value.ano_publicacao