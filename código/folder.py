from mail import Mensaje

class Carpeta():
    def  __init__(self, nombre):
        self.__nombre = nombre
        self.__mensajes = []
        self.__primer_hijo = None # aca lo que hacemos es crear o moldear la estructura del arbol general con los nodos
        self.__siguiente_hermano = None # lo mismo en esta

    @property
    def nombre(self):
        return self.__nombre

    @property
    def mensajes(self):
        return self.__mensajes
    
    @property
    def hijo(self):
        return self.__primer_hijo
    
    @property
    def siguiente_hermano(self):
        return self.__siguiente_hermano
    
    #ahora hacemos el setter para poder asignarle o modificarle el valor cuando sea necesario
    @siguiente_hermano.setter
    def siguiente_hermano (self, valor):
        self.__siguiente_hermano = valor

# aca esta creada la busqueda recursiva para remitente o asunto
    def agregar_mensajes(self, mensaje):
        self.mensajes.append(mensaje)
    
    def eliminar_mensaje(self, mensaje):
        try:
            self.mensajes.remove(mensaje)
            return True
        except ValueError:
            #ValueError se utiliza cuando hay un error en la lógica de la llamada, en este caso, cuando se llama a un mensaje que no existe o que no se encontró en esa carpeta.
            return False

    def agregar_subcarpeta(self , dato):
        nuevo_dato = Carpeta(dato)
        #aca lo que hacemos es que a esta nueva variable le decimos o asignamos toda la estructura de la clase y dato es el valor que va a tener el nodo        
        if self.__primer_hijo is None:
            self.__primer_hijo = nuevo_dato
        else:
            hijo_actual = self.__primer_hijo 
           #Aca lo  que haces es que si ya existe un hijo recorremos la lista recursivamente mientras que no este vacia
            while hijo_actual.siguiente_hermano  is not None:
                hijo_actual = hijo_actual.siguiente_hermano

            hijo_actual.siguiente_hermano = nuevo_dato
            #esto lo que hace es mantener la rama para que se pueda a volver a enlazar un nodo nuevo iterativamente 
        return nuevo_dato


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