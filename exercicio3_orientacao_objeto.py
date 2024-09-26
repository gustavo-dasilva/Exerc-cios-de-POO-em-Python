import random
from time import sleep

class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome

    def jogar_jokenpo(self):
        placar = {self.nome[0]: 0, 'empate': 0, self.nome[1]: 0}
        while True:
            print('JO-', end='')
            sleep(1)
            print('KEN-', end='')
            sleep(1)
            print('PO!', end='')
            sleep(1)
            jokenpo = ['Pedra', 'Papel', 'Tesoura']
            jogador1 = random.choice(jokenpo)
            print(jogador1, 'x', end=' ')
            jogador2 = random.choice(jokenpo)
            print(jogador2)
            if jogador1 == jogador2:
                print('EMPATE')
                placar['empate'] += 1
            elif jogador1 == 'Pedra' and jogador2 == 'Tesoura' or jogador1 == 'Papel' and jogador2 == 'Pedra' or jogador1 == 'Tesoura' and jogador2 == 'Papel':
                print(f'{self.nome[0]} VENCEU!')
                placar[self.nome[0]] += 1
            else:
                print(f'{self.nome[1]} VENCEU!')
                placar[self.nome[1]] += 1
            print('PLACAR: ', end='')
            for jogador,pontos in placar.items():       #MOSTRAR O DICIONÁRIO SEM AS CHAVES
                print(f'{jogador}: {pontos}', end=' ')
            print()
            op = input('Quer continuar ? [S/N]').upper()
            if op == 'N':
                print('FIM DE JOGO')
                break

amigos = Pessoa(['José', 'Pedro'])
amigos.jogar_jokenpo()
