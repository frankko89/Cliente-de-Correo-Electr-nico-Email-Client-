import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from folder import Carpeta
from mail import Mensaje
import datetime as dt

@pytest.fixture
def carpeta_raiz():
    return Carpeta("Raiz")

@pytest.fixture
def mensaje_simple():
    class DummyUser:
        def __init__(self, correo):
            self.correo = correo
            self.nombre_completo = "Test User"
            
    remitente = DummyUser("a@test.com")
    destinatario = DummyUser("b@test.com")
    return Mensaje(remitente, destinatario, "Hola", "Cuerpo", dt.date.today())

def test_crear_subcarpeta_primer_hijo(carpeta_raiz):
    hijo1 = carpeta_raiz.agregar_subcarpeta("Hijo1")
    
    assert carpeta_raiz.hijo is not None
    assert carpeta_raiz.hijo == hijo1
    assert carpeta_raiz.hijo.nombre == "Hijo1"

def test_crear_hermanos_correctamente(carpeta_raiz):
    hijo1 = carpeta_raiz.agregar_subcarpeta("Hijo1")
    hijo2 = carpeta_raiz.agregar_subcarpeta("Hijo2")
    hijo3 = carpeta_raiz.agregar_subcarpeta("Hijo3")

    assert carpeta_raiz.hijo == hijo1 
    assert hijo1.siguiente_hermano == hijo2 
    assert hijo2.siguiente_hermano == hijo3 
    assert hijo3.siguiente_hermano is None 

def test_agregar_y_eliminar_mensaje(carpeta_raiz, mensaje_simple):
    carpeta_raiz.agregar_mensajes(mensaje_simple)
    assert len(carpeta_raiz.mensajes) == 1
    assert carpeta_raiz.mensajes[0] == mensaje_simple
    
    resultado = carpeta_raiz.eliminar_mensaje(mensaje_simple)
    assert resultado is True
    assert len(carpeta_raiz.mensajes) == 0

def test_eliminar_mensaje_inexistente(carpeta_raiz, mensaje_simple):
    resultado = carpeta_raiz.eliminar_mensaje(mensaje_simple)
    assert resultado is False 