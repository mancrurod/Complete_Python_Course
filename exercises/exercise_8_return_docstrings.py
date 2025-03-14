# Objetivo

# Desarrollar un "Generador de Mensajes Personalizados" utilizando funciones en Python. El enfoque principal será en la sentencia return, la implementación de argumentos, el uso de strings y la incorporación de docstrings para la documentación de funciones.

# Solución
nombre = "Santiago"


def generar_mensaje(arg1, arg2="Bienvenido al curso de Python"):
    """Generador de mensajes personalizados

    Keyword arguments:
    arg1 -- nombre de la persona
    arg2 -- mensaje de bienvenida
    """
    return f"¡Hola, {arg1}! {arg2}"


generar_mensaje(nombre)