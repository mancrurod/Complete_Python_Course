# Objetivo
# En este ejercicio práctico se propone la creación de una sencilla aplicación en Python que nos ayude a verificar la integridad de un mensaje calculando la función hash de una cadena de texto que el usuario le proporcione.

# Solución

def mensaje_cabecera():
  mensaje = """
 _____      _                  _     _           _
|_   _|    | |                (_)   | |         | |
  | | _ __ | |_ ___  __ _ _ __ _  __| | __ _  __| |
  | || '_ \| __/ _ \/ _` | '__| |/ _` |/ _` |/ _` |
 _| || | | | ||  __/ (_| | |  | | (_| | (_| | (_| |
 \___/_| |_|\__\___|\__, |_|  |_|\__,_|\__,_|\__,_|
                     __/ |
                    |___/
     _      _
    | |    | |
  __| | ___| |
 / _` |/ _ \ |
| (_| |  __/ |
 \__,_|\___|_|


                                _
                               (_)
 _ __ ___   ___ _ __  ___  __ _ _  ___
| '_ ` _ \ / _ \ '_ \/ __|/ _` | |/ _ \
| | | | | |  __/ | | \__ \ (_| | |  __/
|_| |_| |_|\___|_| |_|___/\__,_| |\___|
                              _/ |
                             |__/



░  ░░░░  ░░░      ░░░   ░░░  ░░░      ░░░       ░░░  ░░░░  ░░       ░░░░      ░░░       ░░
▒   ▒▒   ▒▒  ▒▒▒▒  ▒▒    ▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒
▓        ▓▓  ▓▓▓▓  ▓▓  ▓  ▓  ▓▓  ▓▓▓▓▓▓▓▓       ▓▓▓  ▓▓▓▓  ▓▓       ▓▓▓  ▓▓▓▓  ▓▓  ▓▓▓▓  ▓
█  █  █  ██        ██  ██    ██  ████  ██  ███  ███  ████  ██  ███  ███  ████  ██  ████  █
█  ████  ██  ████  ██  ███   ███      ███  ████  ███      ███  ████  ███      ███       ██


"""
  print(mensaje)

def calcular_hash(cadena):
   id_hash = hash(cadena)
   return id_hash

def solicitar_cadena():
  cadena = input("Introduce una cadena de texto: ")
  return cadena

def main():
  mensaje_cabecera()
  cadena = solicitar_cadena()
  id_hash = calcular_hash(cadena)
  print("El hash de la cadena es: ", id_hash)

main()