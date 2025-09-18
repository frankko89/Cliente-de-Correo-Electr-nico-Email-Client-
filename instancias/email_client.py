from user import Usuario 
from mail import Mensaje
class servidorCorreo():
    def __init__ (self):
        self._usuario = {}


def registrarse(self, nombre, apellido, correo, contrasenia):
        if correo in self._usuario: #aca revisa si el correo ya existe en el diccionario
            print("El correo ya está registrado.")
            return False #esto lo ponemos para que el codigo si lo necesita pueda usarlo en alguna linea
        #si da el caso que no existe va a llamar a la usuario para crear un nuevo usuario y registarlo
        else:
            nuevo_usuario = Usuario(nombre, apellido, correo, contrasenia) 
            self._usuario[correo] = nuevo_usuario
            print("Registro exitoso.")
            return True #lo mismo que en la linea 11

def iniciar_sesion(self, correo, contrasenia):
    if correo not in self._usuario: #revisa si el correo existe en el diccionario
            print("El correo no está registrado, por favor registrese.")
            return False
   
    buscar_usuario = self.usuario[correo] #si existe lo busca en el diccionario
    if buscar_usuario.contrasenia == contrasenia: #revisa si la contrasenia es correcta
            print(f"inicio de sesion exitoso. ¡Bienvenido {buscar_usuario.nombre_completo}!")
            return buscar_usuario
    else:
         print("contrasenia incorrecta")
         return False
    
def enviar_mensaje(self, remitente_mail, destinatario_mail, asunto, cuerpo):

#aca ahora vamos a revisar si tanto el remitente como el destinatario existen y si no es el caso vamos a tirar un error
    if remitente_mail not in self.usuario:
        print(f"El correo del remitente {remitente_mail} no está registrado.")
        return False
    
    if destinatario_mail not in self.usuario:
        print(f"El correo del destinatario {destinatario_mail} no está registrado.")
        return False
    
    remitente = self.usuario[remitente_mail]
    destinatario = self.usuario[destinatario_mail]
#aca si no tenemos ningun problema con los correos se los asignamos a las variables de la clase Mensaje para poder crear el modelo como tal
    Nuevo_mensaje = Mensaje(remitente, destinatario, asunto, cuerpo)
    remitente.bandeja_salida.append(Nuevo_mensaje)
    destinatario.bandeja_entrada.append(Nuevo_mensaje)  
    print("Mensaje enviado exitosamente.")  
    return True
# y por ultimo hacemos que tanto en la bandeja del remitente como en la del destinatario se guarde el mensaje que se envio y terminamos la funcioon con un return para terminar por completo la funcin

def organizar_mensajes():
     pass
 #creamos la clase esta pero no la vamos a estar utilizando por el momento 