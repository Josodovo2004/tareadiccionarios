class AnalisisRedesSociales:
    def __init__(self):
        self.usuarios = {}

    def agregar_usuario(self, nombre_usuario, seguidores):
        self.usuarios[nombre_usuario] = seguidores

    def obtener_seguidores(self, nombre_usuario):
        return self.usuarios.get(nombre_usuario)

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            for usuario, seguidores in self.usuarios.items():
                print(f"Usuario: {usuario}, Seguidores: {seguidores}")

    def eliminar_usuario(self, nombre_usuario):
        if nombre_usuario in self.usuarios:
            del self.usuarios[nombre_usuario]
            print(f"Usuario '{nombre_usuario}' eliminado.")
        else:
            print("Usuario no encontrado.")

analisis_redes_sociales = AnalisisRedesSociales()

while True:
    print("\nMenú de opciones - Análisis de Redes Sociales:")
    print("1) Agregar Usuario")
    print("2) Obtener Seguidores")
    print("3) Mostrar Usuarios")
    print("4) Eliminar Usuario")
    print("5) Salir")

    eleccion = input("Elección: ")

    if eleccion == '1':
        nombre_usuario = input("Nombre del usuario: ")
        seguidores = int(input("Número de seguidores: "))
        analisis_redes_sociales.agregar_usuario(nombre_usuario, seguidores)
    elif eleccion == '2':
        nombre_usuario = input("Nombre del usuario: ")
        seguidores = analisis_redes_sociales.obtener_seguidores(nombre_usuario)
        if seguidores is not None:
            print(f"Seguidores de {nombre_usuario}: {seguidores}")
        else:
            print("Usuario no encontrado.")
    elif eleccion == '3':
        analisis_redes_sociales.mostrar_usuarios()
    elif eleccion == '4':
        nombre_usuario = input("Nombre del usuario a eliminar: ")
        analisis_redes_sociales.eliminar_usuario(nombre_usuario)
    elif eleccion == '5':
        break
    else:
        print('Elección no válida')
