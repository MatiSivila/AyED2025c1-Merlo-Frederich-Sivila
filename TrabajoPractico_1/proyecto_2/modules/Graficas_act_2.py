import time
import matplotlib.pyplot as plt
from LDE import ListaDobleEnlazada

def graficar_comparacion(tamanios, tiempos_dict):
    plt.figure(figsize=(12, 6))
    for nombre_algoritmo, tiempos in tiempos_dict.items():
        plt.plot(tamanios, tiempos, label=nombre_algoritmo, marker='o', markersize=3)
    plt.xlabel("Tamaño de la lista")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.title("Comparación de métodos: len, copiar, invertir")
    plt.legend()
    plt.grid(True)
    plt.show()

def graficar_tiempos(tamanios, tiempos, nombre_algoritmo):
    plt.figure(figsize=(10, 6))
    plt.plot(tamanios, tiempos, label=nombre_algoritmo, marker='o', markersize=3, linewidth=1.5)
    plt.title(f"Tiempo de ejecución de {nombre_algoritmo}")
    plt.xlabel("Tamaño de la lista")
    plt.ylabel("Tiempo (ms)")
    plt.grid(True)
    plt.legend()
    plt.show()


tamaños = list(range(0, 1001, 50))
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

for n in tamaños:
    lde = ListaDobleEnlazada(range(n))

    
    inicio = time.perf_counter()
    _ = len(lde)
    fin = time.perf_counter()
    tiempos_len.append((fin - inicio) * 1000)

   
    inicio = time.perf_counter()
    _ = lde.copiar()
    fin = time.perf_counter()
    tiempos_copiar.append((fin - inicio) * 1000)

    
    inicio = time.perf_counter()
    lde.invertir()
    fin = time.perf_counter()
    tiempos_invertir.append((fin - inicio) * 1000)

graficar_tiempos(tamaños, tiempos_len, "len()")
graficar_tiempos(tamaños, tiempos_copiar, "copiar()")
graficar_tiempos(tamaños, tiempos_invertir, "invertir()")
