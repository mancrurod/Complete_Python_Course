class GestionAsistencia:
    """
    Clase para gestionar la asistencia de estudiantes a actividades universitarias.

    Atributos:
        asistentes_actividad_A (set): Conjunto de estudiantes que asistieron a la actividad A.
        asistentes_actividad_B (set): Conjunto de estudiantes que asistieron a la actividad B.
    """

    def __init__(self):
        """
        Inicializa la clase con dos sets vacíos para almacenar asistentes de las actividades A y B.
        """
        self.asistentes_actividad_A = set()
        self.asistentes_actividad_B = set()

    def añadir_asistente(self, actividad, estudiante):
        """
        Añade un estudiante al conjunto de asistentes de una actividad específica.

        Args:
            actividad (str): Nombre de la actividad ('A' o 'B').
            estudiante (str): Nombre del estudiante que asistió a la actividad.
        """
        if actividad == 'A':
            self.asistentes_actividad_A.add(estudiante)
        elif actividad == 'B':
            self.asistentes_actividad_B.add(estudiante)
        else:
            print("Actividad no válida. Use 'A' o 'B'.")

    def asistencia_total(self):
        """
        Retorna un conjunto con todos los estudiantes que asistieron a al menos una actividad.

        Returns:
            set: Conjunto de estudiantes que asistieron a la actividad A, B o ambas.
        """
        return self.asistentes_actividad_A.union(self.asistentes_actividad_B)

    def asistencia_comun(self):
        """
        Retorna un conjunto con los estudiantes que asistieron a ambas actividades (A y B).

        Returns:
            set: Conjunto de estudiantes que asistieron a ambas actividades.
        """
        return self.asistentes_actividad_A.intersection(self.asistentes_actividad_B)

    def diferencia_actividad_A(self):
        """
        Retorna un conjunto con los estudiantes que asistieron exclusivamente a la actividad A.

        Returns:
            set: Conjunto de estudiantes que solo asistieron a la actividad A.
        """
        return self.asistentes_actividad_A.difference(self.asistentes_actividad_B)

    def diferencia_actividad_B(self):
        """
        Retorna un conjunto con los estudiantes que asistieron exclusivamente a la actividad B.

        Returns:
            set: Conjunto de estudiantes que solo asistieron a la actividad B.
        """
        return self.asistentes_actividad_B.difference(self.asistentes_actividad_A)

gestion = GestionAsistencia()

# Añadimos asistentes a las actividades
gestion.añadir_asistente('A', 'Ana')
gestion.añadir_asistente('A', 'Juan')
gestion.añadir_asistente('B', 'Luis')
gestion.añadir_asistente('B', 'Ana')

# Imprimimos los resultados
print("Asistentes actividad A:", gestion.asistentes_actividad_A)
print("Asistentes actividad B:", gestion.asistentes_actividad_B)
print("Asistencia total:", gestion.asistencia_total())
print("Asistencia común:", gestion.asistencia_comun())
print("Diferencia actividad A:", gestion.diferencia_actividad_A())
print("Diferencia actividad B:", gestion.diferencia_actividad_B())