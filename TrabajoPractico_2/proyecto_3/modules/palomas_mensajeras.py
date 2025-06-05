import os

if __name__ == "__main__":
    from grafo import Grafo  
    from algoritmo_prim import prim
    G = Grafo()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(script_dir, "aldeas.txt")

   
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(", ")
            if len(partes) != 3:
                continue 
            origen, destino, distancia = partes
            G.agregarArista(origen, destino, int(distancia))


    # Ejecutar Prim
    origen = G.obtenerVertice("Peligros") 
    prim(G, origen)

    # Mostrar resultados
    print("\n Resultados obtenidos: \n")
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

