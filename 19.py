class GestionAlquilerVehiculos:
    def __init__(self):
        self.vehiculos = {}

    def agregar_vehiculo(self, nombre_vehiculo, modelo, disponibilidad=True):
        if nombre_vehiculo not in self.vehiculos:
            self.vehiculos[nombre_vehiculo] = {'modelo': modelo, 'disponible': disponibilidad}
            print(f"Vehículo '{nombre_vehiculo}' agregado al sistema.")
        else:
            print("Este vehículo ya está registrado.")

    def eliminar_vehiculo(self, nombre_vehiculo):
        if nombre_vehiculo in self.vehiculos:
            del self.vehiculos[nombre_vehiculo]
            print(f"Vehículo '{nombre_vehiculo}' eliminado del sistema.")
        else:
            print("Vehículo no encontrado.")

    def mostrar_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos registrados.")
        else:
            print("Vehículos registrados:")
            for vehiculo, info in self.vehiculos.items():
                print(f"{vehiculo} - Modelo: {info['modelo']}, Disponible: {info['disponible']}")

    def alquilar_vehiculo(self, nombre_vehiculo):
        if nombre_vehiculo in self.vehiculos:
            if self.vehiculos[nombre_vehiculo]['disponible']:
                self.vehiculos[nombre_vehiculo]['disponible'] = False
                print(f"Vehículo '{nombre_vehiculo}' alquilado.")
            else:
                print(f"El vehículo '{nombre_vehiculo}' no está disponible para alquiler.")
        else:
            print("Vehículo no encontrado.")

    def devolver_vehiculo(self, nombre_vehiculo):
        if nombre_vehiculo in self.vehiculos:
            if not self.vehiculos[nombre_vehiculo]['disponible']:
                self.vehiculos[nombre_vehiculo]['disponible'] = True
                print(f"Vehículo '{nombre_vehiculo}' devuelto correctamente.")
            else:
                print(f"El vehículo '{nombre_vehiculo}' ya está disponible.")
        else:
            print("Vehículo no encontrado.")

gestor_alquiler = GestionAlquilerVehiculos()

while True:
    print("\nMenú de opciones - Sistema de Alquiler de Vehículos:")
    print("1) Agregar Vehículo")
    print("2) Eliminar Vehículo")
    print("3) Mostrar Vehículos")
    print("4) Alquilar Vehículo")
    print("5) Devolver Vehículo")
    print("6) Salir")

    eleccion = input("Elección: ")

    if eleccion == '1':
        nombre_vehiculo = input("Nombre del vehículo: ")
        modelo = input("Modelo del vehículo: ")
        gestor_alquiler.agregar_vehiculo(nombre_vehiculo, modelo)
    elif eleccion == '2':
        nombre_vehiculo = input("Nombre del vehículo a eliminar: ")
        gestor_alquiler.eliminar_vehiculo(nombre_vehiculo)
    elif eleccion == '3':
        gestor_alquiler.mostrar_vehiculos()
    elif eleccion == '4':
        nombre_vehiculo = input("Nombre del vehículo a alquilar: ")
        gestor_alquiler.alquilar_vehiculo(nombre_vehiculo)
    elif eleccion == '5':
        nombre_vehiculo = input("Nombre del vehículo a devolver: ")
        gestor_alquiler.devolver_vehiculo(nombre_vehiculo)
    elif eleccion == '6':
        break
    else:
        print('Elección no válida')
