Palomas mensajeras

Este proyecto simula un sistema de comunicación antiguo basado en palomas mensajeras, optimizando el envío de mensajes desde la aldea de origen Peligros hacia otras 21 aldeas. Se utiliza el algoritmo de Prim para construir un árbol de expansión mínima que garantice la entrega más eficiente del mensaje.
Se obtiene como resultado: 
1. La lista de aldeas en orden alfabético.
2. La mejor manera de replicar mensajes entre aldeas usando el menor esfuerzo (suma de distancias).
3. Qué aldea debe enviar o recibir mensajes de otras, de forma eficiente.

---
## 🏗Arquitectura General
vertice.py: Representación de una Aldea como un vértice del grafo.
grafo.py: Definición de la clase Grafo, que representa el conjunto de aldeas y caminos.
cola_prioridad.py: Implementación de una cola de prioridad mínima para facilitar el algoritmo de Prim.
algoritmo_prim.py: Implementación del algoritmo de Prim para obtener el árbol de expansión mínima.
palomas_mensajeras.py: Script principal que coordina la ejecución del programa.

---
## 📑Dependencias

1. Python 3.8+
2. No se utilizan librerías externas: todo está implementado con módulos estándar de Python.

---
## 🚀Cómo Ejecutar el Proyecto
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. Ejecutar el archivo `palomas_mensajeras.py` desde un entorno Python.

3. Asegurarse de tener el archivo aldeas.txt en el mismo directorio que el script.

4. **Instalar las dependencias**:
   ```bash
   python palomas_mensajeras.py

---

## 💻Uso de la aplicación

Se cargan las aldeas y distancias desde el archivo aldeas.txt, se aplica el algoritmo de Prim para encontrar el recorrido más eficiente desde la aldea "Peligros".
Se imprime por consola:
- Aldeas ordenadas alfabéticamente.
- Para cada aldea, desde qué vecina recibe el mensaje.
- A qué vecinas debe enviar la noticia.
- Distancia total recorrida por todas las palomas.

---

## 🙎‍♀️🙎‍♂️Autores

- Frederich, Rocío
- Merlo, Maria Fernanda
- Sivila, Matias
---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
