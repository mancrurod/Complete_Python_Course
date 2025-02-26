# Objetivo
# Programa "La Fiesta de Cumpleaños de Python" aplicando los conceptos de argumentos posicionales, de palabra clave y con valores por defecto en Python.

# Solución
def organizar_fiesta(invitados, tema="Python", lugar="aula de informática"):
    print(f"Preparando una fiesta para {invitados} invitados.")
    print(f"Tema de la fiesta: {tema}")
    print(f"Lugar de la celebración: {lugar}")

organizar_fiesta(10)
organizar_fiesta(10, tema="Python")
organizar_fiesta(10, tema="Python", lugar="Centro de deportes")