class Computador:
    def __init__(self, marca, preco, ano):
        self.marca = marca
        self.preco = preco
        self.ano = ano

    def Ligar(self):
        input('estou ligando...')

    def Desligar(self):
        input('deseja mesmo desligar o computador?')
        print('estou desligando...')

    def ExibirInformarcoesDesteComputador(self):
        print(self.marca, self.preco, self.ano)
    


Computador1 = Computador('asus', '1800', '2021')
Computador1.Ligar()
Computador1.Desligar()
Computador1.ExibirInformarcoesDesteComputador()
