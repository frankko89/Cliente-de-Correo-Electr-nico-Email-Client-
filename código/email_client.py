from user import Usuario 
from mail import Mensaje
from folder import Carpeta
import datetime as dt

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
        
        remitente = self.usuarios[remitente_mail]
        destinatario = self.usuarios[destinatario_mail]
    #aca si no tenemos ningun problema con los correos se los asignamos a las variables de la clase Mensaje para poder crear el modelo como tal
        nuevo_mensaje = Mensaje(remitente, destinatario, asunto, cuerpo, dt.date.today())
        remitente.bandeja_salida.agregar_mensajes(nuevo_mensaje)
        destinatario.bandeja_entrada.agregar_mensajes(nuevo_mensaje) 
        print("Mensaje enviado exitosamente.")  
        print("-------------------------")
        return True
    # y por ultimo hacemos que tanto en la bandeja del remitente como en la del destinatario se guarde el mensaje que se envio y terminamos la funcioon con un return para terminar por completo la funcin   