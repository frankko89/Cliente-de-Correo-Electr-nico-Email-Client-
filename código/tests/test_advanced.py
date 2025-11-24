import pytest
import sys
import os
import heapq

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from user import Usuario
from mail import Mensaje
from email_client import _buscar_camino 
import datetime as dt

# --- FIXTURES ---
@pytest.fixture
def usuario_con_cola():
    return Usuario("Test", "User", "test@user.com", "1234")

@pytest.fixture
def mensajes_priorizados():
    class DummyUser:
        def __init__(self):
            self.correo = "x@x.com"
            self.nombre_completo = "X"
            self.filtros = [] 
            self.carpeta_raiz = None

    remitente = DummyUser()
    destinatario = DummyUser()
    
    m1 = Mensaje(remitente, destinatario, "Normal", "...", dt.date.today())
    m1.establecer_prioridad(3) 
    
    m2 = Mensaje(remitente, destinatario, "Urgente", "...", dt.date.today())
    m2.establecer_prioridad(1) 
    
    m3 = Mensaje(remitente, destinatario, "Importante", "...", dt.date.today())
    m3.establecer_prioridad(2) 
    
    return [m1, m2, m3]

# --- TESTS DE COLA DE PRIORIDAD (HEAP) ---

def test_cola_prioridad_orden(usuario_con_cola, mensajes_priorizados):
    m_normal, m_urgente, m_importante = mensajes_priorizados
    
    usuario_con_cola.agregar_a_cola(m_normal)
    usuario_con_cola.agregar_a_cola(m_urgente)
    usuario_con_cola.agregar_a_cola(m_importante)
    
    cola_copia = list(usuario_con_cola.cola_de_prioridad)
    heapq.heapify(cola_copia) 
    
    primero = heapq.heappop(cola_copia)
    segundo = heapq.heappop(cola_copia)
    tercero = heapq.heappop(cola_copia)

    assert primero.prioridad == 1
    assert primero.asunto == "Urgente"
    
    assert segundo.prioridad == 2
    
    assert tercero.prioridad == 3

# --- TESTS DE GRAFOS (DFS / RUTAS) ---

def test_busqueda_camino_existente():
    visitados = set()
    camino = _buscar_camino("unab.edu.com", "google.com", visitados)
    
    assert camino is not None
    assert camino == ["unab.edu.com", "google.com"]

def test_busqueda_camino_largo():
    visitados = set()
    camino = _buscar_camino("hotmail.com", "gmail.com", visitados)
    
    assert camino is not None
    assert camino[0] == "hotmail.com"
    assert camino[-1] == "gmail.com"
    assert len(camino) > 2 

def test_camino_inexistente():
    visitados = set()
    camino = _buscar_camino("hotmail.com", "narnia.com", visitados)
    assert camino is None