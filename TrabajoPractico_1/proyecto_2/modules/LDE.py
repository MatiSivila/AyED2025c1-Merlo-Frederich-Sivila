class Nodo:  
    def __init__(self, dato, anterior=None, siguiente=None):
        self.dato = dato
        self.anterior = anterior
        self.siguiente = siguiente

class ListaDobleEnlazada:
    def __init__(self, iterable=None):
        self.__cabeza = None
        self.__cola = None
        self.__tamanio = 0
        if iterable:
            for item in iterable:
                self.agregar_al_final(item)

    @property
    def cabeza(self):
        return self.__cabeza
    
    @cabeza.setter
    def cabeza(self, nuevo_cabeza):
        self.__cabeza = nuevo_cabeza
        
    @property
    def cola(self):
        return self.__cola
    
    @cola.setter
    def cola(self, nuevo_cola):
        self.__cola = nuevo_cola

    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, nuevo_tamanio):
        self.__tamanio = nuevo_tamanio
    
    def esta_vacia(self):
        return self.__tamanio == 0

    def __len__(self):
        return self.__tamanio

    def agregar_al_inicio(self, item):
        nuevo = Nodo(item, None, self.cabeza)
        if self.__cabeza:
            self.__cabeza.anterior = nuevo
        else:
            self.__cola = nuevo
        self.__cabeza = nuevo
        self.__tamanio += 1

    def agregar_al_final(self, item):
        nuevo = Nodo(item, self.__cola, None)
        if self.__cola:
            self.__cola.siguiente = nuevo
        else:
            self.__cabeza = nuevo
        self.__cola = nuevo
        self.__tamanio += 1

    def insertar(self, item, posicion=None):
        if posicion is None or posicion >= self.__tamanio:
            self.agregar_al_final(item)
        elif posicion < 0:
            raise IndexError("Posición inválida")
        elif posicion == 0:
            self.agregar_al_inicio(item)
        else:
            actual = self.__cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            nuevo = Nodo(item, actual.anterior, actual)
            actual.anterior.siguiente = nuevo
            actual.anterior = nuevo
            self.__tamanio += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise IndexError("Lista vacía")
        if posicion is None:
            posicion = self.__tamanio - 1
        elif posicion < 0:
            posicion = self.__tamanio + posicion
        if posicion < 0 or posicion >= self.__tamanio:
            raise IndexError("Posición inválida")

        if posicion == 0:
            extraido = self.__cabeza.dato
            self.__cabeza = self.__cabeza.siguiente
            if self.__cabeza:
                self.__cabeza.anterior = None
            else:
                self.__cola = None
        elif posicion == self.__tamanio - 1:
            extraido = self.__cola.dato
            self.__cola = self.__cola.anterior
            if self.__cola:
                self.__cola.siguiente = None
            else:
                self.__cabeza = None
        else:
            actual = self.__cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            extraido = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
        self.__tamanio -= 1
        return extraido
    
    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.__cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia
    
    def invertir(self):
        actual = self.__cabeza
        self.__cabeza, self.__cola = self.__cola, self.__cabeza
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
        actual = self.__cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente


