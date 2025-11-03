class Mensaje():
    def __init__(self, remitente, destinatario, asunto, cuerpo, fecha):
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__asunto = asunto
        self.__cuerpo = cuerpo
        self.__fecha = fecha
        self.__leido = False
        self.__importante = False
        
    @property
    def remitente(self):
        return self.__remitente
    
    @property
    def destinatario(self):
        return self.__destinatario
    
    @property
    def asunto(self):
        return self.__asunto
    
    @property
    def cuerpo(self):
        return self.__cuerpo
    
    @property
    def fecha(self):
        return self.__fecha
    
    @property
    def leido(self):
        return self.__leido
    
    @property
    def importante(self):
        return self.__importante
    
    def mostrar_mensaje(self):
        print(f"De: {self.remitente.nombre_completo} <{self.remitente.correo}>")
        print(f"Para: {self.destinatario.nombre_completo} <{self.destinatario.correo}>")
        print(f"Asunto: {self.asunto}")
        print(f"Fecha: {self.fecha}")
        print(f"Cuerpo: {self.cuerpo}")
        
    def marcar_como_leido(self):
        self.leido = True 
        print("El mensaje ha sido marcado como leído.")
    
    def marcar_importante(self, es_importante):
        self.__importante = es_importante