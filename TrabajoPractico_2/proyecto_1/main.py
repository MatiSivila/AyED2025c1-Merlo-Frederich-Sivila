"""
Sala de emergencias
"""

import time
import datetime
import modules.modulo_paciente as pac
from modules.cola_prioridad import ColaPrioridad as cola
import random

n = 20  # cantidad de ciclos de simulación
contador = 0
cola_de_espera = cola()

# Ciclo que gestiona la simulación
while contador < n or not cola_de_espera.esta_vacia(): 
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    if contador < n:
        # Se crea un paciente un paciente por segundo
        # La criticidad del paciente es aleatoria
        paciente = pac.Paciente(contador)
        cola_de_espera.insertar(paciente)
        contador +=1

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = cola_de_espera.atender()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', cola_de_espera.tamano())
    lista_espera = cola_de_espera.lista_actual()
    for paciente in lista_espera:
        print('\t',paciente)
    

    print()
    print('-*-'*15)
    
    time.sleep(1)