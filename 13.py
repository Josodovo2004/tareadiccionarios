class ConfiguracionApp:
    def __init__(self):
        self.configuracion = {
            'modo': 'Normal',
            'escala': 'Mediana',
            'eficiencia': 'Alta'
        }

    def modificar_configuracion(self, ajuste, valor):
        if ajuste in self.configuracion:
            self.configuracion[ajuste] = valor
            print(f"Ajuste '{ajuste}' modificado correctamente.")
        else:
            print("Ajuste no válido.")

    def obtener_configuracion(self, ajuste):
        return self.configuracion.get(ajuste)

    def mostrar_configuracion(self):
        for ajuste, valor in self.configuracion.items():
            print(f"{ajuste}: {valor}")

configuracion_app = ConfiguracionApp()

while True:
    print("\nMenú de opciones - Configuración de la Aplicación:")
    print("1) Modificar Configuración")
    print("2) Obtener Configuración")
    print("3) Mostrar Configuración")
    print("4) Salir")

    eleccion = input("Elección: ")

    if eleccion == '1':
        ajuste = input("Nombre del ajuste: ")
        valor = input("Nuevo valor: ")
        configuracion_app.modificar_configuracion(ajuste, valor)
    elif eleccion == '2':
        ajuste = input("Nombre del ajuste: ")
        valor = configuracion_app.obtener_configuracion(ajuste)
        if valor is not None:
            print(f"Valor de {ajuste}: {valor}")
        else:
            print("Ajuste no encontrado.")
    elif eleccion == '3':
        configuracion_app.mostrar_configuracion()
    elif eleccion == '4':
        break
    else:
        print('Elección no válida')
