class Visitor:
    
    def VisitMaestro(self, elem):
        pass
    def VisitAlumno(self, elem):
        pass
    
class ConcreteVisitor1(Visitor):
    
    def VisitMaestro(self, elem):
        print("Maestro")
        
    def VisitAlumno(self, elem):
        print("Alumno")
    
    
class ConcreteVisitor2(Visitor):
    
    def VisitMaestro(self, elem):
        print("Maestro")
        
    def VisitAlumno(self, elem):
        print("Alumno")

class Persona:
    def Recibir(self,v):
        pass
   
class Maestro(Persona):
    def Recibir(self,v):
        print("Maestro recibido")
        v.VisitMaestro(self)

class Alumno(Persona):
    def Recibir(self,v):
        print("Alunmo recibido")
        v.VisitAlumno(self)
        
class Cliente():        
    n=[]
    maestro=Maestro()
    alumno=Alumno()
    n.append(maestro)
    n.append(alumno)
    v1=ConcreteVisitor1()
    v2=ConcreteVisitor2()

    for i in n:
        i.Recibir(v1)
        i.Recibir(v2)
    

       
    
        
        
        
    
    

