class Sistema:
    def __init__(self) -> None:
        self.__nome = "Silva's Tech"
        self.__email = 'silvastech@gmail.com'

    def get_nome(self):     #MÉTODO PARA O OBJETO PEGAR O ATRIBUTO PRIVADO "NOME"
        return self.__nome

    def get_email(self):    #MÉTODO PARA O OBJETO PEGAR O ATRIBUTO PRIVADO "EMAIL"
        return self.__email

    def enviar_email(self) -> None:
        print('----EMAIL-----')
        destino = []
        destino.append(input('Destinatário: '))
        while True:
            op = input('Adicionar mais um destinatário? [S/N]').upper()
            if op == 'S':
                destino.append(input('Destinatário: '))
            else:
                break
        titulo = input('Título: ')
        texto = input('Texto: ')
        cont = 0
        print('-----EMAIL------')
        print(titulo)
        print(texto)
        print(f'EMAIL ENVIADO DE {self.get_nome()}, EMAIL: {self.get_email()} COM SUCESSO PARA: ', end='')
        while cont < len(destino):
            print(destino[cont], end=' ')
            if cont < len(destino) - 1: print(end=', ')     #PARA NÃO SAIR A VÍRGULA NA ÚLTIMA REPETIÇÃO
            cont += 1


class Funcionario(Sistema):     #HERANÇA
    def __init__(self, id:int) -> None:
        super().__init__()
        self.id = id


funcionario = Funcionario(8426)
funcionario.enviar_email()



