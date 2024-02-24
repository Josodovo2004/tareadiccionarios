class Almacen():
    def __init__(self) -> None:
        self.productos = {}
    def registrar_producto(self):
        producto = input('Nombre del producto: ')
        cantidad = int(input('stock del producto: '))

        self.productos[producto] = cantidad
    def actualizar_producto(self):
        while True:
            productoAcualizar = input('Que producto quiere actualizar:')
            try:
                self.productos[productoAcualizar] = input('Cual es el nuevo stock')
                break
            except:
                print('Producto no valido')

    def eliminar_producto(self):
        while True:
            productoEliminar = input('Que producto quiere actualizar:')
            try:
                self.productos.pop(productoEliminar)
                break
            except:
                print('Producto no valido')

almacen = Almacen()

while True:
    eleccion = input("""Menu de opciones almacen:
          1) Agregar stock producto
          2) Actualizar stock producto
          3) Eliminar stock producto
          4) Salir
eleccion: """)
    
    if eleccion == '1':
        almacen.registrar_producto()
    elif eleccion == '2':
        almacen.actualizar_producto()
    elif eleccion == '3':
        almacen.eliminar_producto()
    elif eleccion == '4':
        break
    else:
        print('Eleccion no valida')