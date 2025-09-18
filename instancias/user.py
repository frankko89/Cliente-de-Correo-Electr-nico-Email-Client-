import datetime as dt
from mail import Mensaje

class Usuario():
    def __init__(self, nombre, apellido, correo, contrasenia):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo 
        self._contrasenia = contrasenia
    
    @property
    def correo(self):
        return self.__correo
    
    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"
    
    @property
    def contrasenia(self):
        return self._contrasenia
    
    def enviar_mensaje(self, destinatario, asunto, cuerpo):
        fecha_actual = dt.date.today()
        return Mensaje(self,destinatario, asunto, cuerpo, fecha_actual)
    
    def recibir_mensaje(self, mensaje):
        print(f"{self.nombre_completo} recibió un mensaje de {mensaje.remitente.nombre_completo}")