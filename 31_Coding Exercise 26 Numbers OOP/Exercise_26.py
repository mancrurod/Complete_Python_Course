class SimuladorPrestamo:
    def __init__(self, detalles_prestamo):
        self.años_prestamo = 30
        self.precio_vivienda = 300000
        self.tasa_mensual = (detalles_prestamo.imag / 12) / 100
        self.numero_pagos = self.años_prestamo * 12
        self.entrada = detalles_prestamo.real
        self.prestamo = self.precio_vivienda - self.entrada
        self.cuota_mensual = 0


    def calcular_pago_total(self):
        self.cuota_mensual = self.prestamo * (self.tasa_mensual * (1 + self.tasa_mensual) ** self.numero_pagos) / (
                    (1 + self.tasa_mensual) ** self.numero_pagos - 1)
        return self.cuota_mensual

    def mostrar_resultados(self):
        print(
            f"----- Simulación Hipoteca -----\nPara una vivienda de {self.precio_vivienda} aportando una entrada de {self.entrada} euros y con una tasa de interés del 2.5% anual durante {self.años_prestamo} años:\nCuota mensual a pagar: {self.cuota_mensual} euros\n----- Fin de la Simulación -----")

prestamo = SimuladorPrestamo(50000+2.5j)
prestamo.calcular_pago_total()
prestamo.mostrar_resultados()