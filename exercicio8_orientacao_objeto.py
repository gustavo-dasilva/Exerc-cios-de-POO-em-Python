'''
A segunda calculadora faz uma lógica diferente para o cálculo do segundo número.
O segundo número é elevado ao cubo e então seu resultado é subtraído do valor inicial que ele recebeu.
Após isso, o resultado é multiplicado por 2 e somado à constante 2.
Assim, tem-se a resposta definitiva para o segundo número.


The second calculator uses a different logic for calculating the second number.
The second number is raised to the power of three, and then its result is subtracted from the initial value it received.
After that, the result is multiplied by 2 and added to the constant 2.
Thus, we have the definitive answer for the second number.
'''

class Calculadora1:
    def __init__(self) -> None:
        self.numero1 = None
        self.numero2 = None
        self.__constante1 = 5.7
        self.constante2 = 4.2

    def resultado_numero1(self):        #CÁLCULO DO PRIMEIRO NÚMERO
        resp_provisoria1 = self.numero1 * 5 / 8
        resp_provisoaria2 = pow(resp_provisoria1,(1/2))
        resp_definitiva = resp_provisoaria2 ** 3
        return resp_definitiva

    def resultado_numero2(self):        #CÁLCULO DO SEGUNDO NÚMERO
        resp_provisoria = self.numero2 ** 2 + self.numero2
        resp_definitiva = resp_provisoria * 2 / 5 + self.__constante1
        return resp_definitiva

    def resultado_final(self):      #CÁLCULO FINAL
        resultado = (self.resultado_numero1() + self.resultado_numero2()) * self.constante2
        return resultado

    def calcular(self):
        self.numero1 = int(input('Número 1: '))
        self.numero2 = int(input('Número 2: '))
        print('CALCULANDO...')
        resposta_final = self.resultado_final()
        return f'Resultado: {resposta_final}'


class Calculadora2(Calculadora1):       #HERANÇA
    def __init__(self):
        super().__init__()
        self.constante2 = 1.2

    def resultado_numero2(self):        #POLIMORFISMO
        resp_provisoria = self.numero2 ** 3 - self.numero2
        resp_definitiva = resp_provisoria * 2 + self.constante2
        return resp_definitiva


calculadora1 = Calculadora1()
print(calculadora1.calcular())

calculadora2 = Calculadora2()
print(calculadora2.calcular())

