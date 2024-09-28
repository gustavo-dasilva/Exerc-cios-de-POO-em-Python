class Biblioteca:
    def __init__(self) -> None:
        self.titulo = str
        self.autor = str
        self.ano = int
        self.__id = int

    lista_livros = []  # LISTA QUE VAI SALVAR O DICIONÁRIO COM AS INFORMAÇÕES DOS LIVROS

    def inserir_livro(self, titulo, autor, ano, id):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.__id = id

        livro_info = {'Título': titulo,     #DICIONÁRIO COM AS INFORMAÇÕES DO LIVRO
                      'Autor': autor,
                      'Ano': ano,
                      'ID': id}

        Biblioteca.lista_livros.append(livro_info)    #ADICIONANDO O DICIONÁRIO DENTRO DA LISTA DE LIVROS

    @classmethod
    def fazer_listagem(cls):        #MOSTRAR A LISTAGEM DE LIVROS SALVOS NO ESCOPO DA CLASSE
        return cls.lista_livros


livro1 = Biblioteca()
livro2 = Biblioteca()
livro3 = Biblioteca()


livro1.inserir_livro('Harry Potter', 'JK Rowling', 1997, 1234)

livro2.inserir_livro('A Cabana', 'William P. Young', 2007, 4321)

livro3.inserir_livro('Lua Nova', 'Stephenie Meyer', 2006, 4526)

print(livro3.fazer_listagem())