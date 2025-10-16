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

def inicio():
    print("INICIO")
    print("1. Enviar correo")
    print("2. Revisar bandeja de entrada")
    print("3. Ver bandeja de salida")
    print("4. Buscar mensajes por asunto o usuario")
    print("5. Ver estructuras de las carpetas") #agregamos una nueva seccion para poder ver la estructura del arbol
    print("6. Mover un mensaje a una carpeta.") #nueva función para mover mensajes de una carpeta a otra
    print("7. Cerrar sesion")
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
    
def mostrar_carpetas(actual, nivel = 0):
    if actual is not None:
        indentacion = " " * nivel
        #aca lo que se haces es que se muestre como seria una carpeta dentro de otra
        print(f"{indentacion}|-- {actual.nombre} ({len(actual.mensajes)}) mensajes")
        #y aca lo que se va a ver es una forma visual la estructura y lo que haces es que accede a cada carpeta creada y a la lista de o de los mensajes que tenga
        mostrar_carpetas(actual.hijo, nivel + 1)
        
        mostrar_carpetas(actual.siguiente_hermano, nivel + 2)
        #y por ultimo en estas ultimas 2 lineas de codigo lo que hacemos es llamar a los getter que definimos en la clase folder
        #para poder ver que tiene cada adentro cada rama y si tiene algo se muestra y si no salta a la siguiente 

def bandeja_entrada(usuario_logueado):
    print("BANDEJA DE ENTRADA")
    mostrar_lista_mensajes(usuario_logueado.bandeja_entrada.mensajes)

def bandeja_salida(usuario_logueado):
    print("BANDEJA DE SALIDA")
    mostrar_lista_mensajes(usuario_logueado.bandeja_salida.mensajes)

def mostrar_lista_mensajes(lista_de_mensajes):
    if not lista_de_mensajes:
        print("No se encontraron mensajes.")
        print("-------------------------")
        return

    for i, m in enumerate(lista_de_mensajes):
        print(f"{i+1}. De: {m.remitente.nombre_completo} | Asunto: {m.asunto} | Fecha: {m.fecha}")
    print("-------------------------")

def mover_mensaje(usuario):
    #logica para que el usuario mueva mensaje entre dos carpetas existentes en su buzón.
    print("MOVER MENSAJE")
    nombre_origen = input("Ingrese el nombre de la carpeta origen (ej:bandeja de entrada): ")
    carpeta_origen = usuario.buscar_carpeta(usuario.carpeta_raiz, nombre_origen)
    
    if not carpeta_origen:
        print(f"Error: Carpeta '{nombre_origen}' no encontrada. Intente de nuevo.")
        return
    
    mensajes_en_origen = carpeta_origen.mensajes
    if not mensajes_en_origen:
        print(f"La carpeta '{nombre_origen}' está vacía. No hay mensajes para mover.")
        return
    
    print(f"\nMensajes en '{nombre_origen}':")
    mostrar_lista_mensajes(mensajes_en_origen)
    
    try:
        seleccion_mensaje = int(input("Ingrese el NÚMERO del mensaje a mover: ")) - 1
        if not (0 <= seleccion_mensaje < len(mensajes_en_origen)):
            print("Selección inválida.")
            return
        
        mensaje_a_mover = mensajes_en_origen[seleccion_mensaje]
        
    except ValueError:
        print("Entrada no válida.")
        return
    
    nombre_destino = input("Ingrese el nombre de la carpeta destino (ej: bandeja de salida): ")
    
    usuario.mover_mensaje(mensaje_a_mover, nombre_origen, nombre_destino)
    print("-------------------------")
    
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
                bandeja_entrada(usuario)

            elif seleccion == "3":
                bandeja_salida(usuario)

            elif seleccion == "4":
                print("Buscar mensajes")
                criterio = input("Ingrese el asunto o usuario para buscar: ")
                resultados_entrada = usuario.bandeja_entrada.buscar_mensajes(criterio)
                resultados_salida = usuario.bandeja_salida.buscar_mensajes(criterio)
                resultados_totales = resultados_entrada + resultados_salida
                
                if not resultados_totales:
                    print("No se encontraron mensajes que coincidan con la búsqueda.")
                else:
                    print(f"Se encontraron {len(resultados_totales)} resultados:")
                    mostrar_lista_mensajes(resultados_totales)
                    
            elif seleccion == "5":
                print("\nEstructura de Carpetas: ")
            
                mostrar_carpetas(usuario.carpeta_raiz)
                #aca lo que hacemos es que cuando se ingrese la opcion 5 llame a la funcion mostrar_carpeta 
                print("-------------------------")
            
            elif seleccion == "6":
                mover_mensaje(usuario)
            
            elif seleccion == "7":
                print("Cerrando sesión...")
                print("-------------------------")
                sesion_iniciada = False
            
            else:
                print("Opción no válida. Intente de nuevo.")
                print("-------------------------")

if __name__ == "__main__":
    main()