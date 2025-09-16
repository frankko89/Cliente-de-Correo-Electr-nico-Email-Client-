import datetime as dt

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