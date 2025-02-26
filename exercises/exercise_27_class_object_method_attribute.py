# Objetivo
# En este caso práctico se propone al alumno "Crear un software para la gestión de una biblioteca". Para ello el alumno debe hacer uso de clases, objetos, métodos y atributos en Python.

# Solución
class Libro:
    """Definimos la clase Libro."""

    def __init__(self, titulo, autor, isbn):
        """Incluye los siguientes atributos: título, autor, isbn y disponible

        titulo -- str que indica el título de la obra
        autor -- str que indica el autor de la obra
        isbn -- str que indica el número ISBN de la obra
        disponible -- bool que indica si la obra está disponible o no para préstamo
        """
        self.disponible = True
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def informacion(self):
        """Devuelve la información del libro como string."""
        print(f"--> Informacion del libro: {self.titulo}")
        print("Titulo:", self.titulo)
        print("Autor:", self.autor)
        print("ISBN:", self.isbn)

    def prestar_libro(self):
        if self.disponible is True:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
            print(f"--> Informacion del libro: {self.titulo}\n{self.informacion()}")
        else:
            print("Este libro ya está prestado.")

    def devolver_libro(self):
        if self.disponible is False:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto a la biblioteca.")
            print(f"--> Informacion del libro: {self.titulo}\n{self.informacion()}")
        else:
            print("Este libro ya está en la biblioteca.")


harry_potter = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "978-0747532743")
george_orwell = Libro("1984", "George Orwell", "978-0451524935")

harry_potter.prestar_libro()
harry_potter.devolver_libro()
george_orwell.prestar_libro()
george_orwell.prestar_libro()



