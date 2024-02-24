class RegistroEstudiantes():
    def __init__(self) -> None:
        self.idCounter = 1
        self.listaAlumnos = {}
    def inscribir_alumno(self):
        nombre = input('Nombre almuno: ')
        edad = input('Edad Alumno: ')
        nota = int(input('Nota: '))
        self.listaAlumnos[self.idCounter] = [nombre, edad, nota]
        self.idCounter += 1
    def actualizar_alumno(self):
        alumnoAcualizar = input('Nombre del alumno a actualizar:')
        for key in self.listaAlumnos.keys:
            if alumnoAcualizar in self.listaAlumnos[key]:
                nombre = input('Nombre almuno: ')
                edad = input('Edad Alumno: ')
                nota = int(input('Nota: '))
                self.listaAlumnos[self.idCounter] = [nombre, edad, nota]
                break
    def lista_alumnos(self):
        for key in self.listaAlumnos.keys:
            print(self.listaAlumnos[key])
    def eliminar_alumno(self):
        alumnoEliminar = input('Alumno a eliminar')
        for key in self.listaAlumnos.keys:
            if alumnoEliminar in self.listaAlumnos[key]:
                self.listaAlumnos.pop(key)
                break
registro = RegistroEstudiantes()

while True:
    eleccion = input("""Menu de opciones almacen:
          1) Ingresar Alumno
          2) Actualizar Alumno
          3) Lista de Alumnos
          4) Eliminar Alumno
          5) Salir
eleccion: """)
    
    if eleccion == '1':
        registro.inscribir_alumno()
    elif eleccion == '2':
        registro.actualizar_alumno()
    elif eleccion == '3':
        registro.lista_alumnos()
    elif eleccion == '4':
        registro.eliminar_alumno()
    elif eleccion == '5':
        break
    else:
        print('Eleccion no valida')