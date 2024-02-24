class GestionEventos:
    def __init__(self):
        self.eventos = {}

    def agregar_evento(self, nombre_evento, fecha, hora):
        if nombre_evento not in self.eventos:
            self.eventos[nombre_evento] = {'fecha': fecha, 'hora': hora, 'participantes': []}
            print(f"Evento '{nombre_evento}' agregado.")
        else:
            print("Este evento ya está registrado.")

    def eliminar_evento(self, nombre_evento):
        if nombre_evento in self.eventos:
            del self.eventos[nombre_evento]
            print(f"Evento '{nombre_evento}' eliminado.")
        else:
            print("Evento no encontrado.")

    def mostrar_eventos(self):
        if not self.eventos:
            print("No hay eventos registrados.")
        else:
            print("Eventos registrados:")
            for evento, info in self.eventos.items():
                print(f"{evento} - Fecha: {info['fecha']}, Hora: {info['hora']}, Participantes: {info['participantes']}")

    def agregar_participante(self, nombre_evento, participante):
        if nombre_evento in self.eventos:
            self.eventos[nombre_evento]['participantes'].append(participante)
            print(f"Participante '{participante}' agregado al evento '{nombre_evento}'.")
        else:
            print("Evento no encontrado.")

# Ejemplo de uso con bucle while y menú de opciones
gestor_eventos = GestionEventos()

while True:
    print("\nMenú de opciones - Gestión de Eventos:")
    print("1) Agregar Evento")
    print("2) Eliminar Evento")
    print("3) Mostrar Eventos")
    print("4) Agregar Participante a Evento")
    print("5) Salir")

    eleccion = input("Elección: ")

    if eleccion == '1':
        nombre_evento = input("Nombre del evento: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        hora = input("Hora (HH:MM): ")
        gestor_eventos.agregar_evento(nombre_evento, fecha, hora)
    elif eleccion == '2':
        nombre_evento = input("Nombre del evento a eliminar: ")
        gestor_eventos.eliminar_evento(nombre_evento)
    elif eleccion == '3':
        gestor_eventos.mostrar_eventos()
    elif eleccion == '4':
        nombre_evento = input("Nombre del evento: ")
        participante = input("Nombre del participante: ")
        gestor_eventos.agregar_participante(nombre_evento, participante)
    elif eleccion == '5':
        break
    else:
        print('Elección no válida')
