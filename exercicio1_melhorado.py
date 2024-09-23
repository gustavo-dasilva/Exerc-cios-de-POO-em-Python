from abc import ABC,abstractmethod
from time import sleep
class Elevador_Interface(ABC):

    @abstractmethod
    def usar_elevador(self):
        pass

class Edificio(Elevador_Interface):
    def __init__(self):
        self.__andar_atual = 0
        self.__andar_selec = 0
        self.__tot_andares = 12


    def get_andar(self):
        return self.__andar_atual

    def set_andar(self):
        self.__andar_selec = int(input('Selecione o andar: '))

    def usar_elevador(self):
        while True:
            if self.__andar_selec == self.get_andar():    #SE JÁ ESTIVER NO MESMO ANDAR SELECIONADO
                self.aviso_elevador()
            elif self.__andar_selec > self.__tot_andares:   #ANDAR NÃO EXISTENTE
                self.erro_elevador()
            elif self.__andar_selec > self.get_andar():   #ELEVADOR SUBINDO
                self.subir_elevador()
            else:
                self.descer_elevador()                      #ELEVADOR DESCENDO

            self.set_andar()
            sleep(1)
            print('Porta fechando...')
            sleep(2)
            if self.__andar_selec <= 0:
                break


    def subir_elevador(self):

        while self.__andar_selec > self.get_andar():
            self.__andar_atual += 1
            print(f'{self.__andar_atual}º andar')
            sleep(2)
        print('Porta abrindo...')
        sleep(2)

        
    def descer_elevador(self):

        while self.__andar_selec < self.get_andar():
            self.__andar_atual -= 1
            print(f'{self.__andar_atual}º andar')
            sleep(2)
        print('Porta abrindo...')
        sleep(2)

        
    def erro_elevador(self):
        print('Andar inexistente.')
        
    def aviso_elevador(self):
        print(f'Você já está no {self.__andar_selec}º andar')



morador = Edificio()

morador.set_andar()
morador.usar_elevador()
