from modules.NodoArbol import NodoArbol

class ABB:
    def __init__(self): #CREO UN ABB VACIO SIN RAIZ Y DE TAMAÑO 0
        self.raiz = None 
        self.tamano = 0
    
    def devolver_tamano(self):
        return self.tamano
    
    def __len__(self): #Este metodo funciona para que puedas definir lafuncion len(arbol) y que funcione correctamente
        """Devuelve el valor del tamaño actual del ABB"""
        return self.tamano 
   
    def __iter__(self):
        return self.raiz.__iter__() #Permite que el arbol pueda ser iterado por un for o por el operador "in" asi que es buena opción si se lo necesita en esos caso 
    
    def agregar(self, clave, valor):
        if self.raiz: #Pregunta si existe una raiz
            self._agregar(clave, valor, self.raiz) #En caso que si llama al metodo auxiliar para que determine en donde se agrege el nuevo nodo
        else: #Si no existe la raiz
            self.raiz = NodoArbol(clave, valor) #Determina un nodo arbol como una raiz
        self.tamano = self.tamano + 1 #Incrementa el valor del tamaño
    
    def eliminar(self,clave):
        if self.raiz:
            self.raiz = self._eliminar_recursivo(self.raiz,clave)
        else:
            raise KeyError(f"Clave {clave} no se encuentra en el ABB.")
            
    def __contains__(self, clave): #METODO PARA QUE PYTHON IDENTIFIQUE EL OPERADOR IN PARA EL ABB AY QUE POR DEFECTO NO LO HACE
        return self._buscar_recursivo(self.raiz, clave) is not None

    def _eliminar_recursivo(self, nodo, clave):
        if nodo is None: #ESTA LINEA ES IMPORTANTE PORQUE O INDICA QUE EL NODO A ELIMINAR NO EXISTE EN EL ARBOL O QUE EL ARBOL ESTA VACIO, PARA EN AMBOS CASOS TERMINAR
            if nodo is None:#SI EL NODO NO EXISTE
                raise KeyError(f"Clave {clave} no se encuentra en el ABB.") 

        if clave < nodo.clave: #SI LA CLAVE A ELIMINAR ES MENOR QUE LA CLAVE DEL NODO EN EL ARBOL
            nodo.hijoIzquierdo = self._eliminar_recursivo(nodo.hijoIzquierdo, clave) #APLICA EL METODO RECURSIVAMENTE PARA EL HIJO IZQUIERDO(PARA SEGUIR BAJANDO POR EL ARBOL)
        elif clave > nodo.clave:#SI LA CLAVE ES MAYOR 
            nodo.hijoDerecho = self._eliminar_recursivo(nodo.hijoDerecho, clave)#APLICA EL METODO RECURSIVAMENTE PARA EL HIJO DERECHO(PARA SEGUIR BAJANDO POR EL ARBOL)
        else:
            #SI EL NODO NO TIENE HIJOS(NODO HOJA) SOLO SE ELIMINA EL NODO Y SE RESTA 1 EL TAMAÑO
            if nodo.hijoIzquierdo is None and nodo.hijoDerecho is None:
                self.tamano -= 1
                return None

            #SI EL NODO TIENE UN SOLO HIJO SE ELIMINA EL NODO Y SE RESTA UNO EL TAMAÑO
            if nodo.hijoIzquierdo is None:
                self.tamano -= 1
                return nodo.hijoDerecho
            elif nodo.hijoDerecho is None:
                self.tamano -= 1
                return nodo.hijoIzquierdo

            # Caso 3: Nodo con dos hijos
            sucesor = self._minimo(nodo.hijoDerecho) #BUSCA EL NODO CON LA CLAVE MINIMA DEL SUBARBOL DERECHO DEL NODO, PARA REEMPLAZAR
            nodo.clave = sucesor.clave #LE ASIGNA LA CLAVE DEL SUCESOR 
            nodo.cargaUtil = sucesor.cargaUtil #LE ASIGNA LA CARGA UTIL
            nodo.hijoDerecho = self._eliminar_recursivo(nodo.hijoDerecho, sucesor.clave) #LO INCERTA COMO NUEVO NODO PADRE Y REACOMODA EL ARBOL
        return nodo

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

    def _agregar(self,clave,valor,nodoActual): #Metodo auxiliar nodo actual es el nodo que ya existe en el arbol 
        if clave < nodoActual.clave: #Si la clave actual es menor que la clave del nodo del arbol se dirige al subarbol izquierdo
            if nodoActual.tieneHijoIzquierdo(): #Si este subarbol ya posee un hijo izquierdo vuelve a llamar al metodo auxiliar para acomodarlo
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)#<-------
            else: # Si el subarbol no posee hijo izquierdo crea un nodo arbol en el hijo izquierdo
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual) #<-------------
        else: #Si la clave es mayor o igual lo dirige al subarbol derecho
            if nodoActual.tieneHijoDerecho(): #Si existe nodo derecho 
                self._agregar(clave, valor, nodoActual.hijoDerecho) #Llama al metodo auxiliar para reubicar el nuevo nodo
            else: #Si no posee hijo derecho
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual) #Crea un hijo derecho y pone el valor en esa ubicacion

        # Asignación con corchetes: abb[clave] = valor
    def __setitem__(self, clave, valor):
        self.agregar(clave, valor)

    # Acceso con corchetes: valor = abb[clave]
    def __getitem__(self, clave):
        nodo = self._buscar_recursivo(self.raiz, clave)
        if nodo is not None:
            return nodo.cargaUtil
        else:
            raise KeyError(f"Clave {clave} no encontrada en el árbol.")

    # Eliminación con corchetes: del abb[clave]
    def __delitem__(self, clave):
        self.eliminar(clave)

#ESTOS TRES ULTIMOS METODOS SON PARA QUE PYTHON PERMITA OPERAR CON CORCHETES COMO SI FUERA UNA LISTA EL ABB
