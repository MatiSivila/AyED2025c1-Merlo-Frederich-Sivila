from datetime import datetime
from modules.Arbol_AVL import AVL

class Temperaturas_DB:
    def __init__(self):
        self.__arbol_avl = AVL()
    
    def guardar_temperatura(self, temperatura , fecha):
        fecha_datetime = datetime.strptime(fecha, "%d/%m/%Y")
        self.__arbol_avl.agregar(fecha_datetime,temperatura)

    def devolver_temperatura(self,fecha):
        fecha_datetime = datetime.strptime(fecha, "%d/%m/%Y")
        nodo = self.__arbol_avl.buscar(fecha_datetime)
        if nodo:
            return nodo.cargaUtil
        else:
            return None
    
    def max_temp_entre_fechas(self, fecha1, fecha2):
        fecha1_datetime = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_datetime = datetime.strptime(fecha2, "%d/%m/%Y")
        if fecha1_datetime > fecha2_datetime:
            raise ValueError ("La fecha 1 debe ser menor que la fecha 2")
        temperatura_maxima = self.__temperaturas_rango(fecha1_datetime,fecha2_datetime)
        if temperatura_maxima:
            return max(temperatura_maxima)
        
    def __temperaturas_rango(self,fecha1,fecha2):
        nodos = self.rango_nodos(fecha1,fecha2)
        return [nodo.cargaUtil for nodo in nodos]

    def min_temp_entre_fechas(self, fecha1, fecha2):
        fecha1_datetime = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_datetime = datetime.strptime(fecha2, "%d/%m/%Y")
        if fecha1_datetime > fecha2_datetime:
            raise ValueError ("La fecha 1 debe ser menor que la fecha 2")
        temperatura_minima = self.__temperaturas_rango(fecha1_datetime,fecha2_datetime)
        if temperatura_minima:
            return min(temperatura_minima)

    def temp_extremos_rango(self, fecha1, fecha2):
        fecha1_datetime = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_datetime = datetime.strptime(fecha2, "%d/%m/%Y")
        if fecha1_datetime > fecha2_datetime:
            raise ValueError ("La fecha 1 debe ser menor que la fecha 2")
        temperaturas = self.__temperaturas_rango(fecha1_datetime,fecha2_datetime)
        if temperaturas:
            return min(temperaturas),max(temperaturas)
    


    def devolver_temperaturas(self,fecha1,fecha2):
        fecha1_datetime = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_datetime = datetime.strptime(fecha2, "%d/%m/%Y")
        if fecha1_datetime in self.__arbol_avl and fecha2_datetime in self.__arbol_avl:
            nodos = self.rango_nodos(fecha1_datetime,fecha2_datetime)
            return [f"{nodo.clave.strftime('%d/%m/%Y')}: {nodo.cargaUtil}°C" for nodo in nodos]
        else:
            raise KeyError("No se encuentran registros de esas fechas")
            
    def cantidad_muestras(self):
        return self.__arbol_avl.tamano
    
    def rango_nodos(self,fecha1,fecha2):
        nodos = []
        self.__recorrer_rango(self.__arbol_avl.raiz,fecha1,fecha2,nodos)
        return nodos
                  
    def __recorrer_rango(self,nodo,fecha1,fecha2,nodos):
        if nodo is None:
            return None
        if fecha1 <= nodo.clave <= fecha2:
            self.__recorrer_rango(nodo.hijoIzquierdo,fecha1,fecha2,nodos)
            nodos.append(nodo)
            self.__recorrer_rango(nodo.hijoDerecho,fecha1,fecha2,nodos)
        elif nodo.clave < fecha1:
            self.__recorrer_rango(nodo.hijoDerecho,fecha1,fecha2,nodos)
        else:
            self.__recorrer_rango(nodo.hijoIzquierdo,fecha1,fecha2,nodos)
        
    def borrar_temperatura(self,fecha):
        fecha_datetime = datetime.strptime(fecha,"%d/%m/%Y")
        self.__arbol_avl.eliminar(fecha_datetime)
        
    