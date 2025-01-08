# Objetivo
# Programa una aplicación "TO-DO List" que recoja la lista de tareas que tienes pendientes de realizar. Para ello, utiliza la estructura de control de flujo for en Python.

# Solución
def añadir_tarea(tarea_nueva):
    tareas_archivo = open("tareas.txt", "r")
    tareas = tareas_archivo.read().splitlines()
    tareas += [tarea_nueva]
    return tareas


def gestionar_tareas(tareas):
    print("Tareas pendientes de realizar:")
    num_tareas = 0
    for tarea_pendiente in tareas:
        num_tareas += 1
        print(f"{num_tareas}. {tarea_pendiente}")
    print(f"Hay {num_tareas} tareas pendientes de realizar.")


tarea_nueva = "Pagar la factura del internet."
tareas = añadir_tarea(tarea_nueva)
gestionar_tareas(tareas)



