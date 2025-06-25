import os
from modules.grafo import Grafo

if __name__ == "__main__":
    G = Grafo()

    # Obtener ruta de aldeas.txt
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(script_dir, 'data', 'aldeas.txt')

    with open(ruta_archivo, 'r', encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(", ")
            if len(partes) != 3:
                continue
            origen, destino, distancia = partes
            G.agregar_arista(origen, destino, int(distancia))

    mst = G.prim("Peligros")

    # Mostrar resultado
    print("\nLista de aldeas involucradas (orden alfabético):")
    aldeas = set()
    for o, d, _ in mst:
        aldeas.add(o)
        aldeas.add(d)
    for nombre in sorted(aldeas):
        print(f"- {nombre}")

    print("\nComunicación por aldea:\n")
    arbol = []
    for origen, destino, _ in mst:
        arbol.append((origen, destino))

    total = 0
    for origen, destino, peso in mst:
        print(f"{destino} recibe el mensaje desde {origen}.")
        total += peso
        hijos = [d for o, d in arbol if o == destino]
        if hijos:
            print(f"Debe reenviar la noticia a: {', '.join(sorted(hijos))}\n")
        else:
            print("No reenvía el mensaje.\n")

    print(f"Distancia total recorrida por las palomas: {total} leguas\n")