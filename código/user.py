import datetime as dt
from mail import Mensaje
from folder import Carpeta

class Usuario():
    def __init__(self, nombre, apellido, correo, contrasenia):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo 
        self.__contrasenia = contrasenia
        self.__carpeta_raiz = Carpeta(f"carpetas de {self.nombre_completo}")
        self.__bandeja_entrada = self.__carpeta_raiz.agregar_subcarpeta("bandeja de entrada")
        self.__bandeja_salida = self.__carpeta_raiz.agregar_subcarpeta("bandeja de salida")

    @property
    def carpeta_raiz(self):
        return self.__carpeta_raiz

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