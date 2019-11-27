from abc import ABC, abstractmethod

class Tareas(ABC):
    @abstractmethod
    def realizar(self):
        pass
    
class Usuario(Tareas):
    print('Preparado para realizar tarea')
    
class ListaTareas(Tareas):
    def __init__(self):
        self._tarea = set()
    def realizacion(self):
        for tar in self._tarea:
            tar._tarea()
    def add(self, tareas):
        self._tarea.add(tareas)
    def remove(self, tareas):
        self._tarea.discard(tareas)

class Tarea(Tareas):
    def realizacion(self):
        print('Realizar tarea')

def main():
    tarea = Tarea()
    lista = ListaTareas()
    lista.add(tarea)
    lista.realizacion()

if __name__ == "__main__":
    main()
