class Animal:
    def __init__(self, nombre, especie, edad, habitat):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.habitat = habitat

    def mostrar_info(self):
        print(f"--> Nombre: {self.nombre}\nEspecie: {self.especie}\nEdad: {self.edad}\nHábitat: {self.habitat.tipo_habitat}, {self.habitat.temperatura}")

class Habitat:
    def __init__(self, tipo_habitat, temperatura):
        self.tipo_habitat = tipo_habitat
        self.temperatura = temperatura

class Mamifero(Animal):
    def __init__(self, nombre, especie, edad, habitat, tipo_pelaje):
        super().__init__(nombre, especie, edad, habitat)
        self.tipo_pelaje = tipo_pelaje

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de pelaje: {self.tipo_pelaje}")


class Ave(Animal):
    def __init__(self, nombre, especie, edad, habitat, tipo_plumaje):
        super().__init__(nombre, especie, edad, habitat)
        self.tipo_plumaje = tipo_plumaje

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de pelaje: {self.tipo_plumaje}")


class Zoologico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def añadir_animal(self, animal):
        self.animales += [animal]

    def mostrar_animales(self):
        print(f"Animales en {self.nombre}:")
        for animal in self.animales:
            print(f"--> {animal.mostrar_info()}\n")


zoo = Zoologico("ZooFantástico")

habitat_sabana = Habitat("Sabana", "Cálido")
habitat_bosque = Habitat("Bosque", "Templado")

simba = Mamifero("Simba", "León", 5, habitat_sabana, "Corto")
piolin = Ave("Piolín", "Canario", 2, habitat_bosque, "Suave")

zoo.añadir_animal(simba)
zoo.añadir_animal(piolin)

zoo.mostrar_animales