class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.clave = clave #Le asigno una clave de referencia
        self.cargaUtil = valor #Le proporciono la carga util(datos del nodo)
        self.hijoIzquierdo = izquierdo #Determino un hijo izquierdo
        self.hijoDerecho = derecho #Determino un hijo derecho
        self.padre = padre	# opcional, pero útil si está presente <-- Nose a que se refiere
        self.altura = 0

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo is not None

    def tieneHijoDerecho(self):
        return self.hijoDerecho is not None

    def esHoja(self):
        return self.hijoIzquierdo is None and self.hijoDerecho is None

    def __iter__(self):
        if self.tieneHijoIzquierdo():
            yield from self.hijoIzquierdo
        yield (self.clave, self.cargaUtil)  # clave y valor como tupla
        if self.tieneHijoDerecho():
            yield from self.hijoDerecho         