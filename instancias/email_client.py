from user import Usuario 

class servidorCorreo():
    def __init__ (self):
        self.mensajes = {}


def registrarse(self, nombre, apellido, correo, contrasenia):
        if correo in self.usuarios: #aca revisa si el correo ya existe en el diccionario
            print("El correo ya está registrado.")
            return  
        #si da el caso que no existe va a llamar a la usuario para crear un nuevo usuario y registarlo
        else:
            nuevo_usuario = Usuario(nombre, apellido, correo, contrasenia) 
            self.usuarios[correo] = nuevo_usuario
            print("Registro exitoso.")
            return  