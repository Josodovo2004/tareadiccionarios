class SistemaVotaciones:
    def __init__(self):
        self.votos_candidatos = {}

    def votar(self, nombre_candidato):
        if nombre_candidato in self.votos_candidatos:
            self.votos_candidatos[nombre_candidato] += 1
        else:
            self.votos_candidatos[nombre_candidato] = 1
        print(f"Voto registrado para el candidato '{nombre_candidato}'.")

    def agregar_candidato(self, nombre_candidato):
        if nombre_candidato not in self.votos_candidatos:
            self.votos_candidatos[nombre_candidato] = 0
            print(f"Candidato '{nombre_candidato}' agregado.")
        else:
            print("Este candidato ya existe.")

    def eliminar_candidato(self, nombre_candidato):
        if nombre_candidato in self.votos_candidatos:
            del self.votos_candidatos[nombre_candidato]
            print(f"Candidato '{nombre_candidato}' eliminado.")
        else:
            print("Candidato no encontrado.")

    def mostrar_resultados(self):
        if not self.votos_candidatos:
            print("No hay votos registrados.")
        else:
            print("Resultados de la votación:")
            for candidato, votos in self.votos_candidatos.items():
                print(f"{candidato}: {votos} votos")

sistema_votaciones = SistemaVotaciones()

while True:
    print("\nMenú de opciones - Sistema de Votaciones:")
    print("1) Votar por un Candidato")
    print("2) Agregar Candidato")
    print("3) Eliminar Candidato")
    print("4) Mostrar Resultados")
    print("5) Salir")

    eleccion = input("Elección: ")

    if eleccion == '1':
        nombre_candidato = input("Nombre del candidato: ")
        sistema_votaciones.votar(nombre_candidato)
    elif eleccion == '2':
        nombre_candidato = input("Nombre del nuevo candidato: ")
        sistema_votaciones.agregar_candidato(nombre_candidato)
    elif eleccion == '3':
        nombre_candidato = input("Nombre del candidato a eliminar: ")
        sistema_votaciones.eliminar_candidato(nombre_candidato)
    elif eleccion == '4':
        sistema_votaciones.mostrar_resultados()
    elif eleccion == '5':
        break
    else:
        print('Elección no válida')
