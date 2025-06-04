from modules.Temperaturas_DB import Temperaturas_DB

db = Temperaturas_DB()

# Cargar 20 temperaturas con fechas (formato dd/mm/aaaa)
datos = [
    ("01/01/2023", 25.5),
    ("02/01/2023", 24.8),
    ("03/01/2023", 26.1),
    ("04/01/2023", 27.3),
    ("05/01/2023", 22.4),
    ("06/01/2023", 23.9),
    ("07/01/2023", 21.0),
    ("08/01/2023", 28.6),
    ("09/01/2023", 29.1),
    ("10/01/2023", 30.0),
    ("11/01/2023", 31.2),
    ("12/01/2023", 28.0),
    ("13/01/2023", 26.7),
    ("14/01/2023", 25.0),
    ("15/01/2023", 24.3),
    ("16/01/2023", 22.0),
    ("17/01/2023", 20.5),
    ("18/01/2023", 19.8),
    ("19/01/2023", 18.9),
    ("20/01/2023", 17.6)
]

for fecha, temp in datos:
    db.guardar_temperatura(temp, fecha)

# Probar métodos
print("Cantidad total de muestras:", db.cantidad_muestras())

print("\nTemperatura del 08/01/2023:", db.devolver_temperatura("08/01/2023"), "ºC")

print("\nTemperaturas entre 05/01/2023 y 15/01/2023:")
for entrada in db.devolver_temperaturas("05/01/2023", "15/01/2023"):
    print(entrada)

print("\nTemperatura máxima entre 01/01/2023 y 10/01/2023:",
      db.max_temp_entre_fechas("01/01/2023", "10/01/2023"), "ºC")

print("Temperatura mínima entre 01/01/2023 y 10/01/2023:",
      db.min_temp_entre_fechas("01/01/2023", "10/01/2023"), "ºC")

print("Temperaturas extrema entre 01/01/2023 y 20/01/2023:",
      db.temp_extremos_rango("01/01/2023", "20/01/2023"))

# Borrar una muestra
db.borrar_temperatura("10/01/2023")
print("Después de borrar la muestra del 10/01/2023:")
print("Temperatura del 10/01/2023:", db.devolver_temperatura("10/01/2023"))

print("Cantidad total de muestras:", db.cantidad_muestras())
