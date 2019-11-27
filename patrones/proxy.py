from abc import ABC, abstractmethod

class ComidaAlumno(ABC):

    @abstractmethod
    def Lista(self):
        pass

class FamiliarAlumno(ComidaAlumno):
    def Lista(self):
        print("Lleva una lista de comida como:"+
              "Chorizo,Azúcar,Café,Chocolate,"+
              "Pastillas,Sal,Pan,Pasta Dental")
        
class Proxy(ComidaAlumno):
     def __init__(self,familiar_alumno:FamiliarAlumno):
        self._FamiliarAlumno = FamiliarAlumno()

     def Lista(self):

        if self.recibe():
            self._FamiliarAlumno.Lista()
            self.acceso()

     def recibe(self):
        print("La lista de productos permitidos solo sera: Sal,Pan,Pasta Dental,Pastillas")
        return True

     def acceso (self):
        print("Tiren los productos restantes")


def Alumno(ComidaAlumno):
    ComidaAlumno.Lista()

if __name__ == "__main__":
    Familiar = FamiliarAlumno()
    Alumno(Familiar)

    print("")

    entrega = Proxy(FamiliarAlumno)
    Alumno(entrega)

    
