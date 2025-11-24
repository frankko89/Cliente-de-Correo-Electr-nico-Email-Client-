import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from user import Usuario
from mail import Mensaje
import datetime as dt

@pytest.fixture
def usuario_test():
    return Usuario("Juan", "Perez", "juan@test.com", "1234")

@pytest.fixture
def mensaje_dummy():
    class Dummy: pass
    return Dummy() 

def test_estructura_inicial_usuario(usuario_test):
    raiz = usuario_test.carpeta_raiz
    assert usuario_test.bandeja_entrada is not None
    assert usuario_test.bandeja_entrada.nombre == "Bandeja de Entrada"
    assert usuario_test.bandeja_salida is not None

def test_mover_mensaje_exitoso(usuario_test, mensaje_dummy):
    origen = usuario_test.bandeja_entrada
    destino = usuario_test.bandeja_salida 
    
    origen.agregar_mensajes(mensaje_dummy)
    assert len(origen.mensajes) == 1
    assert len(destino.mensajes) == 0
    
    resultado = usuario_test.mover_mensaje(mensaje_dummy, "Bandeja de Entrada", "Bandeja de Salida")

    assert resultado is True
    assert len(origen.mensajes) == 0
    assert len(destino.mensajes) == 1
    assert destino.mensajes[0] == mensaje_dummy

def test_mover_mensaje_carpeta_inexistente(usuario_test, mensaje_dummy):
    usuario_test.bandeja_entrada.agregar_mensajes(mensaje_dummy)
    
    resultado = usuario_test.mover_mensaje(mensaje_dummy, "Bandeja de Entrada", "Narnia")
    
    assert resultado is False
    assert len(usuario_test.bandeja_entrada.mensajes) == 1