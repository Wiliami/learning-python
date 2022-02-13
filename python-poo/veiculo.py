class Veiculo :

    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.roda = rodas
        self.marca = marca
        self.tanque = tanque

    def abatecer(self, litros):
        self.tanque += litros