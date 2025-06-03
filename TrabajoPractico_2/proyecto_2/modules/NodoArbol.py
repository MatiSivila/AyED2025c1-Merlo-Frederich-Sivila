class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.__clave = clave #Le asigno una clave de referencia
        self.__cargaUtil = valor #Le proporciono la carga util(datos del nodo)
        self.__hijoIzquierdo = izquierdo #Determino un hijo izquierdo
        self.__hijoDerecho = derecho #Determino un hijo derecho
        self.__padre = padre	# opcional, pero útil si está presente <-- Nose a que se refiere
        self.__altura = 1

    @property
    def clave(self):
        return self.__clave
    
    @property
    def cargaUtil(self):
        return self.__cargaUtil
    
    @property
    def hijoIzquierdo(self):
        return self.__hijoIzquierdo
    
    @property
    def hijoDerecho(self):
        return self.__hijoDerecho
    
    @property
    def padre(self):
        return self.__padre
    
    @property
    def altura(self):
        return self.__altura
    
    @hijoDerecho.setter
    def hijoDerecho(self,valor):
        self.__hijoDerecho = valor

    @hijoIzquierdo.setter
    def hijoIzquierdo(self,valor):
        self.__hijoIzquierdo = valor

    @padre.setter
    def padre(self,valor):
        self.__padre = valor

    @altura.setter
    def altura(self,valor):
        self.__altura = valor   

    def tieneHijoIzquierdo(self):
        return self.__hijoIzquierdo is not None

    def tieneHijoDerecho(self):
        return self.__hijoDerecho is not None

    def esHoja(self):
        return self.__hijoIzquierdo is None and self.hijoDerecho is None

    def __iter__(self):
        if self.tieneHijoIzquierdo():
            yield from self.__hijoIzquierdo
        yield (self.clave, self.cargaUtil)  # clave y valor como tupla
        if self.tieneHijoDerecho():
            yield from self.__hijoDerecho         