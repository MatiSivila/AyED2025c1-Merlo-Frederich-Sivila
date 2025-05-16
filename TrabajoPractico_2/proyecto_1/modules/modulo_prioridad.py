import datetime
import heapq
import itertools

# Cola de prioridad genérica

class ColaPrioridad:
    def __init__(self):
        self._heap = []
        self._contador = itertools.count()

    def insertar(self, prioridad, elemento):
        count = next(self._contador)
        heapq.heappush(self._heap, (prioridad, count, elemento))

    def extraer(self):
        if self._heap:
            return heapq.heappop(self._heap)[-1]
        raise IndexError("extraer desde cola vacía")

    def esta_vacia(self):
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)

    def __iter__(self):
        return (item[-1] for item in sorted(self._heap))