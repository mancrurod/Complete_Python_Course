# Objetivo
# Programar un juego de Adivinanza con Letras y Palabras. Este ejercicio tiene como objetivo que practiques con operadores de pertenencia, comparación y operadores lógicos en Python.

# Solución
palabra_adivinar = "mesopotámico"

def adivinar_palabra(letra_prueba, palabra_intento):
    letra_en_palabra = letra_prueba in palabra_adivinar
    print('¿La letra de prueba se encuentra en la palabra?', letra_en_palabra)
    resultado_adivinanza = (palabra_intento == palabra_adivinar) and (len(palabra_intento) == len(palabra_adivinar))
    print('El jugador gana:', resultado_adivinanza)

adivinar_palabra('o', 'mesopotámico')