class AgendaTelefonica:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self):
        nombre = input('Nombre del contacto: ')
        numero = input('Número de celular: ')

        self.contactos[nombre] = numero

    def modificar_contacto(self):
        while True:
            contacto_modificar = input('¿Qué contacto desea modificar?: ')
            if contacto_modificar in self.contactos:
                nuevo_numero = input('Nuevo número de celular: ')
                self.contactos[contacto_modificar] = nuevo_numero
                break
            else:
                print('Contacto no encontrado')

    def eliminar_contacto(self):
        while True:
            contacto_eliminar = input('¿Qué contacto desea eliminar?: ')
            if contacto_eliminar in self.contactos:
                del self.contactos[contacto_eliminar]
                break
            else:
                print('Contacto no encontrado')

agenda = AgendaTelefonica()

while True:
    eleccion = input("""Menú de opciones - Agenda Telefónica:
          1) Agregar contacto
          2) Modificar contacto
          3) Eliminar contacto
          4) Salir
Eleccion: """)
    
    if eleccion == '1':
        agenda.agregar_contacto()
    elif eleccion == '2':
        agenda.modificar_contacto()
    elif eleccion == '3':
        agenda.eliminar_contacto()
    elif eleccion == '4':
        break
    else:
        print('Elección no válida')
