# Objetivo
# En este ejercicio práctico se propone la implementación en Python 3 de tres de las funciones de activación más populares en el diseño de redes neuronales artificiales profundas, las funciones ReLu, Sigmoid y Tanh.

# 1. ReLu
def relu(x):
    valor = max(0, x)
    print(valor)

# 2. Sigmoid
from math import e
def sigmoid(x):
    abajo = 1 + e ** -x
    arriba = 1
    valor = arriba / abajo
    print(valor)

# 3. Tanh
def tanh(x):
    arriba = (e ** x - e ** -x) / 2
    abajo = (e ** x + e ** -x) / 2
    resultado_tanh = arriba / abajo
    print(resultado_tanh)