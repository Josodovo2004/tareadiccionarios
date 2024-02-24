class GestionEmpleados:
    def __init__(self):
        self.idCounter = 1
        self.listaEmpleados = {}

    def registrar_empleado(self):
        nombre = input('Nombre del empleado: ')
        posicion = input('Posición del empleado: ')
        salario = float(input('Salario del empleado: '))
        self.listaEmpleados[self.idCounter] = [nombre, posicion, salario]
        self.idCounter += 1

    def actualizar_empleado(self):
        empleado_actualizar = int(input('ID del empleado a actualizar: '))
        if empleado_actualizar in self.listaEmpleados:
            nombre = input('Nuevo nombre del empleado: ')
            posicion = input('Nueva posición del empleado: ')
            salario = float(input('Nuevo salario del empleado: '))
            self.listaEmpleados[empleado_actualizar] = [nombre, posicion, salario]
        else:
            print('Empleado no encontrado.')

    def lista_empleados(self):
        for empleado_id, detalles_empleado in self.listaEmpleados.items():
            print(f"ID: {empleado_id}, Nombre: {detalles_empleado[0]}, Posición: {detalles_empleado[1]}, Salario: {detalles_empleado[2]}")

    def eliminar_empleado(self):
        empleado_eliminar = int(input('ID del empleado a eliminar: '))
        if empleado_eliminar in self.listaEmpleados:
            del self.listaEmpleados[empleado_eliminar]
            print('Empleado eliminado.')
        else:
            print('Empleado no encontrado.')

# Ejemplo de uso
gestor_empleados = GestionEmpleados()

while True:
    eleccion = input("""Menú de opciones - Empleados:
                     1) Registrar Empleado
                     2) Actualizar Empleado
                     3) Lista Empleados
                     4) Eliminar Empleado
                     5) Salir
Eleccion: """)
    if eleccion == '1':
        gestor_empleados.registrar_empleado()
    elif eleccion == '2':
        gestor_empleados.actualizar_empleado()
    elif eleccion == '3':
        gestor_empleados.lista_empleados()
    elif eleccion == '4':
        gestor_empleados.eliminar_empleado()
    elif eleccion == '5':
        break
    else:
        print('Elección no válida')
