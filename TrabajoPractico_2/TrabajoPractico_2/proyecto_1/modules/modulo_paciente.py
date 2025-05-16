# Clase Paciente
import random

class Paciente:
    _id = 1  

    def __init__(self):
        self.id = Paciente._id
        Paciente._id += 1
        self.criticidad = random.randint(1, 3) 

    def __str__(self):
        niveles = {1: "Crítico", 2: "Moderado", 3: "Bajo"}
        return f"Paciente #{self.id} - Riesgo: {niveles[self.criticidad]}"