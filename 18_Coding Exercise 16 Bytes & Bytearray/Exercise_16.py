# Objetivo
# Implementa un "Codificador de comunicaciones" en Python utilizando Bytes.

# Solución
mensaje = b'Este es un mensaje secreto'

def crear_codigo_secreto(mensaje):
    repr_hex = mensaje[::2]
    repr_hex = repr_hex.hex()
    repr_bin = mensaje[::2]
    repr_bin_primero = bin(repr_bin[0])
    repr_bin_ultimo = bin(repr_bin[-1])
    repr_bin = repr_bin.decode('utf-8')
    codigo = repr_hex + repr_bin + repr_bin_primero + repr_bin_ultimo
    return codigo

print('Mensaje original:', mensaje)
print('Mensaje codificado:', crear_codigo_secreto(mensaje))