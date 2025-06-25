class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = []  # Lista de tuplas: (vecino, peso)
        self.predecesor = None
        self.distancia = float('inf')

    def agregar_vecino(self, vecino, peso):
        self.vecinos.append((vecino, peso))

    def obtener_vecinos(self):
        return self.vecinos

    def __lt__(self, otro):
        return self.nombre < otro.nombre  # para comparaciones en montículo

    def __str__(self):
        return self.nombre