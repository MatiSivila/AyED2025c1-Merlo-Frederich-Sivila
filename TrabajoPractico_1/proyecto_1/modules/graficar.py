import matplotlib.pyplot as plt

def graficar_tiempos(datos, tiempos):
    """
    Grafica los tiempos de ordenamiento en función de los datos.

    :param datos: Lista de 500 elementos representando los datos.
    :param tiempos: Lista de 500 elementos representando los tiempos de ordenamiento.
    """
    if len(datos) != 500 or len(tiempos) != 500:
        raise ValueError("Ambas listas deben contener exactamente 500 elementos.")
    
    plt.figure(figsize=(10, 6))
    plt.plot(datos, tiempos, marker='o', linestyle='-', color='b', label='Tiempo de ordenamiento')
    plt.title('Tiempos de Ordenamiento por Datos')
    plt.xlabel('Datos')
    plt.ylabel('Tiempo (ms)')
    plt.legend()
    plt.grid(True)
    plt.show()