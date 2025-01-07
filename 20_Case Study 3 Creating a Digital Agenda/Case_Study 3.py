agenda_digital = {
    "Eustaquio Fernández": {
        "Dirección": "Calle Piruleta 1",
        "Correo electrónico": "eustaquiofernandez@gmail.com",
        "Teléfono": "666666999"
    },
    "Rigoberta Lala": {
        "Dirección": "Calle Piruleto 2",
        "Correo electrónico": "rigobertalala@gmail.com",
        "Teléfono": "999666999"
    }
}

def escribir_agenda(nombre_agenda, agenda_digital):
    """
    Escribe la agenda en un fichero en disco.
    """
    agenda_fichero = open(nombre_agenda, 'w')
    agenda_fichero.write(str(agenda_digital))
    agenda_fichero.close()

def leer_agenda(nombre_agenda):
    """
    Lee la agenda del fichero.
    """
    agenda_digital_lectura = open(nombre_agenda, "r")
    agenda_digital = agenda_digital_lectura.readlines()
    agenda_digital_lectura.close()
    return eval(agenda_digital[0])

def solicitar_contacto_agenda():
    """
    Solicita al usuario los datos para el nuevo contacto para la agenda.
    """
    solicitar_nombre = input("Escriba el nombre completo del contacto:")
    solicitar_direccion = input("Escriba la dirección donde vive:")
    solicitar_correo = input("Escriba su correo electrónico:")
    solicitar_telefono = input("Escriba su número de teléfono:")
    contacto = {
        "Nombre": solicitar_nombre,
        "Dirección": solicitar_direccion,
        "Correo electrónico": solicitar_correo,
        "Teléfono": solicitar_telefono
    }
    return contacto

def crear_contacto(agenda_digital, nuevo_contacto):
    """
    Introduce un nuevo contacto en la agenda.
    """
    agenda_digital[nuevo_contacto["Nombre"]] = {
        "Dirección": nuevo_contacto["Dirección"],
        "Correo electrónico": nuevo_contacto["Correo electrónico"],
        "Teléfono": nuevo_contacto["Teléfono"]
    }
    return agenda_digital

def consultar_contacto_agenda(agenda_digital):
    """
    Consulta un contacto en la agenda.
    """
    nombre_completo = input("Introduce el nombre completo del contacto: ")
    print("\n[+]", nombre_completo)
    print("\tDirección:", agenda_digital[nombre_completo]["Dirección"])
    print("\tCorreo electrónico:", agenda_digital[nombre_completo]["Correo electrónico"])
    print("\tTeléfono:", agenda_digital[nombre_completo]["Teléfono"])

# Probando el funcionamiento de la agenda
# Crear un contacto nuevo en la agenda

escribir_agenda("agenda_digital", agenda_digital)
agenda_digital = leer_agenda("agenda_digital")
nuevo_contacto = solicitar_contacto_agenda()
crear_contacto(agenda_digital, nuevo_contacto)
escribir_agenda("agenda_digital", agenda_digital)

# Consultar un contacto en la agenda

agenda_digital = leer_agenda("agenda_digital")
consultar_contacto_agenda(agenda_digital)