Sala de Emergencia simulación de Triaje 

Este proyecto es una simulación del proceso de triaje en una sala de emergencias. Se utiliza una cola de prioridad para gestionar la atención de pacientes según su nivel de riesgo (1: Crítico, 2: Moderado, 3: Bajo).

---
## 🏗Arquitectura General

El proyecto está divido en tres múdulos:
modulo_paciente.py: contiene la clase "Paciente", que genera pacientes con un ID único y un nivel de riesgo aleatorio.
modulo_prioridad.py: implementa una cola de prioridad genérica (ColaPrioridad) basada en heapq, que permite insertar elementos con una prioridad asociada.
Sala_de_emergencia.py: archivo principal que simula la llegada y atención de pacientes en la sala de emergencias.


---
## 📑Dependencias

**Python 3.x**
No se requieren librerías externas aparte de las estándar (`heapq`, `itertools`, `random`, `datetime`, `time`)

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. Ejecutar el archivo `Sala_de_emergencia.py` desde un entorno Python.

3. **Instalar las dependencias**:
   ```bash
   python Sala_de_emergencia.py
  
---
## 💻 Uso de la Aplicación

- Se generan 20 pacientes con niveles de riesgo aleatorios (1: Crítico, 2: Moderado, 3: Bajo).
- En cada ciclo de simulación:
  - Se inserta un nuevo paciente en la cola de espera.
  - Con 50% de probabilidad se atiende un paciente (se extrae el de mayor prioridad).
- Se imprime por consola:
  - Hora actual
  - Paciente atendido (si corresponde)
  - Lista de pacientes pendientes en la sala de espera

---

## 🙎‍♀️🙎‍♂️Autores

- Frederich, Rocío
- Merlo, Maria Fernanda
- Sivila, Matias

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
