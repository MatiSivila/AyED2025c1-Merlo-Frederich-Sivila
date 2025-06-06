from modules.cola_prioridad import ColaPrioridad

def prim(G, inicio):
    cp = ColaPrioridad()
    for v in G:
        v.asignarDistancia(float('inf'))
        v.asignarPredecesor(None)
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(), v) for v in G])

    while not cp.estaVacia():
        actual = cp.eliminarMin()
        for vecino in actual.obtenerConexiones():
            costo = actual.obtenerPonderacion(vecino)
            if vecino in cp and costo < vecino.obtenerDistancia():
                vecino.asignarPredecesor(actual)
                vecino.asignarDistancia(costo)
                cp.decrementarClave(vecino, costo)
