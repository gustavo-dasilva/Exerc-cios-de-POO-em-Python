from time import sleep
class Elevador:
    def __init__(self, num_elevador: int):
        self.tot_andar = 15
        self.andar_atual = 0
        self.andar_selec = 1
        self.num_elevador = num_elevador        #IDENTIFICADOR DO ELEVADOR

    def usar_elevador(self):
        self.andar_selec = int(input('Selecione o andar: '))
        if self.andar_selec <= 0 or self.andar_selec > self.tot_andar:
            self.msg_erro()
        elif self.andar_selec > self.andar_atual:
            self.subir()
        elif self.andar_selec < self.andar_atual:
            self.descer()
        else:
            self.mesmo_andar()



    def subir(self):
        while self.andar_atual < self.andar_selec:
            self.andar_atual += 1
            print(self.andar_atual)
            sleep(2)



    def descer(self):
        while self.andar_atual > self.andar_selec:
            self.andar_atual -= 1
            print(self.andar_atual)
            sleep(2)



    def msg_erro(self):
        print('Andar inexistente')
        self.usar_elevador()

    def mesmo_andar(self):
        print('Você já está neste andar')
        self.usar_elevador()


class Morador:
    def __init__(self, elevador: Elevador):     #INJEÇÃO DE DEPENDÊNCIA
        self.elevador = elevador

    def chamar_elevador(self):
        print(f'Bem-vindo(a) ao elevador {self.elevador.num_elevador}')
        self.elevador.usar_elevador()



elevador1 = Elevador(1)
elevador2 = Elevador(2)

morador = Morador(elevador1)
morador.chamar_elevador()

morador2 = Morador(elevador2)
morador2.chamar_elevador()

morador3 = Morador(elevador1)
morador.chamar_elevador()

morador4 = Morador(elevador2)
morador4.chamar_elevador()

morador5 = Morador(elevador1)
morador5.chamar_elevador()

morador6 = Morador(elevador2)
morador6.chamar_elevador()


