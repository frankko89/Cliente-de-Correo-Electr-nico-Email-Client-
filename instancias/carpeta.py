from mail import Mensaje
#estos import son para hacer las carpetas de enviados, recibidos y borrados y saber quien los hizo

"""En esta clase se van a almenacer todos los mails enviador, recibidos y borrados pero lo decidimos
hacer en subs-clases para poder tener un mejor control y mejor orden de los mails"""

class Carpeta():
    def  __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = []
    
    def agregar_mensajes(self, mensaje):
        self.mensajes.append(mensaje)
        print (f"el mensaje se agrego a la carpeta {self.nombre}")

    """metodo para filtrar los mensajes por asunto"""
    def filtrar_por_asunto(self, asunto_filtro):
        busqueda = []
        for x in self.mensajes: 
            if asunto_filtro in x.asunto:
                busqueda.append(x)
        return busqueda

    def filtrar_por_usuario(self, usuario_filtro):
        busqueda = []
        for x in self.mensajes: 
            if usuario_filtro in x.remitente:
                busqueda.append(x)
        return busqueda