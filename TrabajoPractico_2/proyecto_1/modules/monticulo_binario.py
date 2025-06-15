import math

class MonticuloBinario: 
    """
    Montículo Binario Mínimo en el que la clave más pequeña está siempre en el frente, 
    pues los niveles de gravedad van de 1 a 3.
    """
    def __init__(self):
        self.__lista_monticulo = [-math.inf]  # Elemento inicial ficticio para simplificar los cálculos de índices y no usar el inidce 0
        self.__tamano_actual = 0

    @property
    def tamano(self):
        """
        Tamaño actual del monticulo binario
        """ 
        return self.__tamano_actual #Que el atributo del tamño del monticulo no se pueda editar 

    @property
    def lista_monticulo(self):
        """
        Copia la lista del monticulo binario
        """
        return self.__lista_monticulo.copy()#Para que el monticulo binario se mantenga que haga una copia y asi no modificar el original

    
    #Metodos de modificacion mas que nada interna del monticulo binario, son herramientas para que se mantenga como un monticulo de minima como utilizaremos para la simulacion del triaje 
    def __infilt_arriba(self, i): 
        """
        Subir un elemento en el montículo para mantener la raiz del monitculo como el menor o mejor dicho monticulo minimo.
        """
        while i // 2 > 0:
            if self.__lista_monticulo[i] < self.__lista_monticulo[i // 2]:
                self.__lista_monticulo[i], self.__lista_monticulo[i // 2] = self.__lista_monticulo[i // 2], self.__lista_monticulo[i]
            i = i // 2

    def __infilt_abajo(self, i): 
        """
        Bajar un elemento en el montículo y mantener la raiz del monitculo como el menor o mejor dicho monticulo minimo.
        """
        while (i * 2) <= self.__tamano_actual:
            hm = self.__hijo_min(i)
            if self.__lista_monticulo[i] > self.__lista_monticulo[hm]:
                self.__lista_monticulo[i], self.__lista_monticulo[hm] = self.__lista_monticulo[hm], self.__lista_monticulo[i]
            i = hm
            
    def __hijo_min(self, i): 
        """
        Poder determinar el índice del hijo menor de un nodo.
        """
        if i * 2 + 1 > self.__tamano_actual:
            return i * 2
        else:
            if self.__lista_monticulo[i * 2] < self.__lista_monticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    
    def insertar(self, k): #K en este caso seria un paciente 
        """
        Agregar un elemento al montículo.
        Recibe un elemento cualquiera k.
        """ 
        self.__lista_monticulo.append(k)
        self.__tamano_actual += 1
        self.__infilt_arriba(self.__tamano_actual)

    def eliminar_min(self): #Para nuestro caso cuando se atienda una persona según el criterio de orden o gravedad del estado o orden de llegada se lo eliminara al primero que estara en la raiz
        """
        Eliminar del monticulo y devolver el valor mínimo del montículo osea la raíz.
        """
        if self.esta_vacio():
            raise IndexError("No se puede eliminar de un montículo que está vacio.")
        
        valor_eliminado = self.__lista_monticulo[1]
        self.__lista_monticulo[1] = self.__lista_monticulo[self.__tamano_actual]
        self.__tamano_actual -= 1
        self.__lista_monticulo.pop()
        self.__infilt_abajo(1)
        return valor_eliminado
    
    def buscar_min(self): #Este a diferencia de el eliminar minimo(raiz) solo lo va a informar 
        """
        Devolver el valor mínimo(la raiz) del montículo sin eliminarlo.
        """
        if self.esta_vacio():
            return None
        return self.__lista_monticulo[1]
        
    def esta_vacio(self): #Lo que dice el docstring
        """
        Devolver True si el montículo está vacio y False si no 
        """
        return self.__tamano_actual == 0

    def construir_monticulo(self, una_lista):  #Aqui le damos el formato de monticulo binario
        """
        Organizar una lista en forma de montículo binario
        """
        i = len(una_lista) // 2
        self.__tamano_actual = len(una_lista)
        self.__lista_monticulo = [-math.inf] + una_lista[:]  # Mantener el primer elemento ficticio
        while i > 0:
            self.__infilt_abajo(i)
            i -= 1
    
    