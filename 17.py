class GestionRecetas:
    def __init__(self):
        self.recetas = {}

    def agregar_receta(self, nombre_plato, receta):
        if nombre_plato not in self.recetas:
            self.recetas[nombre_plato] = receta
            print(f"Receta para '{nombre_plato}' agregada.")
        else:
            print("Ya existe una receta con ese nombre.")

    def obtener_receta(self, nombre_plato):
        if nombre_plato in self.recetas:
            print(f"Receta para '{nombre_plato}': {self.recetas[nombre_plato]}")
        else:
            print("Receta no encontrada.")

    def mostrar_recetas(self):
        if not self.recetas:
            print("No hay recetas registradas.")
        else:
            print("Recetas disponibles:")
            for plato, receta in self.recetas.items():
                print(f"{plato}: {receta}")

    def eliminar_receta(self, nombre_plato):
        if nombre_plato in self.recetas:
            del self.recetas[nombre_plato]
            print(f"Receta para '{nombre_plato}' eliminada.")
        else:
            print("Receta no encontrada.")

gestor_recetas = GestionRecetas()

while True:
    print("\nMenú de opciones - Gestión de Recetas de Cocina:")
    print("1) Agregar Receta")
    print("2) Obtener Receta")
    print("3) Mostrar Recetas")
    print("4) Eliminar Receta")
    print("5) Salir")

    eleccion = input("Elección: ")

    if eleccion == '1':
        nombre_plato = input("Nombre del plato: ")
        receta = input("Receta: ")
        gestor_recetas.agregar_receta(nombre_plato, receta)
    elif eleccion == '2':
        nombre_plato = input("Nombre del plato: ")
        gestor_recetas.obtener_receta(nombre_plato)
    elif eleccion == '3':
        gestor_recetas.mostrar_recetas()
    elif eleccion == '4':
        nombre_plato = input("Nombre del plato a eliminar: ")
        gestor_recetas.eliminar_receta(nombre_plato)
    elif eleccion == '5':
        break
    else:
        print('Elección no válida')
