class GestionProyectos:
    def __init__(self) -> None:
        self.proyectos = {}

    def crear_proyecto(self, nombre_proyecto):
        if nombre_proyecto not in self.proyectos:
            self.proyectos[nombre_proyecto] = []
            print(f"Proyecto '{nombre_proyecto}' creado.")
        else:
            print("Ya existe un proyecto con ese nombre.")

    def agregar_miembro(self, nombre_proyecto, nombre_miembro):
        if nombre_proyecto in self.proyectos:
            if nombre_miembro not in self.proyectos[nombre_proyecto]:
                self.proyectos[nombre_proyecto].append(nombre_miembro)
                print(f"Miembro '{nombre_miembro}' agregado al proyecto '{nombre_proyecto}'.")
            else:
                print("Este miembro ya está en el proyecto.")
        else:
            print("Proyecto no encontrado.")

    def mostrar_proyectos(self):
        if not self.proyectos:
            print("No hay proyectos registrados.")
        else:
            for proyecto, miembros in self.proyectos.items():
                print(f"Proyecto: {proyecto}, Miembros: {', '.join(miembros)}")

    def eliminar_proyecto(self, nombre_proyecto):
        if nombre_proyecto in self.proyectos:
            del self.proyectos[nombre_proyecto]
            print(f"Proyecto '{nombre_proyecto}' eliminado.")
        else:
            print("Proyecto no encontrado.")

gestor_proyectos = GestionProyectos()

while True:
    print("\nMenú de opciones - Gestión de Proyectos:")
    print("1) Crear Proyecto")
    print("2) Agregar Miembro a Proyecto")
    print("3) Mostrar Proyectos y Miembros")
    print("4) Eliminar Proyecto")
    print("5) Salir")

    eleccion = input("Elección: ")

    if eleccion == '1':
        nombre_proyecto = input("Nombre del proyecto: ")
        gestor_proyectos.crear_proyecto(nombre_proyecto)
    elif eleccion == '2':
        nombre_proyecto = input("Nombre del proyecto: ")
        nombre_miembro = input("Nombre del miembro: ")
        gestor_proyectos.agregar_miembro(nombre_proyecto, nombre_miembro)
    elif eleccion == '3':
        gestor_proyectos.mostrar_proyectos()
    elif eleccion == '4':
        nombre_proyecto = input("Nombre del proyecto a eliminar: ")
        gestor_proyectos.eliminar_proyecto(nombre_proyecto)
    elif eleccion == '5':
        break
    else:
        print('Elección no válida')
