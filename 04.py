class Inventario():
    def __init__(self) -> None:
        self.idCounter = 1
        self.listaProductos = {}
    def registro_producto(self):
        nombre = input('Nombre producto: ')
        cantidad = input('Cantidad Producto: ')
        precio = int(input('Precio: '))
        self.listaProductos[self.idCounter] = [nombre, cantidad, precio]
        self.idCounter += 1
    def actualizar_producto(self):
        productoAcualizar = input('Nombre del alumno a actualizar:')
        for key in self.listaProductos.keys:
            if productoAcualizar in self.listaAlumnos[key]:
                nombre = input('Nombre producto: ')
                cantidad = input('Cantidad: ')
                precio = int(input('Precio: '))
                self.listaProductos[self.idCounter] = [nombre, cantidad, precio]
                break
    def lista_productos(self):
        for key in self.listaProductos.keys:
            print(self.listaProductos[key])
    def eliminar_producto(self):
        productoEliminar = input('Producto a eliminar')
        for key in self.listaProductos.keys:
            if productoEliminar in self.listaProductos[key]:
                self.listaProductos.pop(key)
                break
inventario = Inventario()

while True:
    eleccion = input("""Menu de opciones almacen:
          1) Registrar Producto
          2) Actualizar Producto
          3) Lista de Productos
          4) Eliminar Producto
          5) Salir
eleccion: """)
    
    if eleccion == '1':
        inventario.registro_producto()
    elif eleccion == '2':
        inventario.actualizar_producto()
    elif eleccion == '3':
        inventario.lista_productos()
    elif eleccion == '4':
        inventario.eliminar_producto()
    elif eleccion == '5':
        break
    else:
        print('Eleccion no valida')