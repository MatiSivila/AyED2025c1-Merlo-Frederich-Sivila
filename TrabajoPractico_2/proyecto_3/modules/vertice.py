import sys

class vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        self.distancia = sys.maxsize
        self.predecesor = None
   
    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion
    
    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]
    
    def asignarDistancia(self, dist):
        self.distancia = dist

    def obtenerDistancia(self):
        return self.distancia

    def asignarPredecesor(self, pred):
        self.predecesor = pred

    def obtenerPredecesor(self):
        return self.predecesor
    
    def __str__(self):
        return f"{self.id} conectadoA: {[x.id for x in self.conectadoA]}"