import time 
import random
def metodo_burbuja(lista):
    for num_pasadas in range(len(lista)-1):
        for j in range(num_pasadas):
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
    return lista

