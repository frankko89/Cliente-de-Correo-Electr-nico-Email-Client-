import email_client as ServidorCorreo
from carpeta import Carpeta
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

def inicio():
    print("INICIO")
    print("1. Enviar correo")
    print("2. Revisar bandeja de entrada")
    print("3. Ver bandeja de salida")
    print("4. Buscar mensajes por asunto o usuario")
    print("5. Cerrar sesión")
    print("-------------------------")
    seleccion = input("Seleccione una opción: ")
    return seleccion

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
        return usuario

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
        return nuevo_usuario

def bandeja_entrada():
    #llamaría a la funcion organizar_mensajes() de la clase ServidorCorreo 
    #permitiría seleccionar y leer mensajes con un remitente distinto al usuario actual
    print("BANDEJA DE ENTRADA")

def bandeja_salida():
    #llamaría a la funcion organizar_mensajes() de la clase ServidorCorreo 
    #permitiría seleccionar y leer mensajes enviados por el usuario actual
    print("BANDEJA DE SALIDA")
    
def main():
    sesion_iniciada = False
    
    while True:
        if not sesion_iniciada:
            opcion = menu_principal()
            if opcion == "1":
                usuario = primera_opcion()
                if usuario:
                    sesion_iniciada = True
            elif opcion == "2":
                usuario = segunda_opcion()
                if usuario:
                    sesion_iniciada = True
            elif opcion == "3":
                print("Saliendo...")
                print("-------------------------")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                print("-------------------------")
            
        else:
            seleccion = inicio()
            if seleccion == "1":
                print("Enviar correo")
                print("-------------------------")
                remitente_mail = usuario.correo
                destinatario_mail = input("Ingrese el correo electrónico del destinatario: ")
                asunto = input("Ingrese el asunto del correo: ")
                cuerpo = input("Ingrese el cuerpo del correo: ")
                ServidorCorreo.enviar_mensaje(remitente_mail, destinatario_mail, asunto, cuerpo)

            elif seleccion == "2":
                bandeja_entrada()

            elif seleccion == "3":
                bandeja_salida()

            elif seleccion == "4":
                print("Buscar mensajes")
                criterio = input("Ingrese el asunto o usuario para buscar: ")
                ServidorCorreo.buscar_mensajes(criterio)

            elif seleccion == "5":
                print("Cerrando sesión...")
                print("-------------------------")
                sesion_iniciada = False
            
            else:
                print("Opción no válida. Intente de nuevo.")
                print("-------------------------")

if __name__ == "__main__":
    main()