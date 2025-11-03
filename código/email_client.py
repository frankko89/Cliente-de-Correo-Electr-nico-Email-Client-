from user import Usuario 
from mail import Mensaje
from folder import Carpeta
import datetime as dt

#indicamos posibles variables de dominios
TIPO_DE_DOMINIO = {
    "mail.com": ["hotmail.com", "outlook.com", "yahoo.com"],  
    "gmail.com": ["yahoo.com"],                         
    "hotmail.com": ["outlook.com", "mail.com"],
    "outlook.com": ["hotmail.com", "mail.com"],
    "yahoo.com": ["gmail.com", "mail.com"],
    "unab.edu.com": ["google.com"],
    "google.com": ["unab.edu.com"]
}

#creamos una función de búsqueda recursiva DFS
def _buscar_camino(nodo_actual, destino, visitados):
    #marca el nodo actual como visitado
    visitados.add(nodo_actual)
    
    #obtiene los "vecinos" o conexiones
    conexiones = TIPO_DE_DOMINIO.get(nodo_actual, [])
    
    #caso base 1: si el destino es un vecino directo
    if destino in conexiones:
        return [nodo_actual, destino] 
    
    #caso recursivo: busca todas las conexiones
    for conexion in conexiones:
        if conexion not in visitados:
            camino_encontrado = _buscar_camino(conexion, destino, visitados)
            
            if camino_encontrado:
                return [nodo_actual] + camino_encontrado
            
    #caso base 2: no encontró camino en este nodo
    return None

class servidorCorreo():
    def __init__ (self):
        self.__usuario = {}
    
    @property
    def usuarios(self):
        return self.__usuario

    def registrarse(self, nombre, apellido, correo, contrasenia):
            if correo in self.usuarios: #aca revisa si el correo ya existe en el diccionario
                print("El correo ya está registrado.")
                return False #esto lo ponemos para que el codigo si lo necesita pueda usarlo en alguna linea
            #si da el caso que no existe va a llamar a usuario para crear un nuevo usuario y registarlo
            elif nombre == "" or apellido == "" or correo == "" or contrasenia == "":
                print("Todos los campos son obligatorios.")
                return False
            elif nombre.isdigit() or apellido.isdigit():
                print("El nombre y apellido no pueden contener números.")
                return False
            elif "@" not in correo or "." not in correo:
                print("El correo no es válido.")
                return False
            else:
                nuevo_usuario = Usuario(nombre, apellido, correo, contrasenia) 
                self.usuarios[correo] = nuevo_usuario
                return nuevo_usuario 

    def iniciar_sesion(self, correo, contrasenia):
        if correo not in self.usuarios: #revisa si el correo existe en el diccionario
                print("El correo no está registrado, por favor registrese.")
                return False
        elif contrasenia == "":
                print("Todos los campos son obligatorios.")
                return False
            
        buscar_usuario = self.usuarios[correo] #si existe lo busca en el diccionario
        if buscar_usuario.contrasenia == contrasenia: #revisa si la contrasenia es correcta
                return buscar_usuario
        else:
            print("Contrasenia incorrecta.")
            return False
        
    def enviar_mensaje(self, remitente_mail, destinatario_mail, asunto, cuerpo):
    #aca ahora vamos a revisar si el destinatario existe y si no es el caso vamos a tirar un error
        if destinatario_mail not in self.usuarios:
            print(f"El correo del destinatario {destinatario_mail} no está registrado.")
            print("-------------------------")
            return False
        
        try:
            dominio_origen = remitente_mail.split('@')[1]
            dominio_destino = destinatario_mail.split('@')[1]
        except IndexError:
            print("Error: Los correos no tienen un formato válido (falta @ o dominio).")
            return False

        if dominio_origen == dominio_destino:
            print("Detectado envío interno (mismo dominio)...")
        else:
            print(f"Detectado envío externo: {dominio_origen} -> {dominio_destino}")
            ruta_encontrada = _buscar_camino(dominio_origen, dominio_destino, set())
            
            if ruta_encontrada is None:
                print(f"Error de Red: No se encontró una ruta de {dominio_origen} a {dominio_destino}.")
                print("El mensaje NO se puede enviar.")
                print("-------------------------")
                return False # detiene el envío si no hay ruta
            else:
                ruta_str = " -> ".join(ruta_encontrada)
                print(f"Simulación de Red: Ruta encontrada: {ruta_str}")
        
        remitente = self.usuarios[remitente_mail]
        destinatario = self.usuarios[destinatario_mail]

        mensaje_salida = Mensaje(remitente, destinatario, asunto, cuerpo, dt.date.today())
        mensaje_entrada = Mensaje(remitente, destinatario, asunto, cuerpo, dt.date.today())

        remitente.bandeja_salida.agregar_mensajes(mensaje_salida)

        mensaje_filtrado = False
        for regla in destinatario.filtros:
            
            coincidencia = False
            if regla["criterio"] == "remitente":
                  if mensaje_salida.remitente.correo.lower() == regla["valor"]:
                       coincidencia = True
            
            elif regla["criterio"] == "asunto":
                 if regla["valor"] in mensaje_entrada.asunto.lower():
                     coincidencia = True

            #ahora se ejecutaria la parte donde si hubo coincidencias
            if coincidencia:
                print(f"Se encontro la carpeta indicada: moviendo a {regla['destino']}...")
                carpeta_destino = destinatario.buscar_carpeta(destinatario.carpeta_raiz, regla["destino"])
                
                if carpeta_destino:
                    # si encontramos la carpeta, agregamos el mensaje
                    carpeta_destino.agregar_mensajes(mensaje_entrada)
                    mensaje_filtrado = True
                    break 
                else:
                    print(f"Advertencia: La carpeta de filtro '{regla['destino']}' no se encontró.")

        #si no se encontro ninguna carpeta que coincida o no se movio a ninguna, directamente se manda a la carpeta de mensajes
        if not mensaje_filtrado:
            print("No se aplicó ningún filtro. Moviendo a Bandeja de Entrada.")
            destinatario.bandeja_entrada.agregar_mensajes(mensaje_entrada)
       
        print("Mensaje enviado exitosamente.")
        print("-------------------------")
        return True
    # y por ultimo hacemos que tanto en la bandeja del remitente como en la del destinatario se guarde el mensaje que se envió y terminamos la función con un return para terminar por completo la función   