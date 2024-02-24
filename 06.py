class GestionTareas:
    def __init__(self):
        self.idCounter = 1
        self.tareas = {}

    def agregar_tarea(self):
        tarea = input('Descripción de la tarea: ')
        estado = 'pendiente'
        self.tareas[self.idCounter] = [tarea, estado]
        self.idCounter += 1

    def actualizar_tarea(self):
        tarea_actualizar = int(input('ID de la tarea a actualizar: '))
        if tarea_actualizar in self.tareas:
            nueva_descripcion = input('Nueva descripción de la tarea: ')
            nuevo_estado = input('Nuevo estado de la tarea (pendiente/realizada): ')
            self.tareas[tarea_actualizar] = [nueva_descripcion, nuevo_estado]
        else:
            print('Tarea no encontrada')

    def lista_tareas(self):
        for key, value in self.tareas.items():
            print(f"ID: {key}, Descripción: {value[0]}, Estado: {value[1]}")

    def eliminar_tarea(self):
        tarea_eliminar = int(input('ID de la tarea a eliminar: '))
        if tarea_eliminar in self.tareas:
            self.tareas.pop(tarea_eliminar)
        else:
            print('Tarea no encontrada')

# Instanciamos la clase
gestor_tareas = GestionTareas()

while True:
    eleccion = input("""Menú de opciones - Gestión de Tareas:
          1) Agregar Tarea
          2) Actualizar Tarea
          3) Lista de Tareas
          4) Eliminar Tarea
          5) Salir
Eleccion: """)
    
    if eleccion == '1':
        gestor_tareas.agregar_tarea()
    elif eleccion == '2':
        gestor_tareas.actualizar_tarea()
    elif eleccion == '3':
        gestor_tareas.lista_tareas()
    elif eleccion == '4':
        gestor_tareas.eliminar_tarea()
    elif eleccion == '5':
        break
    else:
        print('Elección no válida')
