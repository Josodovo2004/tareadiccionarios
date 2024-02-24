class RegistroActividades:
    def __init__(self) -> None:
        self.idCounter = 1
        self.listaActividades = {}

    def registrar_actividad(self):
        fecha = input('Fecha de la actividad (YYYY-MM-DD): ')
        actividad = input('Actividad: ')
        duracion = input('Duración de la actividad (en horas): ')
        self.listaActividades[self.idCounter] = [fecha, actividad, duracion]
        self.idCounter += 1

    def actualizar_actividad(self):
        actividad_actualizar = input('Actividad a actualizar: ')
        for key in self.listaActividades.keys():
            if actividad_actualizar in self.listaActividades[key]:
                fecha = input('Fecha de la actividad (YYYY-MM-DD): ')
                actividad = input('Nueva actividad: ')
                duracion = input('Nueva duración de la actividad (en horas): ')
                self.listaActividades[key] = [fecha, actividad, duracion]
                break

    def lista_actividades(self):
        for key, value in self.listaActividades.items():
            print(f"ID: {key}, Fecha: {value[0]}, Actividad: {value[1]}, Duración: {value[2]} horas")

    def eliminar_actividad(self):
        actividad_eliminar = input('Actividad a eliminar: ')
        for key, value in self.listaActividades.items():
            if actividad_eliminar in value:
                self.listaActividades.pop(key)
                break

# Ejemplo de uso con bucle while y menú de opciones
registro_actividades = RegistroActividades()

while True:
    print("\nMenú de opciones - Registro de Actividades Diarias:")
    print("1) Registrar Actividad")
    print("2) Actualizar Actividad")
    print("3) Lista de Actividades")
    print("4) Eliminar Actividad")
    print("5) Salir")

    eleccion = input("Elección: ")

    if eleccion == '1':
        registro_actividades.registrar_actividad()
    elif eleccion == '2':
        registro_actividades.actualizar_actividad()
    elif eleccion == '3':
        registro_actividades.lista_actividades()
    elif eleccion == '4':
        registro_actividades.eliminar_actividad()
    elif eleccion == '5':
        break
    else:
        print('Elección no válida')
