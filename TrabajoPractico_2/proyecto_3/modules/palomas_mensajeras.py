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

    
    origen = G.obtenerVertice("Peligros") 
    prim(G, origen)

  
    print("\n Lista de aldeas (orden alfabético):")
    aldeas_ordenadas = sorted([v.id for v in G])
    for nombre in aldeas_ordenadas:
        print(f"- {nombre}")

   
    print("\n Comunicación por aldea:\n")

   
    arbol = {}
    for v in G:
        pred = v.obtenerPredecesor()
        if pred:
            arbol.setdefault(pred.id, []).append(v.id)

    total = 0
    for v in sorted(G, key=lambda x: x.id):
        pred = v.obtenerPredecesor()
        if pred:
            print(f"{v.id} recibe el mensaje desde {pred.id}.")
            total += v.obtenerDistancia()
        elif v.obtenerDistancia() == 0:
            print(f"{v.id} inicia el envío del mensaje.")

        hijos = arbol.get(v.id, [])
        if hijos:
            print(f"Debe reenviar la noticia a: {', '.join(sorted(hijos))}\n")
        else:
            print("No reenvía el mensaje.\n")

 
    print(f" Distancia total recorrida por las palomas: {total} leguas\n")
