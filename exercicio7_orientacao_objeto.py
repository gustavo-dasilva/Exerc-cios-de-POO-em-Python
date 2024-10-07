'''
Calculadora que recebe dois números. O primeiro é multiplicado por 5, dividido por 8 e do resultado é tirado a raíz quadrada e elevado ao cubo.
O segundo número é elevado ao quadrado e então somado ao seu valor inicial recebido. O resultado é multiplicado por 2, dividido por 5 e somado a uma constante de 5.7.
No final, os resultado anteriores são somados e então multiplicados por uma constante de 4.2
'''

'''
Calculator that receives two numbers. The first number is multiplied by 5, divided by 8, and then the square root of the result is taken and raised to the power of three. 
The second number is squared and then added to its initial value. The result is multiplied by 2, divided by 5, and added to a constant of 5.7. 
In the end, the previous results are summed and then multiplied by a constant of 4.2.
'''
class Calculadora:
    def __init__(self) -> None:
        self.numero1 = None
        self.numero2 = None
        self.__constante1 = 5.7
        self.__constante2 = 4.2

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
        resultado = (self.resultado_numero1() + self.resultado_numero2()) * self.__constante2
        return resultado

    def calcular(self):
        self.numero1 = int(input('Número 1: '))
        self.numero2 = int(input('Número 2: '))
        print('CALCULANDO...')
        resposta_final = self.resultado_final()
        return f'Resultado: {resposta_final}'

calculadora = Calculadora()
print(calculadora.calcular())


