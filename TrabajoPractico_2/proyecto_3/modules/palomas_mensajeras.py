import os

if __name__ == "__main__":
    from grafo import Grafo  # Asegurate de tener la clase Grafo en un archivo llamado grafo.py o modificalo según tu estructura
    from algoritmo_prim import prim    # Asegurate de tener implementado prim en un archivo prim.py o donde corresponda

    G = Grafo()

    # Ruta absoluta al archivo aldeas.txt, basada en la ubicación de este script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(script_dir, "aldeas.txt")

    # Carga del grafo
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            origen, destino, distancia = linea.strip().split(", ")
            G.agregarArista(origen, destino, int(distancia))

    # Ejecutar Prim
    origen = G.obtenerVertice("Peligros")  # Cambiá "Peligros" si querés otro vértice inicial
    prim(G, origen)

    # Mostrar resultados
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

