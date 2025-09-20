import email_client as ServidorCorreo
#import mail as Mensaje
#import user as Usuario
ServidorCorreo = ServidorCorreo.servidorCorreo()

def menu_principal():
    print("Bienvenido al Cliente de Correo Electrónico")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    print("-------------------------")
    opcion = input("Seleccione una opción: ")
    return opcion

def primera_opcion():
    print("Iniciar sesión")
    print("-------------------------")
    email = input("Correo electrónico: ")
    password = input("Contraseña: ")
    print("-------------------------")
    usuario = ServidorCorreo.iniciar_sesion(email, password)
    if usuario == False:
        print("Error de inicio de sesión. Verifique sus datos.")
        print("-------------------------")
    else:
        print(f"Bienvenido, {usuario.nombre_completo}!")
        print("-------------------------")
        #return bandeja_entrada()
        # Más adelante acá se conectaría el menú de Carpeta y Mensajes

def segunda_opcion():
    print("Registrarse")
    print("-------------------------")
    nuevo_nombre = input("Ingrese su nombre: ")
    nuevo_apellido = input("Ingrese su apellido: ")
    nuevo_correo = input("Ingrese su correo electrónico: ")
    nueva_contrasenia = input("Ingrese su contraseña: ")
    print("-------------------------")
    nuevo_usuario = ServidorCorreo.registrarse(nuevo_nombre, nuevo_apellido, nuevo_correo, nueva_contrasenia)
    if nuevo_usuario == False:
        print("Error al registrarse. Intente nuevamente.")
        print("-------------------------")
    else:
        print("Registro exitoso. Iniciando sesión...")
        print("-------------------------")
        ServidorCorreo.iniciar_sesion(nuevo_correo, nueva_contrasenia)
        print(f"Bienvenido, {nuevo_usuario.nombre_completo}!")
        print("-------------------------")
        #return bandeja_entrada()
        # Más adelante acá se conectaría el menú de Carpeta y Mensajes

def bandeja_entrada():
    print("Bandeja de Entrada")
    print("-------------------------")
    #funciones de Carpeta y Mensajes
    input("Presione Enter para regresar al menú principal.")
    
def main():
    while True:
        opcion = menu_principal()
        if opcion == "1":
            primera_opcion()
        elif opcion == "2":
            segunda_opcion()
        elif opcion == "3":
            print("Saliendo...")
            print("-------------------------")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            print("-------------------------")

if __name__ == "__main__":
    main()