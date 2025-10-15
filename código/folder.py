from mail import Mensaje

class Carpeta():
    def  __init__(self, nombre):
        self.__nombre = nombre
        self.__mensajes = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def mensajes(self):
        return self.__mensajes
    
    def agregar_mensajes(self, mensaje):
        self.mensajes.append(mensaje)
        print (f"el mensaje se agrego a la carpeta {self.nombre}")
    
    def buscar_mensajes(self, criterio):
        return self._buscar_recursivo(self.mensajes, criterio.lower())
    
    def _buscar_recursivo(self, lista_mensajes, criterio_lower):
        if not lista_mensajes:
            return []
        
        primer_mensaje = lista_mensajes[0]
        resto_de_mensajes = lista_mensajes[1:]  
        resultados_del_resto = self._buscar_recursivo(resto_de_mensajes, criterio_lower)   
        remitente = primer_mensaje.remitente.nombre_completo.lower()
        asunto = primer_mensaje.asunto.lower()
        
        if criterio_lower in remitente or criterio_lower in asunto:
            return [primer_mensaje] + resultados_del_resto    
        else:
            return resultados_del_resto