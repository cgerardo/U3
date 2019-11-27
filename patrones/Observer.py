import abc

class Laptop:

    def __init__(self):
        self._tiendas = set()
        self._estado_laptop = None

    @property
    def estado_laptop(self):
        return self._estado_laptop

    @estado_laptop.setter
    def estado_laptop(self, arg):
        self._estado_laptop = arg

    def agregar(self, tienda):
        tienda._laptop = self
        self._tiendas.add(tienda)

class Tienda(metaclass=abc.ABCMeta):

    def __init__(self):
        self._laptop = None

    @abc.abstractmethod
    def update(self, arg):
        pass


class Comprador(Tienda):

    def update(self, arg):
        self._estado_tienda = arg

def main():
    laptop = Laptop()
    comprador = Comprador()
    laptop._estado_laptop = 000


if __name__ == "__main__":
    main()
