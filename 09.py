class BibliotecaPersonal:
    def __init__(self):
        self.libros = {}
        self.id_counter = 1

    def agregar_libro(self, titulo, autor, salario):
        libro = {"titulo": titulo, "autor": autor, "salario": salario}
        self.libros[self.id_counter] = libro
        self.id_counter += 1

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            for libro_id, detalles_libro in self.libros.items():
                print(f"ID: {libro_id}, Título: {detalles_libro['titulo']}, Autor: {detalles_libro['autor']}, Salario: {detalles_libro['salario']}")

    def buscar_libro(self, id_libro):
        return self.libros.get(id_libro)

    def eliminar_libro(self, id_libro):
        if id_libro in self.libros:
            libro_eliminado = self.libros.pop(id_libro)
            print(f"Libro '{libro_eliminado['titulo']}' eliminado.")
        else:
            print("Libro no encontrado.")

biblioteca = BibliotecaPersonal()

while True:


    eleccion = input("""Menú de opciones - Biblioteca:
                     1) Agregar Libro
                     2) Mostrar Libros
                     3) Buscar Libro
                     4) Eliminar Libreo
                     5) Salir
Eleccion: """)

    if eleccion == '1':
        titulo = input("Título del libro: ")
        autor = input("Autor del libro: ")
        salario = float(input("Salario del libro: "))
        biblioteca.agregar_libro(titulo, autor, salario)
    elif eleccion == '2':
        biblioteca.mostrar_libros()
    elif eleccion == '3':
        id_libro_eliminar = int(input("ID del libro a eliminar: "))
        biblioteca.eliminar_libro(id_libro_eliminar)
    elif eleccion == '4':
        break
    else:
        print('Elección no válida')
