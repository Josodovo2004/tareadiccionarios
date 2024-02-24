class GestorCalificaciones:
    def __init__(self):
        self.calificaciones = {}

    def agregar_calificacion(self, estudiante, asignatura, calificacion):
        if estudiante not in self.calificaciones:
            self.calificaciones[estudiante] = {}
        self.calificaciones[estudiante][asignatura] = calificacion

    def obtener_calificacion(self, estudiante, asignatura):
        if estudiante in self.calificaciones and asignatura in self.calificaciones[estudiante]:
            return self.calificaciones[estudiante][asignatura]
        else:
            return f"No se encontró la calificación para {asignatura} del estudiante {estudiante}"

    def mostrar_calificaciones(self):
        for estudiante, asignaturas in self.calificaciones.items():
            print(f"Estudiante: {estudiante}")
            for asignatura, calificacion in asignaturas.items():
                print(f"  {asignatura}: {calificacion}")
                
gestor_calificaciones = GestorCalificaciones()

while True:
    eleccion = input("""Menú de opciones - Gestión de Calificaciones:
                     1) Agregar Calificación
                     2) Obtener Calificación
                     3) Mostrar Todas las Calificaciones
                     4) Salir
Eleccion: """)

    if eleccion == '1':
        estudiante = input("Nombre del estudiante: ")
        asignatura = input("Nombre de la asignatura: ")
        calificacion = float(input("Calificación: "))
        gestor_calificaciones.agregar_calificacion(estudiante, asignatura, calificacion)
    elif eleccion == '2':
        estudiante = input("Nombre del estudiante: ")
        asignatura = input("Nombre de la asignatura: ")
        calificacion_obtenida = gestor_calificaciones.obtener_calificacion(estudiante, asignatura)
        print(f"Calificación: {calificacion_obtenida}")
    elif eleccion == '3':
        gestor_calificaciones.mostrar_calificaciones()
    elif eleccion == '4':
        break
    else:
        print('Elección no válida')
