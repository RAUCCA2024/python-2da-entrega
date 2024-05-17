class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}\nPrecio: {self.precio}"

class Cliente:
    def __init__(self, nombre, correo, direccion, telefono, saldo):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.saldo = saldo

    def realizar_compra(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Compra realizada por un total de ${monto}. Saldo restante: {self.saldo}")
        else:
            print("Saldo insuficiente para realizar la compra.")

    def realizar_compra_producto(self, producto):
        if producto.precio <= self.saldo:
            self.saldo -= producto.precio
            print(f"Compra de {producto.nombre} realizada por un total de ${producto.precio}. Saldo restante: {self.saldo}")
        else:
            print("Saldo insuficiente para realizar la compra del producto.")

    def recargar_saldo(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Saldo recargado por un total de ${monto}. Nuevo saldo: {self.saldo}")
        else:
            print("Debe ingresar un monto válido para recargar.")

    def elegir_producto(self, lista_productos):
        print("\nProductos disponibles:")
        for i, producto in enumerate(lista_productos, start=1):
            print(f"{i}. {producto}")

        seleccion = int(input("Seleccione el número del producto que desea comprar: "))
        if 1 <= seleccion <= len(lista_productos):
            return lista_productos[seleccion - 1]
        else:
            print("Selección no válida.")
            return None

    def elegir_medio_de_pago(self):
        print("\nMedios de pago disponibles:")
        print("1. Tarjeta de crédito")
        print("2. Tarjeta de débito")
        print("3. Transferencia bancaria")

        seleccion = int(input("Seleccione el número del medio de pago que desea utilizar: "))
        if seleccion == 1:
            return "Tarjeta de crédito"
        elif seleccion == 2:
            return "Tarjeta de débito"
        elif seleccion == 3:
            return "Transferencia bancaria"
        else:
            print("Selección no válida.")
            return None

    def __str__(self):
        return f"Cliente: {self.nombre}\nCorreo: {self.correo}\nDirección: {self.direccion}\nTeléfono: {self.telefono}\nSaldo: {self.saldo}"


def main():
    # Se crea el cliente1
    cliente1 = Cliente("Maria", "Maria2024@example.com", "Calle pavon 3731 piso 12 D", 1133457290, 100000)
    print("Detalles del cliente:")
    print(cliente1)

    # Se crea una lista de productos
    productos_disponibles = [
        Producto("Computadora portátil", 80000),
        Producto("Smartphone", 50000),
        Producto("Tablet", 30000)
    ]

    # Aquí se elige y se realiza la compra de un producto
    producto_seleccionado = cliente1.elegir_producto(productos_disponibles)
    if producto_seleccionado:
        cliente1.realizar_compra_producto(producto_seleccionado)

    # Recargar saldo de cliente1
    print("\nRecargando saldo con 300:")
    cliente1.recargar_saldo(300)

    # Se elige el medio de pago
    medio_de_pago = cliente1.elegir_medio_de_pago()
    if medio_de_pago:
        print(f"\nCompra realizada utilizando {medio_de_pago}.")

    # Mostrar detalles actualizados de cliente1
    print("\nDetalles del cliente actualizados:")
    print(cliente1)

if __name__ == "__main__":
    main()