# Objetivo
# Programa un "Organizador de Biblioteca Personal" utilizando listas.


# Solución
def aumentar_biblioteca(nuevo_libro):
    """
    Añade un nuevo libro al final de la lista de libros leídos.

    Args:
        nuevo_libro (str): El título del libro a añadir a la lista.

    Returns:
        list: Lista actualizada de libros leídos, incluyendo el nuevo libro.

    """
    # Lectura del listado de libros leidos
    archivo = open("libros.txt", "r")
    libros = archivo.read().splitlines()
    archivo.close()

    # Agregando el nuevo libro al final de la lista
    libros += [nuevo_libro]
    return libros


def primer_libro_leido(libros):
    """
    Devuelve el título del primer libro leído de una lista de libros.

    Args:
        libros (list): Lista de libros leídos.

    Returns:
        str: Título del primer libro leído.

    """
    return libros[0]


# Nuevo libro
nuevo_libro = "Las Aventuras de Huckleberry Finn"

# Llamando a la función para actualizar la biblioteca
biblioteca = aumentar_biblioteca(nuevo_libro)
print("La biblioteca de libros leídos es:")
print(biblioteca)

# Llamando a la función para saber cuál fue el primer libro leído
primer_libro = primer_libro_leido(biblioteca)
print(f'El primer libro que he leído es: "{primer_libro}"')