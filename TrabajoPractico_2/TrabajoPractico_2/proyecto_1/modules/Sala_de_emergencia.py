import time
import datetime
import random
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


# Clase Paciente

class Paciente:
    _id = 1  

    def __init__(self):
        self.id = Paciente._id
        Paciente._id += 1
        self.criticidad = random.randint(1, 3) 

    def __str__(self):
        niveles = {1: "Crítico", 2: "Moderado", 3: "Bajo"}
        return f"Paciente #{self.id} - Riesgo: {niveles[self.criticidad]}"


# Simulación de sala de emergencias

n = 20 
cola_de_espera = ColaPrioridad()

for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    paciente = Paciente()
    cola_de_espera.insertar(paciente.criticidad, paciente)

    # Atención de paciente en 50% de los ciclos
    if random.random() < 0.5 and len(cola_de_espera) > 0:
        paciente_atendido = cola_de_espera.extraer()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)

    print()
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for paciente in cola_de_espera:
        print('\t', paciente)

    print()
    print('-*-'*15)
    time.sleep(1)

