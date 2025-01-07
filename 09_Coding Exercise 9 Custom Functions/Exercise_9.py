# Objetivo
# Combinar el aprendizaje de funciones básicas de Python como print, len, str, int, float, y type con la creación de funciones personalizadas para profundizar en la comprensión y manipulación de tipos de datos básicos.

# Solución
def contar_caracteres(str):
    caracteres_str = len(str)
    print(f"La frase '{str}' tiene {caracteres_str} caracteres.")

contar_caracteres("Aprender Python es divertido")

def convertir_numero(value):
    número_str = str(value)
    número_float = float(value)
    print(f"Entero: {value}, Tipo: {type(value)}")
    print(f"Cadena: {número_str}, Tipo: {type(número_str)}")
    print(f"Flotante: {número_float}, Tipo: {type(número_float)}")

convertir_numero(42)