class Nodo:  
    def __init__(self, dato, anterior=None, siguiente=None):
        self.dato = dato
        self.anterior = anterior
        self.siguiente = siguiente

class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self._largo = 0

    def esta_vacia(self):
        return self._largo == 0

    def __len__(self):
        return self._largo

    def agregar_al_inicio(self, item):
        nuevo = Nodo(item, None, self.primero)
        if self.primero:
            self.primero.anterior = nuevo
        else:
            self.ultimo = nuevo
        self.primero = nuevo
        self._largo += 1

    def agregar_al_final(self, item):
        nuevo = Nodo(item, self.ultimo, None)
        if self.ultimo:
            self.ultimo.siguiente = nuevo
        else:
            self.primero = nuevo
        self.ultimo = nuevo
        self._largo += 1

    def insertar(self, item, posicion=None):
        if posicion is None or posicion >= self._largo:
            self.agregar_al_final(item)
        elif posicion < 0:
            raise IndexError("Posición inválida")
        elif posicion == 0:
            self.agregar_al_inicio(item)
        else:
            actual = self.primero
            for _ in range(posicion):
                actual = actual.siguiente
            nuevo = Nodo(item, actual.anterior, actual)
            actual.anterior.siguiente = nuevo
            actual.anterior = nuevo
            self._largo += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise IndexError("Lista vacía")
        if posicion is None:
            posicion = self._largo - 1
        if posicion < 0 or posicion >= self._largo:
            raise IndexError("Posición inválida")

        if posicion == 0:
            extraido = self.primero.dato
            self.primero = self.primero.siguiente
            if self.primero:
                self.primero.anterior = None
            else:
                self.ultimo = None
        elif posicion == self._largo - 1:
            extraido = self.ultimo.dato
            self.ultimo = self.ultimo.anterior
            if self.ultimo:
                self.ultimo.siguiente = None
            else:
                self.primero = None
        else:
            actual = self.primero
            for _ in range(posicion):
                actual = actual.siguiente
            extraido = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
        self._largo -= 1
        return extraido

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.primero
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self):
        actual = self.primero
        self.primero, self.ultimo = self.ultimo, self.primero
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior

    def concatenar(self, otra_lista):
        copia = otra_lista.copiar()
        actual = copia.primero
        while actual:
            self.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return self

    def __add__(self, otra_lista):
        resultado = self.copiar()
        resultado.concatenar(otra_lista)
        return resultado
