# Objetivo
# Descifrar los "Mensajes Secretos de una Carta de Amor" usando strings, indexación, slicing, stride y strings de múltiples líneas en Python.

# Solución
parrafo1 = "Cada dia te quiero mas y nunca lo he olvidado."

parrafo2 = "En el corazón de una historia de amor tecnológica, Lucas y Carla compartían su pasión por la programación. Cada día, mientras aprendían a programar, sus corazones se sincronizaban con cada línea de código."

parrafo3 = "En cada amanecer, veo el brillo de tus ojos; en cada atardecer, siento el calor de tu abrazo; y en cada noche estrellada, me pierdo en el infinito de tu amor."

mensajes = "Mensajes Secretos Decodificados:"
mensaje_uno = "Mensaje secreto 1:"
mensaje_dos = "Mensaje secreto 2:"
mensaje_tres = "Mensaje secreto 3:"

mensaje_secreto1 = parrafo1[1::18]

mensaje_secreto2 = parrafo2[138:147]

mensaje_secreto3_1 = parrafo3[125]
mensaje_secreto3_2 = parrafo3[94]
mensaje_secreto3_3 = parrafo3[35]
mensaje_secreto3_4 = parrafo3[107]
mensaje_secreto3_5 = parrafo3[20]
mensaje_secreto3_6 = parrafo3[1]

print("Mensajes Secretos Decodificados:")
print("Mensaje secreto 1:")
print(mensaje_secreto1)
print("Mensaje secreto 2:")
print(mensaje_secreto2)
print("Mensaje secreto 3:")
print(mensaje_secreto3_1)
print(mensaje_secreto3_2)
print(mensaje_secreto3_3)
print(mensaje_secreto3_4)
print(mensaje_secreto3_5)
print(mensaje_secreto3_6)