from grafo import Grafo
from algoritmo_prim import prim

def cargar_grafo_desde_archivo(nombre_archivo):
    G = Grafo()
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            origen, destino, distancia = linea.strip().split(", ")
            G.agregarArista(origen, destino, int(distancia))
    return G

def mostrar_resultados(G):
    print("\n--- Resultado del algoritmo de Prim ---\n")
    total = 0
    for v in sorted(G, key=lambda x: x.id):
        pred = v.obtenerPredecesor()
        if pred:
            print(f"{v.id} recibe de {pred.id}")
            print(f"Distancia: {v.obtenerDistancia()} leguas\n")
            total += v.obtenerDistancia()
        elif v.obtenerDistancia() == 0:
            print(f"{v.id} inicia el envío del mensaje.\n")
    print(f"Distancia total recorrida por las palomas: {total} leguas\n")

if __name__ == "__main__":
    G = cargar_grafo_desde_archivo("aldeas.txt")
    origen = G.obtenerVertice("Peligros")
    prim(G, origen)
    mostrar_resultados(G)
