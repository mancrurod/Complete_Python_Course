class AnalisisVentas:
    """Clase para analizar datos de ventas almacenados en una tupla.

    Atributos:
        datos_ventas (tuple): Una tupla que contiene las cifras de ventas.
    """

    def __init__(self, datos_ventas):
        """Inicializa la clase con una tupla de datos de ventas.

        Args:
            datos_ventas (tuple): Una tupla con las cifras de ventas.
        """
        self.datos_ventas = datos_ventas

    def venta_maxima(self):
        """Encuentra la venta máxima y su índice en la tupla de datos.

        Returns:
            tuple: Una tupla con el índice y el valor de la venta máxima.
        """
        valor_maximo = max(self.datos_ventas)
        indice_maximo = self.datos_ventas.index(valor_maximo)
        return indice_maximo, valor_maximo

    def venta_minima(self):
        """Encuentra la venta mínima y su índice en la tupla de datos.

        Returns:
            tuple: Una tupla con el índice y el valor de la venta mínima.
        """
        valor_minimo = min(self.datos_ventas)
        indice_minimo = self.datos_ventas.index(valor_minimo)
        return indice_minimo, valor_minimo

    def frecuencia_venta(self, venta):
        """Cuenta cuántas veces aparece una cifra de venta en la tupla.

        Args:
            venta (int o float): La cifra de venta a contar.

        Returns:
            int: El número de veces que aparece la cifra de venta.
        """
        return self.datos_ventas.count(venta)


# Ejecución del programa
ventas = (100, 150, 150, 50, 250, 300, 100, 350, 200, 200, 150)
analizador = AnalisisVentas(ventas)

# Encontrar la venta máxima
indice_max, valor_max = analizador.venta_maxima()
print(f"La venta máxima tiene el índice {indice_max} y es {valor_max}.")

# Encontrar la venta mínima
indice_min, valor_min = analizador.venta_minima()
print(f"La venta mínima tiene el índice {indice_min} y es {valor_min}.")

# Contar la frecuencia de una venta específica
frecuencia = analizador.frecuencia_venta(200)
print(f"Frecuencia de la venta por un valor de 200 es {frecuencia}.")