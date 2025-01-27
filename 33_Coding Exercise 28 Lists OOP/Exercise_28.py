class SistemaCalificaciones:
    def __init__(self):
        self.calificaciones = []

    def añadir_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def mostrar_calificaciones(self):
        for calificacion in self.calificaciones:
            print(calificacion)

    def calificacion_promedio(self):
        if not self.calificaciones:
            promedio = 0
            return promedio
        else:
            promedio = sum(self.calificaciones) / len(self.calificaciones)
            return promedio

    def ordenar_calificaciones(self):
        self.calificaciones.sort(reverse=False)


mis_notas = SistemaCalificaciones()
mis_notas.añadir_calificacion(8)
mis_notas.añadir_calificacion(9.5)
mis_notas.añadir_calificacion(7)
mis_notas.añadir_calificacion(10)

print(f"Calificaciones originales:")
mis_notas.mostrar_calificaciones()
print(f"Promedio:{mis_notas.calificacion_promedio()}")
mis_notas.ordenar_calificaciones()
print("Calificaciones ordenadas:")
mis_notas.mostrar_calificaciones()