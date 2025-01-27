class GeneradorNombresUsuario:
    def __init__(self, nombre, apellido, año_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.año_nacimiento = año_nacimiento
        self.nombre_usuario = ""

    def generar_nombre_usuario(self):
        nombre = self.nombre.lower()
        apellido = self.apellido.upper()
        nombre_apellido = ''.join([nombre, apellido])
        self.nombre_usuario = nombre_apellido + self.año_nacimiento

    def validar_nombre_usuario(self):
        if len(self.nombre_usuario) >= 8 and self.nombre_usuario[-4:].isdigit():
            return True
        else:
            return False

    def mostrar_nombre_usuario(self):
        if self.validar_nombre_usuario():
            print("Nombre de usuario generado: {}".format(self.nombre_usuario))
        else:
            print("El nombre de usuario no cumple con los criterios de validación.")

datos = GeneradorNombresUsuario("Santiago", "Hernandez", "1994")
datos.generar_nombre_usuario()
datos.mostrar_nombre_usuario()