# Objetivo
# Imagina que estás a cargo de una galería de arte y necesitas asegurarte de que cada pieza de arte sea única. Implementa un programa en Python que utilice sets para lograr este objetivo.

# Solución
# Coleccion de arte con elementos duplicados
coleccion = [
    "Mona Lisa", "El Grito", "Mona Lisa", "La Noche Estrellada",
    "Las Meninas", "Guernica", "La Última Cena", "La Creación de Adán",
    "La Persistencia de la Memoria", "La Libertad guiando al pueblo",
    "El Beso", "Nacimiento de Venus", "El Jardín de las Delicias",
    "La Joven de la Perla", "El David",
    "Los Girasoles", "La Gran Ola de Kanagawa",
    "La Ronda Nocturna", "American Gothic",
    "Los Jugadores de Cartas", "La Noche Estrellada",
    "La Última Cena", "Guernica", "Las Meninas",
    "La Persistencia de la Memoria", "Mona Lisa"
]

def revisar_coleccion(coleccion):
    coleccion_set = list(set(coleccion))
    return coleccion_set

coleccion_limpia = revisar_coleccion(coleccion)

print('Colección antes de la revisión:', coleccion)
print('Colección después de la revisión:', coleccion_limpia)