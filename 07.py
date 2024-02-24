class ConversorUnidades:
    def __init__(self):
        self.conversiones = {}

    def agregar_conversion(self, unidad_origen, unidad_destino, factor_conversion):
        key = f"{unidad_origen}_{unidad_destino}"
        self.conversiones[key] = factor_conversion

    def realizar_conversion(self, valor, unidad_origen, unidad_destino):
        key = f"{unidad_origen}_{unidad_destino}"
        if key in self.conversiones:
            factor_conversion = self.conversiones[key]
            resultado = valor * factor_conversion
            return resultado
        else:
            return f"No se encontró una conversión de {unidad_origen} a {unidad_destino}"


conversor = ConversorUnidades()

while True:
    eleccion = input("""Menú de opciones - Conversor de Unidades:
          1) Agregar Conversión
          2) Realizar Conversión
          3) Salir
Eleccion: """)

    if eleccion == '1':
        unidad_origen = input("Unidad de origen: ")
        unidad_destino = input("Unidad de destino: ")
        factor_conversion = float(input("Factor de conversión: "))
        conversor.agregar_conversion(unidad_origen, unidad_destino, factor_conversion)
    elif eleccion == '2':
        valor = float(input("Valor a convertir: "))
        unidad_origen = input("Unidad de origen: ")
        unidad_destino = input("Unidad de destino: ")
        resultado = conversor.realizar_conversion(valor, unidad_origen, unidad_destino)
        print(f"El resultado de la conversión es: {resultado}")
    elif eleccion == '3':
        break
    else:
        print('Elección no válida')
