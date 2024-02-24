class GestionHotel():
    def __init__(self) -> None:
        self.idCounter = 1
        self.habitaciones = {}
    
    def agregar_habitacion(self):
        self.habitaciones[self.idCounter] = 'libre'
        self.idCounter += 1
    def lista_habitaciones(self):
        for numero, estado in self.habitaciones.items:
            print(f'{numero} | {estado}')
    def actualizar_estado(self):
        numero = int(input('Habitacion de la que quiere cambiar su estado: '))
        if self.habitaciones[numero] == 'libre':
            self.habitaciones[numero] = 'ocupado'
        else:
            self.habitaciones[numero] = 'libre'

hotel = GestionHotel()
    
while True:
    eleccion =  input("""Menú de opciones - Empleados:
                     1) Agregar Habitacion
                     2) Lista Habitaciones
                     3) Actualizar Estado
                     4) Salir
Eleccion: """)
    if eleccion == '1':
        hotel.agregar_habitacion()
    elif eleccion == '2':
        hotel.lista_habitaciones()
    elif eleccion == '3':
        hotel.actualizar_estado()
    elif eleccion == '4':
        break
    else:
        print('Elección no válida')
