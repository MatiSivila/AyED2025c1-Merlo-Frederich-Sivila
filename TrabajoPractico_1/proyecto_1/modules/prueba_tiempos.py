import time

def medir_tiempos(lista,metodo_ord):
    tiempos = []
    for i in range(len(lista)):
        copia_lista = lista[:i+1]  # Tomar una sublista creciente
        inicio = time.perf_counter()
        metodo_ord(copia_lista)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return tiempos