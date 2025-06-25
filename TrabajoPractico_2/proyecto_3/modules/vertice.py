class Vertice:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__vecinos = []  # Lista de tuplas: (vecino, peso)
        self.__predecesor = None
        self.__distancia = float('inf')

    def agregar_vecino(self, vecino, peso):
        self.vecinos.append((vecino, peso))

    def obtener_vecinos(self):
        return self.vecinos

    def __lt__(self, otro):
        return self.nombre < otro.nombre  # para comparaciones en montículo

    def __str__(self):
        return self.nombre
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def vecinos(self):
        return self.__vecinos
    
    @property
    def predecesor(self):
        return self.__predecesor
    
    @predecesor.setter
    def predecesor(self, predecesor):
        self.__predecesor = predecesor

    @property
    def distancia(self):
        return self.__distancia
    
    @distancia.setter
    def distancia(self,distancia):
        self.__distancia = distancia

   
