class GestionInventario:
    def __init__(self):
        self.inventario = {}

    def añadir_producto(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto] += cantidad
        else:
            self.inventario[producto] = cantidad
    def eliminar_producto(self, producto):
        self.inventario.pop(producto)
    def consultar_producto(self, producto):
        return self.inventario.get(producto, "Producto no existe en el inventario.")
    def mostrar_inventario(self):
        print("--- Inventario ---")
        for key, value in self.inventario.items():
            print(f"{key}: {value}")
        print("------------------")

mi_inventario = GestionInventario()
mi_inventario.añadir_producto("Manzanas", 10)
mi_inventario.añadir_producto("Peras", 5)
mi_inventario.añadir_producto("Manzanas", 5)

print("Consultar Manzanas:", mi_inventario.consultar_producto("Manzanas"))

mi_inventario.mostrar_inventario()

mi_inventario.eliminar_producto("Peras")
print(f"Inventario después de eliminar Peras:")
mi_inventario.mostrar_inventario()

