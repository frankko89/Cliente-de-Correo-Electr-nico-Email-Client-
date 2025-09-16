from user import Usuario 

class servidorCorreo():
    pass

class Carpeta(servidorCorreo):
    pass
        
user1 = Usuario("Oriana", "Casas", "oriana@gmail.com")
user2 = Usuario("Franco", "Bishalba", "elfran@gmail.com")

mensaje = user1.enviar_mensaje(user2, "Importante", "eu")
user2.recibir_mensaje(mensaje)
mensaje.mostrar_mensaje()
        