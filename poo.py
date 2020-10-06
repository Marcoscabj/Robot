class Empleado():
    def __init__(self,nombre,sueldo,edad):
        self.nombre=nombre
        self.sueldo=sueldo
        self.edad= edad
    
    def Sueldo(self,descuentos,bonos):
        return self.sueldo - descuentos- bonos

class Agente(Empleado):    
    def __init__(self,nombre,sueldo,edad,numero,piso):
        super().__init__()
