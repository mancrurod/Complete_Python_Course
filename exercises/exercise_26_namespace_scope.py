# Objetivo
# En esta práctica se propone la "Creación de un Simulador de Ecosistema". El alumno debe desarrollar un simulador básico de ecosistema que demuestre el concepto de namespaces y scopes en Python. En este simulador, los animales interactúan en un ecosistema con recursos limitados.

# Solución
recursos_ecosistema = {"agua": 1000, "alimento": 800}
def animal_interactua(animal, cantidad_alimentos, cantidad_agua=None):
    global recursos_ecosistema
    if animal == "herbívoro":
        if recursos_ecosistema["agua"] >= cantidad_agua and recursos_ecosistema["alimento"] >= cantidad_alimentos:
            recursos_ecosistema['agua'] -= cantidad_agua
            recursos_ecosistema['alimento'] -= cantidad_alimentos
            print(f"Un herbívoro ha consumido {cantidad_agua} de agua y {cantidad_alimentos} de alimento.")
            print(f"Estado actual del ecosistema: {recursos_ecosistema}")
        else:
            print("Recursos insuficientes en el ecosistema.")
    elif animal == "carnívoro":
        if recursos_ecosistema["alimento"] >= cantidad_alimentos:
            recursos_ecosistema['alimento'] -= cantidad_alimentos
            print(f"Un carnívoro ha consumido {cantidad_alimentos} de alimento.")
            print(f"Estado actual del ecosistema: {recursos_ecosistema}")
        else:
            print("Recursos insuficientes en el ecosistema.")

def lluvia(unidades_agua):
    global recursos_ecosistema
    recursos_ecosistema['agua'] += unidades_agua
    print(f"¡Ha llovido! Se añadieron {unidades_agua} unidades de agua al ecosistema.")

print(f"Inicio del día en el ecosistema: {recursos_ecosistema}")
animal_interactua("herbívoro", 100, 200)
animal_interactua("carnívoro", 50)
lluvia(200)
print(f"Fin del día en el ecosistema: {recursos_ecosistema}")