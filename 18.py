class SeguimientoHabitos:
    def __init__(self):
        self.habitos = {}

    def agregar_habito(self, nombre_habito):
        if nombre_habito not in self.habitos:
            self.habitos[nombre_habito] = {}
            print(f"Hábito '{nombre_habito}' agregado.")
        else:
            print("Este hábito ya existe.")

    def eliminar_habito(self, nombre_habito):
        if nombre_habito in self.habitos:
            del self.habitos[nombre_habito]
            print(f"Hábito '{nombre_habito}' eliminado.")
        else:
            print("Hábito no encontrado.")

    def agregar_fecha_habito(self, nombre_habito, fecha, cumplido=True):
        if nombre_habito in self.habitos:
            self.habitos[nombre_habito][fecha] = cumplido
            print(f"Registro de hábito para '{nombre_habito}' en la fecha {fecha}.")
        else:
            print("Hábito no encontrado.")

    def mostrar_habitos(self):
        if not self.habitos:
            print("No hay hábitos registrados.")
        else:
            print("Hábitos registrados:")
            for habito, registros in self.habitos.items():
                print(f"{habito}: {registros}")

seguimiento_habitos = SeguimientoHabitos()

while True:
    print("\nMenú de opciones - Seguimiento de Hábitos:")
    print("1) Agregar Hábito")
    print("2) Eliminar Hábito")
    print("3) Agregar Fecha a Hábito")
    print("4) Mostrar Hábitos")
    print("5) Salir")

    eleccion = input("Elección: ")

    if eleccion == '1':
        nombre_habito = input("Nombre del hábito: ")
        seguimiento_habitos.agregar_habito(nombre_habito)
    elif eleccion == '2':
        nombre_habito = input("Nombre del hábito a eliminar: ")
        seguimiento_habitos.eliminar_habito(nombre_habito)
    elif eleccion == '3':
        nombre_habito = input("Nombre del hábito: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        cumplido = input("¿Se cumplió el hábito? (Sí/No): ").lower() == 'sí'
        seguimiento_habitos.agregar_fecha_habito(nombre_habito, fecha, cumplido)
    elif eleccion == '4':
        seguimiento_habitos.mostrar_habitos()
    elif eleccion == '5':
        break
    else:
        print('Elección no válida')
