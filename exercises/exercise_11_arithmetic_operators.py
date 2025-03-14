# Objetivo
Crear un "Simulador de Calculadora de Calorías" utilizando operadores aritméticos en Python, integrando conocimientos previos sobre funciones, strings, y variables.

# Solución
def calcular_calorias(carbohidratos, proteinas, grasas):
    calorias = (carbohidratos * 4) + (proteinas * 4) + (grasas * 9)
    return calorias

calorias_totales = calcular_calorias(10, 40, 5)
print("Calorías totales:", calorias_totales)