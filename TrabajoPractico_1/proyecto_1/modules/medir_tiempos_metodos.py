import time

def medir_tiempo_len(lista):
    tiempos = []
    for _ in range(1,1001):  # Realizar la medición 10 veces
        inicio = time.time()
        _ = len(lista)
        fin = time.time()
        tiempos.append(fin - inicio)
    return tiempos