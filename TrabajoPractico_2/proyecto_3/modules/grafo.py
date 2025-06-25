from vertice import Vertice
from cola_prioridad import ColaPrioridad

class Grafo:
    def __init__(self):
        self.vertices = []  # lista de objetos Vertice

    def obtener_vertice(self, nombre):
        for v in self.vertices:
            if v.nombre == nombre:
                return v
        return None

    def agregar_vertice(self, nombre):
        if not self.obtener_vertice(nombre):
            self.vertices.append(Vertice(nombre))

    def agregar_arista(self, origen, destino, peso):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        v_origen = self.obtener_vertice(origen)
        v_destino = self.obtener_vertice(destino)
        v_origen.agregar_vecino(v_destino, peso)
        v_destino.agregar_vecino(v_origen, peso)  # Grafo no dirigido

    def prim(self, inicio_nombre):
        inicio = self.obtener_vertice(inicio_nombre)
        if inicio is None:
            return []

        for v in self.vertices:
            v.distancia = float('inf')
            v.predecesor = None

        inicio.distancia = 0
        visitados = []
        cola = ColaPrioridad()
        cola.insertar((0, inicio, inicio))  # (peso, origen, destino)

        mst = []

        while not cola.esta_vacia():
            peso, origen, destino = cola.atender()
            if destino in visitados:
                continue
            visitados.append(destino)
            if destino != origen:
                mst.append((origen.nombre, destino.nombre, peso))
            for vecino, costo in destino.obtener_vecinos():
                if vecino not in visitados and costo < vecino.distancia:
                    vecino.distancia = costo
                    vecino.predecesor = destino
                    cola.insertar((costo, destino, vecino))

        return mst