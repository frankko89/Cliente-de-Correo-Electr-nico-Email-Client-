import datetime as dt
from mail import Mensaje
from folder import Carpeta

class Usuario():
    def __init__(self, nombre, apellido, correo, contrasenia):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo 
        self.__contrasenia = contrasenia
        self.__bandeja_entrada = Carpeta("Bandeja de Entrada")
        self.__bandeja_salida = Carpeta("Bandeja de Salida")
            
    @property
    def correo(self):
        return self.__correo
    
    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"
    
    @property
    def contrasenia(self):
        return self.__contrasenia
    
    @property
    def bandeja_entrada(self):
        return self.__bandeja_entrada
    
    @property
    def bandeja_salida(self):
        return self.__bandeja_salida