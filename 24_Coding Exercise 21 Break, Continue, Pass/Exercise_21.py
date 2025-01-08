# Objetivo
# En este caso práctico se propone al alumno "Programar el software de un despertador". Para ello debe hacer uso de las sentencias de control de flujo vistas en clases anteriores en combinación con las sentencias break, continue y pass.

# Solución
def simulador_alarma(tiempo_total):
    segundo_actual = 0
    while segundo_actual <= tiempo_total:
        segundo_actual += 1
        if segundo_actual % 10 == 0:
            print(f"Omitiendo alarma en segundo {segundo_actual}")
            continue
        print(f"Alarma activada, segundo actual: {segundo_actual}")
        if segundo_actual == tiempo_total:
            break
    print(f"Alarma desactivada a los {segundo_actual} segundos")


simulador_alarma(21)