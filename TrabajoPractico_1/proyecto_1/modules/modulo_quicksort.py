import numpy as np
import random as rd
import time

def quicksort(lista):   
    if len(lista) <= 1:
        return lista
    lista_tiempos = []
    valor_mediana = int(np.median(lista))
    pivote = min(lista, key=lambda x: abs(x - valor_mediana))
    indice_original = lista.index(pivote)
    lista[indice_original], lista[0] = lista[0], lista[indice_original]
    
    punt_izq = 1 
    punt_der = len(lista) - 1
    complete = False

    while not complete:
        inicio = time.perf_counter()
        while punt_izq <= punt_der and lista[punt_izq] < pivote:
            punt_izq += 1

        while punt_izq <= punt_der and lista[punt_der] > pivote:
            punt_der -= 1

        if punt_izq > punt_der:
            lista[0], lista[punt_der] = lista[punt_der], lista[0]
            final = time.perf_counter()
            duracion = final - inicio
            lista_tiempos.append(duracion)
            complete = True
        else:
            lista[punt_izq], lista[punt_der] = lista[punt_der], lista[punt_izq]
            punt_izq += 1
            punt_der -= 1
        final = time.perf_counter()
        duracion = final - inicio
        lista_tiempos.append(duracion)
    
    lista_menores = quicksort(lista[:punt_der])
    lista_mayores = quicksort(lista[punt_der + 1:])
    
    return lista_menores + [pivote] + lista_mayores 

