import datetime as dt
from mail import Mensaje

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