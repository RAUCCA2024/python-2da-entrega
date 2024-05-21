from MI_PRIMER_PAQUETE.cliente import Cliente, Producto

def mostrar_menu():
    print("=== MENÚ ===")
    print("1. Mostrar detalles del cliente")
    print("2. Elegir y realizar compra de un producto")
    print("3. Recargar saldo del cliente")
    print("4. Elegir medio de pago")
    print("5. Salir")

def mostrar_detalles_cliente(cliente):
    print("\nDetalles del cliente:")
    print(cliente)

def realizar_compra_producto(cliente, productos):
    try:
        producto_seleccionado = cliente.elegir_producto(productos)
        if producto_seleccionado:
            cliente.realizar_compra_producto(producto_seleccionado)
    except ValueError:
        print("Error: Selección inválida.")

def recargar_saldo(cliente):
    try:
        monto = float(input("Ingrese el monto a recargar: "))
        cliente.recargar_saldo(monto)
    except ValueError:
        print("Error: Ingrese un monto válido.")

def elegir_medio_de_pago(cliente):
    try:
        medio_de_pago = cliente.elegir_medio_de_pago()
        if medio_de_pago:
            print(f"\nCompra realizada utilizando {medio_de_pago}.")
    except ValueError:
        print("Error: Selección inválida.")

def main():
    # Crear cliente1
    cliente1 = Cliente("Maria", "Maria2024@example.com", "Calle pavon 3731 piso 12 D", 1133457290, 100000)

    # Crear lista de productos
    productos_disponibles = [
        Producto("Computadora portátil", 80000),
        Producto("Smartphone", 50000),
        Producto("Tablet", 30000)
    ]

    while True:
        mostrar_menu()  # Mostrar el menú
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_detalles_cliente(cliente1)
        elif opcion == "2":
            realizar_compra_producto(cliente1, productos_disponibles)
        elif opcion == "3":
            recargar_saldo(cliente1)
        elif opcion == "4":
            elegir_medio_de_pago(cliente1)
        elif opcion == "5":
            print("Saliendo")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
    
