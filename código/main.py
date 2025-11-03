import email_client as ServidorCorreo
from folder import Carpeta
#import mail as Mensaje
#import user as Usuario

ServidorCorreo = ServidorCorreo.servidorCorreo()

def menu_principal(hay_usuarios):
    print("Bienvenido al Cliente de Correo Electrónico")
    opciones = {}
    
    if hay_usuarios:    
        print("(1). Iniciar sesión")
        print("(2). Registrarse")
        print("(3). Salir")
        opciones = {"1": "login", "2": "register", "3": "exit"}
    
    else:
        print("(1). Registrarse")
        print("(2). Salir")
        opciones = {"1": "register", "2": "exit"}
        
    print("-------------------------")
    seleccion = input("Seleccione una opción: ")
    #devuelve la acción correspondiente al número, o "inválida" si no existe dicha opción.
    return opciones.get(seleccion, "invalida")

def inicio():
    print("INICIO")
    print("(1). Gestionar mensajes")
    print("(2). Gestionar carpetas")
    print("(3). Crear filtro automatico") #creamos la opcion de crear los filtros 
    print("(4). Buscador")
    print("(5). Cerrar sesion")
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
    nuevo_nombre = input("Ingrese su nombre: ").title()
    nuevo_apellido = input("Ingrese su apellido: ").title()
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
        mostrar_carpetas(actual.siguiente_hermano, nivel)
        #y por ultimo en estas ultimas 2 lineas de codigo lo que hacemos es llamar a los getter que definimos en la clase folder
        #para poder ver que tiene cada adentro cada rama y si tiene algo se muestra y si no salta a la siguiente 

def menu_gestionar_mensajes(usuario):
    while True:
        print("GESTIÓN DE MENSAJES")
        print("(1). Enviar correo")
        print("(2). Revisar bandeja de entrada")
        print("(3). Revisar bandeja de salida")
        print("(4). Ver mensajes importantes")
        print("(5). Mover un mensaje a una carpeta")
        print("(6). Volver atrás")
        print("-------------------------")
        seleccion = input("Seleccione una opción: ")

        if seleccion == "1":
            print("Enviar correo")
            print("-------------------------")
            remitente_mail = usuario.correo
            destinatario_mail = input("Ingrese el correo electrónico del destinatario: ")
            asunto = input("Ingrese el asunto del correo: ")
            cuerpo = input("Ingrese el cuerpo del correo: ")
            ServidorCorreo.enviar_mensaje(remitente_mail, destinatario_mail, asunto, cuerpo)
        
        elif seleccion == "2":
            menu_revisar_bandeja(usuario, usuario.bandeja_entrada, "Bandeja de Entrada")
        
        elif seleccion == "3":
            menu_revisar_bandeja(usuario, usuario.bandeja_salida, "Bandeja de Salida")
        
        elif seleccion == "4":
            print("Accediendo a la Cola de Prioridades...")
            carpeta_virtual_importantes = Carpeta("Mensajes Importantes")
            
            for msg in usuario.importantes:
                carpeta_virtual_importantes.agregar_mensajes(msg)
            
            menu_revisar_bandeja(usuario, carpeta_virtual_importantes, "Mensajes Importantes")
        
        elif seleccion == "5":
            mover_mensaje(usuario) 
        
        elif seleccion == "6":
            break 
        
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_gestionar_carpetas(usuario):
    while True:
        print("GESTIÓN DE CARPETAS")
        print("(1). Ver estructuras de las carpetas")
        print("(2). Crear carpeta")
        print("(3). Revisar mensajes de una carpeta") 
        print("(4). Volver atrás") 
        print("-------------------------")
        seleccion = input("Seleccione una opción: ")

        if seleccion == "1":
            print("\n--Estructura de Carpetas--")
            mostrar_carpetas(usuario.carpeta_raiz)
            print("-------------------------")
        
        elif seleccion == "2":
            print("\n--Nueva Carpeta--")
            nombre = input("Ingrese el nombre de su nueva carpeta: ")
            usuario.carpeta_raiz.agregar_subcarpeta(nombre)

        elif seleccion == "3":
            print("\n--Revisar Carpeta--")
            nombre_carpeta = input("Ingrese el nombre de la carpeta a revisar: ")
            carpeta_encontrada = usuario.buscar_carpeta(usuario.carpeta_raiz, nombre_carpeta)
            if carpeta_encontrada:
                menu_revisar_bandeja(usuario, carpeta_encontrada, carpeta_encontrada.nombre)
            else:
                print(f"Error: No se encontró la carpeta llamada '{nombre_carpeta}'.")
                print("-------------------------")
        
        elif seleccion == "4": 
            break 
        
        else:
            print("Opción no válida. Intente de nuevo.")

def mostrar_lista_mensajes(lista_de_mensajes):
    if not lista_de_mensajes:
        print("No se encontraron mensajes.")
        print("-------------------------")
        return
    
    for i, m in enumerate(lista_de_mensajes):
        estado = "[NUEVO] " if not m.leido else " " * 8
        print(f"{i+1}. {estado}De: {m.remitente.nombre_completo} | Asunto: {m.asunto} | Fecha: {m.fecha}")
    print("-------------------------")

def menu_revisar_bandeja(usuario, carpeta, nombre_carpeta):
    while True:
        print(f"\nREVISANDO: {nombre_carpeta.upper()}")
        lista_de_mensajes = carpeta.mensajes
        
        if not lista_de_mensajes:
            print("No se encontraron mensajes.")
            print("-------------------------")
            break # si no hay mensajes, vuelve al menú anterior
        
        # muestra la lista de mensajes
        mostrar_lista_mensajes(lista_de_mensajes)
        print("(1). Seleccionar mensaje (por número)")
        print("(2). Volver atrás")
        print("-------------------------")
        seleccion = input("Seleccione una opción: ")

        if seleccion == "1":
            try:
                indice = int(input("Ingrese el NÚMERO del mensaje: ")) - 1
                if 0 <= indice < len(lista_de_mensajes):
                    mensaje_seleccionado = lista_de_mensajes[indice]
                    menu_opciones_mensaje(usuario, mensaje_seleccionado)
                else:
                    print("Número de mensaje fuera de rango.")
            except ValueError:
                print("Entrada no válida. Debe ser un número.")
        
        elif seleccion == "2":
            break 
        
        else:
            print("Opción no válida.")

def menu_opciones_mensaje(usuario, mensaje):
    while True:
        estado_importante = "¡IMPORTANTE!" if mensaje.importante else "Normal"
        print(f"Opciones para mensaje: '{mensaje.asunto}' (Prioridad: {estado_importante})")
        opcion_importante = "Desmarcar como importante" if mensaje.importante else "Marcar como importante"
        
        print(f"(1). {opcion_importante}")
        print("(2). Leer mensaje (y marcar como leído)")
        print("(3). Volver atrás")
        print("-------------------------")
        seleccion = input("Seleccione una opción: ")

        if seleccion == "1":
            if mensaje.importante:
                mensaje.marcar_importante(False) # lo desmarca en el objeto
                usuario.quitar_importante(mensaje) # lo quita de la lista del usuario
                print("--Mensaje desmarcado como importante--")
            else:
                mensaje.marcar_importante(True) # lo marca en el objeto
                usuario.agregar_importante(mensaje) # lo agrega a la lista del usuario
                print("--¡Mensaje marcado como IMPORTANTE!--")
        
        elif seleccion == "2":
            # muestra el contenido completo del mensaje
            print(f"\n--- LEYENDO MENSAJE ---")
            print(f"De: {mensaje.remitente.nombre_completo} <{mensaje.remitente.correo}>")
            print(f"Fecha: {mensaje.fecha}")
            print(f"Asunto: {mensaje.asunto}")
            print("-------------------------")
            print(f"Cuerpo:\n{mensaje.cuerpo}")
            print("-------------------------")
            mensaje.marcar_como_leido()
            print("El mensaje ha sido marcado como leído.")
        
        elif seleccion == "3":
            break 
        
        else:
            print("Opción no válida.")

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

def crear_filtro(usuario):
    print(" Crear Nuevo Filtro Automático ")
    print("El filtro moverá automáticamente los correos.")

    print("¿Sobre qué campo quieres filtrar?" )
    print("(1). Remitente (email exacto)" )
    print("(2). Asunto (palabra clave)" )
    criterio_opcion = input("Seleccione una opción: ")

    if criterio_opcion == "1":
        criterio = "remitente"
        valor = input("Ingrese el correo del remitente: ")
    elif criterio_opcion == "2":
        criterio = "asunto"
        valor = input("Ingrese la palabra a buscar: ")
    else:
        print("Error: Opcion no valida.")
        print("Porfavor seleccione una opcion valida.")
        return

    #ahora vamos a pedirle al usuario que nos diga como se va a llamar la carpeta de destino
    print("Estas son las carpetas disponible:")
    mostrar_carpetas(usuario.carpeta_raiz)
    destino = input("Ingrese el nombre de la carpeta de destino: ")

    #validamos que exista la carpeta 
    if not usuario.buscar_carpeta(usuario.carpeta_raiz , destino):
        print(f"Error: La carpeta {destino} no existe. Por favor, creela primero.")
        return
    
    regla = {
        "criterio": criterio,
        "valor": valor.lower(),
        "accion": "mover",
        "destino": destino
    }
    
    usuario.agregar_filtro(regla)
    """
     Una vez echa la validacion, creamos el diccionario como tal y utilizamos el metodo que definimos en la clase user y lo agregamos en la lista
    """




def main():
    sesion_iniciada = False
    usuario = None
    
    while True:
        if not sesion_iniciada:
            #revisamos si la lista de usuarios está vacía
            hay_usuarios_registrados = len(ServidorCorreo.usuarios) > 0
            accion = menu_principal(hay_usuarios_registrados) # y la respuesta a la duda se la pasamos al menú principal para saber qué mostrarle al usuario.
            
            if accion == "login":
                usuario = primera_opcion()
                if usuario:
                    sesion_iniciada = True
            elif accion == "register":
                usuario = segunda_opcion()
                if usuario:
                    sesion_iniciada = True
            elif accion == "exit":
                print("Saliendo...")
                print("-------------------------")
                break
            else: #"Invalida"
                print("Opción no válida. Intente de nuevo.")
                print("-------------------------")
            
        else:
            seleccion = inicio()
            
            if seleccion == "1":
                menu_gestionar_mensajes(usuario)
            
            elif seleccion == "2":
                menu_gestionar_carpetas(usuario)

            elif seleccion == "3":
                crear_filtro(usuario)

            elif seleccion == "4":
                print("Buscador de mensajes")
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
                print("Cerrando sesión...")
                print("-------------------------")
                sesion_iniciada = False
                usuario = None
            
            else:
                print("Opción no válida. Intente de nuevo.")
                print("-------------------------")

if __name__ == "__main__":
    main()