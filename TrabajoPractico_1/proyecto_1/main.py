from modules.graficar import graficar_tiempos
from modules.prueba_tiempos import medir_tiempos
from modules.modulo_burbuja import metodo_burbuja
import random

tamanios = list(range(500))
lista = [random.randint(10000, 99999) for _ in range(500)]  # Generar una lista de 500 elementos aleatorios
ordenamiento_burbuja = metodo_burbuja(lista)  # Ordenar la lista usando el método de burbuja
tiempos_burbuja = medir_tiempos(lista, metodo_burbuja)  # Medir los tiempos de ordenamiento
graficar_tiempos_burbuja = graficar_tiempos(tamanios, tiempos_burbuja)  # Graficar los tiempos de ordenamiento