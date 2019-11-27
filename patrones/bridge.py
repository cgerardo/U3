from abc import ABC, abstractmethod

class Carro(ABC):

    @abstractmethod
    def carro(self):
        pass

class Carros(ABC):
    def __init__(self, carro):
        self.carro = carro

    @abstractmethod
    def size(self):
        pass

class Atras(Carros):
    def __init__(self, carro):
        super(atras, self).__init__(carro)

    def size(self):
        self.carro.carro(self)

class Adelante(Carros):
    def __init__(self, carro):
        super(A, self).__init__(carro)

    def size(self):
        self.carro.carro(self)

class BMW(Carro):
    def carro(self):
        print("BMW")

class Audi(Carro):
    def carro(self):
        print("Audi")

class main():
    bmw = Atras(BMW)
    bmw.size()
    audi = Adelante(Audi)
    audi.size()
