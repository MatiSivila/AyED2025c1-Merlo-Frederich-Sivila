class Nodo:  
    def __init__(self, dato, anterior=None, siguiente=None):
        self.dato = dato
        self.anterior = anterior
        self.siguiente = siguiente

class ListaDobleEnlazada:
    def __init__(self, iterable=None):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
        if iterable:
            for item in iterable:
                self.agregar_al_final(item)

    def esta_vacia(self):
        return self.tamanio == 0

    def __len__(self):
        return self.tamanio

    def agregar_al_inicio(self, item):
        nuevo = Nodo(item, None, self.cabeza)
        if self.cabeza:
            self.cabeza.anterior = nuevo
        else:
            self.cola = nuevo
        self.cabeza = nuevo
        self.tamanio += 1

    def agregar_al_final(self, item):
        nuevo = Nodo(item, self.cola, None)
        if self.cola:
            self.cola.siguiente = nuevo
        else:
            self.cabeza = nuevo
        self.cola = nuevo
        self.tamanio += 1

    def insertar(self, item, posicion=None):
        if posicion is None or posicion >= self.tamanio:
            self.agregar_al_final(item)
        elif posicion < 0:
            raise IndexError("Posición inválida")
        elif posicion == 0:
            self.agregar_al_inicio(item)
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            nuevo = Nodo(item, actual.anterior, actual)
            actual.anterior.siguiente = nuevo
            actual.anterior = nuevo
            self.tamanio += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise IndexError("Lista vacía")
        if posicion is None:
            posicion = self.tamanio - 1
        elif posicion < 0:
            posicion = self.tamanio + posicion
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición inválida")

        if posicion == 0:
            extraido = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        elif posicion == self.tamanio - 1:
            extraido = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            extraido = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
        self.tamanio -= 1
        return extraido

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self):
        actual = self.cabeza
        self.cabeza, self.cola = self.cola, self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior

    def concatenar(self, otra_lista):
        copia = otra_lista.copiar()
        actual = copia.cabeza
        while actual:
            self.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return self

    def __add__(self, otra_lista):
        resultado = self.copiar()
        resultado.concatenar(otra_lista)
        return resultado
    
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente
    


