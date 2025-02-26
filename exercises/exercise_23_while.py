# Objetivo
# En este caso práctico se propone al alumno la "Creación del software de un ascensor". Para ello, debe hacer uso de la sentencia de control de flujo While en Python.

# Solución
def mover_ascensor(piso_actual, piso_deseado):
    while piso_actual != piso_deseado:
        if piso_actual < piso_deseado:
            print(f"Subiendo al piso {piso_deseado}. Piso actual: {piso_actual}")
            piso_actual += 1
        elif piso_actual > piso_deseado:
            print(f"Bajando al piso {piso_deseado}. Piso actual: {piso_actual}")
            piso_actual -= 1
    print(f"Piso {piso_deseado} alcanzado")

mover_ascensor(1, 6)