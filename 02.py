class ContadorPalabras():
    def __init__(self) -> None:
        self.palabras = {}

    def insertar_palabras(self):
        palabra = input('Palabra a agregar: ')

        if palabra in self.palabras:
            self.palabras[palabra] += 1
        else:
            self.palabras[palabra] = 1

contador = ContadorPalabras()

while True:
    eleccion = input('''Opciones:
                     1) Hacer insercion
                     2) Salir
eleccion: ''')
    if eleccion == '1':
        contador.insertar_palabras()
    elif eleccion == '2':
        break
    else:
        print('Opcion no valida')