from modules.graficas import graficar_comparacion
from modules.prueba_tiempos import medir_tiempos
from modules.modulo_burbuja import metodo_burbuja
from modules.modulo_quicksort import quicksort
from modules.modulo_radixsort import radixsort
from modules.graficas import graficar_tiempos
import random

tamanios = list(range(1,501))
lista = [random.randint(10000, 99999) for _ in range(500)]  # Generar una lista de 500 elementos aleatorios


#___________________________________COMPARACION DE ALGORITMOS_________________________________________

#tiempos_dict = {
#    "Burbuja": medir_tiempos(lista, metodo_burbuja),
#    "Quicksort": medir_tiempos(lista, quicksort),
#    "Radixsort": medir_tiempos(lista, radixsort),
#}

#Comparar_graficas = graficar_comparacion(tamanios, tiempos_dict)
#_____________________________________________________________________________________________________



#___________________________________GRAFICAS DE CADA ALGORITMO________________________________________

tiempos_radixsort = medir_tiempos(lista, radixsort)
tiempos_quicksort = medir_tiempos(lista, quicksort)
tiempos_burbuja = medir_tiempos(lista, metodo_burbuja)

#graficar_tiempos(tamanios, tiempos_radixsort, "Radixsort")
#graficar_tiempos(tamanios, tiempos_quicksort, "Quicksort")
graficar_tiempos(tamanios, tiempos_burbuja, "Burbuja")

#_____________________________________________________________________________________________________


