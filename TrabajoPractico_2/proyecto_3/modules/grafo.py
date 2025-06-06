from modules.vertice import Vertice

class Grafo:
    def __init__(self):
        self.listaVertices = {}
    
    def agregarVertice(self, clave):
        if clave not in self.listaVertices:
            self.listaVertices[clave] = Vertice(clave)
        return self.listaVertices[clave]
    
    def obtenerVertice(self, clave):
        return self.listaVertices.get(clave)
    
    def agregarArista(self, de, a, costo=0):
        v1 = self.agregarVertice(de)
        v2 = self.agregarVertice(a)
        v1.agregarVecino(v2, costo)
        v2.agregarVecino(v1, costo)

    def __iter__(self):
        return iter(self.listaVertices.values())