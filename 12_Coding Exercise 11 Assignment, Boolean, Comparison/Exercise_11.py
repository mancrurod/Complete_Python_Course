# Objetivo
# Comparador de longitudes de palabras

# Solución
def comparar_longitud(palabra1, palabra2):
    longitud1 = len(palabra1)
    longitud2 = len(palabra2)
    valor = longitud1 == longitud2
    return valor

print(f"¿Son «gato» y «perro» dos palabras con la misma longitud? {comparar_longitud('gato', 'perro')}")