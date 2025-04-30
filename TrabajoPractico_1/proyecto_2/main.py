from modules.graficas import graficar_comparacion
from modules.prueba_tiempos import medir_tiempos
from modules.modulo_burbuja import metodo_burbuja
from modules.modulo_quicksort import quicksort
from modules.modulo_radixsort import radixsort
from modules.graficas import graficar_tiempos
from modules.ListadobleEnlazada import ListaDobleEnlazada
from modules.ListadobleEnlazada import Nodo
from modules.medir_tiempos_metodos import medir_tiempo_len
import random

tamanios = list(range(1,1001))
lista = [random.randint(10000, 99999) for _ in range(1000)]  # Generar una lista de 500 elementos aleatorios
lista2enlazada = ListaDobleEnlazada()
for i in lista:
    lista2enlazada.insertar(i)

#___________________________________COMPARACION DE ALGORITMOS_________________________________________

#tiempos_dict = {
#    "Burbuja": medir_tiempos(lista, metodo_burbuja),
#    "Quicksort": medir_tiempos(lista, quicksort),
#    "Radixsort": medir_tiempos(lista, radixsort),
#    "Sorted": medir_tiempos(lista, sorted)
#}

#Comparar_graficas = graficar_comparacion(tamanios, tiempos_dict)
#_____________________________________________________________________________________________________



#___________________________________GRAFICAS DE CADA ALGORITMO________________________________________

#tiempos_len = medir_tiempo_len(lista2enlazada)
tiempos_radixsort = medir_tiempos(lista, radixsort)
tiempos_quicksort = medir_tiempos(lista, quicksort)
tiempos_burbuja = medir_tiempos(lista, metodo_burbuja)
tiempos_sorted = medir_tiempos(lista, sorted)
graficar_tiempos(tamanios, tiempos_radixsort, "Radixsort")
graficar_tiempos(tamanios, tiempos_quicksort, "Quicksort")
graficar_tiempos(tamanios, tiempos_burbuja, "Burbuja")
graficar_tiempos(tamanios, tiempos_sorted, "Sorted")
# graficar_tiempos(tamanios, tiempos_len, "len")
# graficar_tiempos = graficar_tiempos(tamanios, tiempos_len, "len")
#_____________________________________________________________________________________________________

