from user import Usuario 
from mail import Mensaje
from carpeta import Carpeta
import datetime as dt

class servidorCorreo():
    def __init__ (self):
        self._usuario = {}
        self.bandeja_entrada = Carpeta("Bandeja de Entrada")
        self.bandeja_salida = Carpeta("Bandeja de Salida")


    def registrarse(self, nombre, apellido, correo, contrasenia):
            if correo in self._usuario: #aca revisa si el correo ya existe en el diccionario
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
                self._usuario[correo] = nuevo_usuario
                return nuevo_usuario 

    def iniciar_sesion(self, correo, contrasenia):
        if correo not in self._usuario: #revisa si el correo existe en el diccionario
                print("El correo no está registrado, por favor registrese.")
                return False
        elif contrasenia == "":
                print("Todos los campos son obligatorios.")
                return False
            
        buscar_usuario = self._usuario[correo] #si existe lo busca en el diccionario
        if buscar_usuario.contrasenia == contrasenia: #revisa si la contrasenia es correcta
                return buscar_usuario
        else:
            print("contrasenia incorrecta")
            return False
        
    def enviar_mensaje(self, remitente_mail, destinatario_mail, asunto, cuerpo):
        
    #aca ahora vamos a revisar si el destinatario existe y si no es el caso vamos a tirar un error
        if destinatario_mail not in self._usuario:
            print(f"El correo del destinatario {destinatario_mail} no está registrado.")
            print("-------------------------")
            return False
        
        remitente = self._usuario[remitente_mail]
        destinatario = self._usuario[destinatario_mail]
        fecha_actual = dt.date.today()
    #aca si no tenemos ningun problema con los correos se los asignamos a las variables de la clase Mensaje para poder crear el modelo como tal
        Nuevo_mensaje = Mensaje(remitente, destinatario, asunto, cuerpo, fecha_actual)
        self.bandeja_salida.append(Nuevo_mensaje)
        destinatario.bandeja_entrada.append(Nuevo_mensaje)  
        print("Mensaje enviado exitosamente.")  
        print("-------------------------")
        return True
    # y por ultimo hacemos que tanto en la bandeja del remitente como en la del destinatario se guarde el mensaje que se envio y terminamos la funcioon con un return para terminar por completo la funcin

    def organizar_mensajes(self):
            #aquí iría la lógica para mostrar y organizar los mensajes mostrando solo asunto y usuario
            pass
    
    def buscar_mensajes(self, criterio):
            resultados_asunto = self.bandeja_entrada.filtrar_por_asunto(criterio) or self.bandeja_salida.filtrar_por_asunto(criterio)
            resultados_usuario = self.bandeja_entrada.filtrar_por_usuario(criterio) or self.bandeja_salida.filtrar_por_usuario(criterio)
            resultados = resultados_asunto + resultados_usuario
            
            if not resultados:
                print("No se encontraron mensajes que coincidan con el criterio.")
            else:
                print(f"Se encontraron {len(resultados)} mensajes:")
                for mensaje in resultados:
                    #llamaria a organizar_mensajes() para mostrar los mensajes encontrados con el asunto y usuario
                    pass

    