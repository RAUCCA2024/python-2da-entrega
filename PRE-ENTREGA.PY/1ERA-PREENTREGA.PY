# Función para almacenar la información (usuario y clave)
def almacenar_informacion(usuarios, usuario, clave):
    if usuario in usuarios:
        print("El usuario ya existe. Por favor, ingresa un usuario diferente.")
    else:
        usuarios[usuario] = clave
        print("Usuario y clave almacenados exitosamente.")

# Función para mostrar la información almacenada (usuarios y claves)
def mostrar_informacion(usuarios):
    if usuarios:
        print("Usuarios y clave almacenados:")
        for usuario, clave in usuarios.items():
            print("Usuario:", usuario, "| Clave:", clave)
    else:
        print("Aún no hay usuarios registrados.")

# Función para iniciar sesión
def iniciar_sesion(usuarios):
    intentos = 3  # Número máximo de intentos de contraseña
    while intentos > 0:
        usuario = input("Ingresa tu nombre de usuario: ")
        clave = input("Ingresa tu clave: ")
        if usuario in usuarios and usuarios[usuario] == clave:
            print("¡Inicio de sesión exitoso!")
            return
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Nombre de usuario o clave incorrectos. Te quedan {intentos} intentos.")
            else:
                print("Número máximo de intentos alcanzado. Sesión terminada.")
                return

# Lógica principal del programa
def main():
    usuarios = {}

    # Datos iniciales
    usuario_inicial = "usuario"
    clave_inicial = "clave"
    almacenar_informacion(usuarios, usuario_inicial, clave_inicial)

    while True:
        print("\n1. Registrar usuario y clave")
        print("2. Mostrar usuarios y claves")
        print("3. Iniciar sesión")
        print("4. Cerrar Sesión")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario = input("Ingresa el nombre de usuario: ")
            clave = input("Ingresa la clave: ")
            almacenar_informacion(usuarios, usuario, clave)
        elif opcion == "2":
            mostrar_informacion(usuarios)
        elif opcion == "3":
            iniciar_sesion(usuarios)
        elif opcion == "4":
            print("Sesión finalizada")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()