class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def construirMonticulo(self, lista):
        self.cola = sorted(lista, key=lambda x: x[0])

    def estaVacia(self):
        return len(self.cola) == 0

    def eliminarMin(self):
        return self.cola.pop(0)[1]

    def decrementarClave(self, vertice, nuevaDistancia):
        for i, (dist, v) in enumerate(self.cola):
            if v == vertice:
                self.cola[i] = (nuevaDistancia, v)
                break
        self.cola.sort(key=lambda x: x[0])

    def __contains__(self, vertice):
        return any(v == vertice for _, v in self.cola)