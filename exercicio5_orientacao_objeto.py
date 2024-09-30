from typing import Type
class Cidade:
    def __init__(self, nome: str, ddd: int) -> None:
        self.nome = nome        #DEIXEI O ATRIBUTO PÚBLICO PARA O OBJETO CONSEGUIR ACESSÁ-LO
        self.__ddd = ddd

    def viajar_niteroi(self):
        print('Indo para a praia!')

    def viajar_belohorizonte(self):
        print('Indo para Inhotim!')

    def viajar_fortaleza(self):
        print('Indo para o Beach Park!')


class Familia:
    def __init__(self, num_membros:int) -> None:
        self.num_membros = num_membros


    def set_viagem(self, cidade: Type[Cidade]):     #ASSOCIAÇÃO DE CLASSES
        if cidade.nome == 'Niterói':
            cidade.viajar_niteroi()
        elif cidade.nome == 'Belo Horizonte':
            cidade.viajar_belohorizonte()
        elif cidade.nome == 'Fortaleza':
            cidade.viajar_fortaleza()



familia = Familia(4)
cidade_escolhida = Cidade('Fortaleza', 41)

familia.set_viagem(cidade_escolhida)



