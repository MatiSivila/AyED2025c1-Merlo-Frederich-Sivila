import time
import datetime
import random
from modulo_paciente import Paciente
from modulo_prioridad import ColaPrioridad



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

