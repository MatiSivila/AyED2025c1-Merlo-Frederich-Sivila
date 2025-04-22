import matplotlib.pyplot as plt

def graficar_comparacion(tamanios, tiempos_dict):
    plt.figure(figsize=(12, 6))

    for nombre_algoritmo, tiempos in tiempos_dict.items():
        plt.plot(tamanios, tiempos, label=nombre_algoritmo)

    plt.xlabel("Tamaño de la lista")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.title("Comparación de algoritmos de ordenamiento")
    plt.legend()
    plt.grid(True)
    plt.show()


import matplotlib.pyplot as plt

def graficar_tiempos(tamanios, tiempos, nombre_algoritmo):
    plt.figure(figsize=(10, 6))
    plt.plot(tamanios, tiempos, label=nombre_algoritmo, marker='o', markersize=2, linewidth=1.5)
    plt.title(f"Tiempo de ejecución de {nombre_algoritmo}")
    plt.xlabel("Tamaño de la lista")
    plt.ylabel("Tiempo (ms)")
    plt.grid(True)
    plt.legend()
    plt.show()