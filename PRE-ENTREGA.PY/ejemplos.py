usuarios = {"Priscila" : "1234"}

def Registro():
    nombre_usuario = input("Por favor, ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    usuarios[nombre_usuario] = password
    print("¡Se ha registrado con éxito!")

def Iniciar_Sesion(nombre_usuario, password):
    while nombre_usuario not in usuarios or usuarios[nombre_usuario] != password:
        print("Usuario o contraseña incorrecto, por favor ingrese nuevamente sus datos")
        nombre_usuario = input("Ingrese nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
    print("¡Bienvenido!")
    return True

def Ver_Usuarios():
    print(usuarios)

def Inicio():
    opcion = 0
    while opcion != 4:
        print("1. Iniciar Sesión")
        print("2. Registrarme")
        print("3. Ver usuarios")
        print("4. Salir")
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            logueado = Iniciar_Sesion(nombre_usuario, password)
            if not logueado:
                print("Usuario o contraseña incorrectas, intente nuevamente")
            else:
                print("Has iniciado sesión")
                break
        elif opcion == 2:
            Registro()
        elif opcion == 3:
            Ver_Usuarios()
        elif opcion == 4:
            print("¡Hasta luego!")
            break

Inicio()