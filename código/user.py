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
        self.__bandeja_entrada = self.__carpeta_raiz.agregar_subcarpeta("Bandeja de Entrada")
        self.__bandeja_salida = self.__carpeta_raiz.agregar_subcarpeta("Bandeja de Salida")
        self.__importantes = []

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
    
    @property
    def importantes(self):
        return self.__importantes
        
    def agregar_importante(self, mensaje):
        if mensaje not in self.__importantes:
            self.__importantes.append(mensaje)
            
    def quitar_importante(self, mensaje):
        if mensaje in self.__importantes:
            self.__importantes.remove(mensaje)
    
    def buscar_carpeta(self, nodo_actual, nombre_carpeta):
        #va a buscar una carpeta en el árbol general según su nombre de forma recursiva
        if nodo_actual is None:
            return None
        
        if nodo_actual.nombre.lower() == nombre_carpeta.lower():
            return nodo_actual
        
        #busca en el primer hijo
        hijo_encontrado = self.buscar_carpeta(nodo_actual.hijo, nombre_carpeta)
        if hijo_encontrado:
            return hijo_encontrado
        #busca en el siguiente hermano
        return self.buscar_carpeta(nodo_actual.siguiente_hermano, nombre_carpeta)
    
    def mover_mensaje(self, mensaje_a_mover, nombre_origen, nombre_destino):
        #función para mover mensaje de una carpeta a otra
        
        #primero buscamos las carpetas por su nombre dentro del árbol
        carpeta_origen = self.buscar_carpeta(self.carpeta_raiz, nombre_origen)
        carpeta_destino = self.buscar_carpeta(self.carpeta_raiz, nombre_destino)
        
        if not carpeta_origen:
            print(f"Error: Carpeta de origen '{nombre_origen}' no encontrada.")
            return False 
        if not carpeta_destino:
            print(f"Error: Carpeta de destino '{nombre_destino}' no encontrada.")
            return False
        
        if carpeta_origen.eliminar_mensaje(mensaje_a_mover): #eliminamos el mensaje de la carpeta de origen
            carpeta_destino.agregar_mensajes(mensaje_a_mover)
            print(f"Mensaje movido exitosamente de '{nombre_origen}' a '{nombre_destino}'.")
            return True
        else:
            print(f"Error: El mensaje no se encontró en la carpeta '{nombre_origen}.")
            return False