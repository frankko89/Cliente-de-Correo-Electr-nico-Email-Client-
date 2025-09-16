import datetime as dt

class Usuario():
    def __init__(self, nombre, apellido, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo 
    
    @property
    def correo(self):
        return self.__correo
    
    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"
    
    def enviar_mensaje(self, destinatario, asunto, cuerpo):
        fecha_actual = dt.date.today()
        return Mensaje(self,destinatario, asunto, cuerpo, fecha_actual)
    
    def recibir_mensaje(self, mensaje):
        print(f"{self.nombre_completo} recibió un mensaje de {mensaje.remitente.nombre_completo}")

class Mensaje():
    def __init__(self, remitente, destinatario, asunto, cuerpo, fecha):
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__asunto = asunto
        self.__cuerpo = cuerpo
        self.__fecha = fecha
        
    @property
    def remitente(self):
        return self.__remitente
    
    @property
    def destinatario(self):
        return self.__destinatario
    
    def mostrar_mensaje(self):
        print(f"De: {self.__remitente.nombre_completo} <{self.__remitente.correo}>")
        print(f"Para: {self.__destinatario.nombre_completo} <{self.__destinatario.correo}>")
        print(f"Asunto: {self.__asunto}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cuerpo: {self.__cuerpo}")
        
user1 = Usuario("Oriana", "Casas", "oriana@gmail.com")
user2 = Usuario("Franco", "Bishalba", "elfran@gmail.com")

mensaje = user1.enviar_mensaje(user2, "Importante", "eu")
user2.recibir_mensaje(mensaje)
mensaje.mostrar_mensaje()
        