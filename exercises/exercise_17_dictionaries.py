# Objetivo
# Programa un "Gestor de Experiencia Laboral y Creación de CV" utilizando Diccionarios en Python.

# Solución
perfil_laboral = {
    "nombre": "Ana",
    "apellido": "Pérez",
    "edad": 30,
    "ciudad": "Madrid",
    "experiencias": ["Ingeniera de software en XYZ Corp"]
}
nueva_experiencia = "Gerente de proyecto en ABC Inc"

def agregar_experiencia(perfil_laboral, nueva_experiencia):
    perfil_laboral["experiencias"] += [nueva_experiencia]
    return perfil_laboral

def generar_cv_reducido(perfil_laboral):
    print(f'CV de {perfil_laboral["nombre"]} {perfil_laboral["apellido"]}\n Edad: {perfil_laboral["edad"]}, Ciudad: {perfil_laboral["ciudad"]}\n experiencia: {perfil_laboral["experiencias"]}')

cv_actualizado = agregar_experiencia(perfil_laboral, nueva_experiencia)
generar_cv_reducido(cv_actualizado)