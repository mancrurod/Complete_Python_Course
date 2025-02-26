# Objetivo
# Programa un "Gestor de Información Personal" utilizando Tuplas en Python.

# Solución
def gestionar_informacion(datos_personales):
    nombre, edad, ciudad = datos_personales
    nacimiento = 2024 - edad
    datos_modificados = (nombre, nacimiento, ciudad)
    return datos_personales, datos_modificados

datos_personales = ("Ana", 30, "Madrid")
original, modificado = gestionar_informacion(datos_personales)

print('Tupla original:', original)
print('Tupla modificada:', modificado)