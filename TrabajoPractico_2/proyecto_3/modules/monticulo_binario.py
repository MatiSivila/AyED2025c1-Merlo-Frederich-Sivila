import math

class MonticuloBinario:
    def __init__(self):
        self.__lista_monticulo = [-math.inf]  # Elemento ficticio para facilitar cálculos
        self.__tamano_actual = 0

    @property
    def tamano(self):
        return self.__tamano_actual

    @property
    def lista_monticulo(self):
        return self.__lista_monticulo.copy()

    def __infilt_arriba(self, i):
        while i // 2 > 0:
            if self.__lista_monticulo[i] < self.__lista_monticulo[i // 2]:
                self.__lista_monticulo[i], self.__lista_monticulo[i // 2] = self.__lista_monticulo[i // 2], self.__lista_monticulo[i]
            i = i // 2

    def __infilt_abajo(self, i):
        while (i * 2) <= self.__tamano_actual:
            hm = self.__hijo_min(i)
            if self.__lista_monticulo[i] > self.__lista_monticulo[hm]:
                self.__lista_monticulo[i], self.__lista_monticulo[hm] = self.__lista_monticulo[hm], self.__lista_monticulo[i]
            i = hm

    def __hijo_min(self, i):
        if i * 2 + 1 > self.__tamano_actual:
            return i * 2
        else:
            if self.__lista_monticulo[i * 2] < self.__lista_monticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insertar(self, k):
        self.__lista_monticulo.append(k)
        self.__tamano_actual += 1
        self.__infilt_arriba(self.__tamano_actual)

    def eliminar_min(self):
        if self.esta_vacio():
            raise IndexError("No se puede eliminar de un montículo vacío.")
        valor_eliminado = self.__lista_monticulo[1]
        self.__lista_monticulo[1] = self.__lista_monticulo[self.__tamano_actual]
        self.__tamano_actual -= 1
        self.__lista_monticulo.pop()
        self.__infilt_abajo(1)
        return valor_eliminado

    def esta_vacio(self):
        return self.__tamano_actual == 0