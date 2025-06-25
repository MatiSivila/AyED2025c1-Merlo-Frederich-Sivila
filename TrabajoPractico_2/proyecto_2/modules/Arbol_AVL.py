from NodoArbol import NodoArbol

class AVL:
    def __init__(self): #CREO UN ABB VACIO SIN RAIZ Y DE TAMAÑO 0
        self.__raiz = None 
        self.__tamano = 0
    
    def devolver_tamano(self):
        return self.__tamano

    @property
    def raiz(self):
        return self.__raiz
    
    @property
    def tamano(self):
        return self.__tamano

    def altura(self,nodo):
        return nodo.altura if nodo else 0
    
    def actualizar_altura(self,nodo):
        nodo.altura = 1 + max(self.altura(nodo.hijoIzquierdo),self.altura(nodo.hijoDerecho))

    def factor_balance(self, nodo):
        return self.altura(nodo.hijoIzquierdo) - self.altura(nodo.hijoDerecho)

    def _rotar_derecha(self, nodoDesbalanceado):
        hijoIzquierdo = nodoDesbalanceado.hijoIzquierdo
        subarbolDerechoDelHijo = hijoIzquierdo.hijoDerecho

        # Rotar
        hijoIzquierdo.hijoDerecho = nodoDesbalanceado
        nodoDesbalanceado.hijoIzquierdo = subarbolDerechoDelHijo

        # Actualizar alturas
        nodoDesbalanceado.altura = 1 + max(self.altura(nodoDesbalanceado.hijoIzquierdo), self.altura(nodoDesbalanceado.hijoDerecho))
        hijoIzquierdo.altura = 1 + max(self.altura(hijoIzquierdo.hijoIzquierdo), self.altura(hijoIzquierdo.hijoDerecho))

        return hijoIzquierdo


    def _rotar_izquierda(self, nodoDesbalanceado):
        hijoDerecho = nodoDesbalanceado.hijoDerecho
        subarbolIzquierdoDelHijo = hijoDerecho.hijoIzquierdo

        # Rotar
        hijoDerecho.hijoIzquierdo = nodoDesbalanceado
        nodoDesbalanceado.hijoDerecho = subarbolIzquierdoDelHijo

        # Actualizar alturas
        nodoDesbalanceado.altura = 1 + max(self.altura(nodoDesbalanceado.hijoIzquierdo), self.altura(nodoDesbalanceado.hijoDerecho))
        hijoDerecho.altura = 1 + max(self.altura(hijoDerecho.hijoIzquierdo), self.altura(hijoDerecho.hijoDerecho))

        return hijoDerecho
    
    def __len__(self): #Este metodo funciona para que puedas definir lafuncion len(arbol) y que funcione correctamente
        """Devuelve el valor del tamaño actual del ABB"""
        return self.__tamano 
   
    def __iter__(self):
        return self.__raiz.__iter__() #Permite que el arbol pueda ser iterado por un for o por el operador "in" asi que es buena opción si se lo necesita en esos caso 
    
    def agregar(self, clave, valor):
        if self.__raiz:#Pregunta si existe una raiz
            self.__raiz = self._agregar(clave, valor, self.__raiz)#En caso que si llama al metodo auxiliar para que determine en donde se agrege el nuevo nodo
        else: #Si no existe la raiz
            self.__raiz = NodoArbol(clave, valor)#Determina un nodo arbol como una raiz
        self.__tamano += 1 #Aumenta el tamaño


    def eliminar(self,clave):
         nodo_eliminado = self._eliminar_recursivo(clave,self.__raiz)
         if nodo_eliminado is not None:
            self.__tamano -=1
            
    def __contains__(self, clave): #METODO PARA QUE PYTHON IDENTIFIQUE EL OPERADOR IN PARA EL ABB AY QUE POR DEFECTO NO LO HACE
        return self._buscar_recursivo(self.__raiz, clave) is not None

    def _eliminar_recursivo(self,clave,nodo):
        if nodo is None:
            return nodo      
        if clave < nodo.clave:
            nodo.hijoIzquierdo = self._eliminar_recursivo(clave,nodo.hijoIzquierdo)
        elif clave > nodo.clave:
            nodo.hijoDerecho = self._eliminar_recursivo(clave,nodo.hijoDerecho)
        else:
            if nodo.tieneAmbosHijos():
                sucesor = self._minimo(nodo.hijoDerecho) #BUSCA EL NODO CON LA CLAVE MINIMA DEL SUBARBOL DERECHO DEL NODO, PARA REEMPLAZAR
                nodo.clave =sucesor.clave
                nodo.cargaUtil = sucesor.cargaUtil
                #nodo.clave,nodo.cargaUtil = sucesor.clave,sucesor.cargaUtil #LE ASIGNA LA CLAVE DEL SUCESOR Y LE ASIGNA LA CARGA UTIL
                nodo.hijoDerecho = self._eliminar_recursivo(sucesor.clave,nodo.hijoDerecho) #LO INCERTA COMO NUEVO NODO PADRE Y REACOMODA EL ARBOL  
            else:
                nodo = nodo.hijoIzquierdo if nodo.tieneHijoIzquierdo() else nodo.hijoDerecho
        if nodo is None:
            return nodo  
        self.equilibrar_post_eliminacion(nodo)
        return nodo

    def equilibrar_post_eliminacion(self,nodo):
        if nodo.factor_equilibrio > 1 or nodo.factor_equilibrio < -1:
            self.__reequilibrar(nodo)
            return
        if nodo.padre is not None:
            if nodo.esHijoIzquierdo():
                nodo.padre.factor_equilibrio -= 1
            elif nodo.esHijoDerecho():
                nodo.padre.factor_equilibrio +=1
            if nodo.padre.factor_equilibrio !=0:
                self.equilibrar_post_eliminacion(nodo.padre)

    def __reequilibrar(self,nodo):
        if nodo.factor_equilibrio < 0:
            if nodo.hijoDerecho.factor_equilibrio > 0:
                self._rotar_derecha(nodo.hijoDerecha)
            self._rotar_izquierda(nodo)
        elif nodo.factor_equilibrio > 0:
            if nodo.hijoIzquierdo.factor_equilibrio < 0:
                self._rotar_izquierda(nodo.hijoIzquierda)
            self._rotar_derecha(nodo)

    def _minimo(self, nodo):
        while nodo.hijoIzquierdo is not None:
            nodo = nodo.hijoIzquierdo
        return nodo
    
    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, nodo, clave):
        if nodo is None:
            return None  #NO EXISTE LA CLAVE EN EL ARBOL
        if clave < nodo.clave:
            return self._buscar_recursivo(nodo.hijoIzquierdo, clave)#APLICA RECURSIVAMENTE PARA EL HIJO IZQUIERDO 
        elif clave > nodo.clave:
            return self._buscar_recursivo(nodo.hijoDerecho, clave)#APLICAR RECURSIVAMENTE PARA EL HIJO DERECHO
        else:
            return nodo  #DEVUELVE EL NODO QUE SE ENCONTRO 

    def obtener(self, clave):
        nodo = self._buscar_recursivo(self.raiz, clave)
        if nodo is not None:
            return nodo.cargaUtil
        else:
            raise KeyError(f"La clave {clave} no se encuentra en el ABB")

    def _agregar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                nodoActual.hijoIzquierdo = self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                nodoActual.hijoDerecho = self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)

        self.actualizar_altura(nodoActual)

        fe = self.factor_balance(nodoActual)

        # Rotaciones
        # Izquierda-Izquierda
        if fe > 1 and clave < nodoActual.hijoIzquierdo.clave:
            return self._rotar_derecha(nodoActual)

        # Derecha-Derecha
        if fe < -1 and clave > nodoActual.hijoDerecho.clave:
            return self._rotar_izquierda(nodoActual)

        # Izquierda-Derecha
        if fe > 1 and clave > nodoActual.hijoIzquierdo.clave:
            nodoActual.hijoIzquierdo = self._rotar_izquierda(nodoActual.hijoIzquierdo)
            return self._rotar_derecha(nodoActual)

        # Derecha-Izquierda
        if fe < -1 and clave < nodoActual.hijoDerecho.clave:
            nodoActual.hijoDerecho = self._rotar_derecha(nodoActual.hijoDerecho)
            return self._rotar_izquierda(nodoActual)

        return nodoActual

        # Asignación con corchetes: ABB[clave] = valor

    def __setitem__(self, clave, valor):
        self.agregar(clave, valor)

    # Acceso con corchetes: valor = ABB[clave]
    def __getitem__(self, clave):
        nodo = self._buscar_recursivo(self.__raiz, clave)
        if nodo is not None:
            return nodo.cargaUtil
        else:
            raise KeyError(f"Clave {clave} no encontrada en el árbol.")

    # Eliminación con corchetes: del ABB[clave]
    def __delitem__(self, clave):
        self.eliminar(clave)

#ESTOS TRES ULTIMOS METODOS SON PARA QUE PYTHON PERMITA OPERAR CON CORCHETES COMO SI FUERA UNA LISTA EL ABB
