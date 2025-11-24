#  Cliente de Correo Electrónico (EmailClient)

> Sistema de gestión de correos implementado en Python con enfoque en Estructuras de Datos avanzadas.

Este proyecto simula un cliente de correo electrónico completo (backend logic), permitiendo la gestión de usuarios, autenticación, enrutamiento de mensajes a través de dominios y organización jerárquica de carpetas.

---

##  Información del Proyecto

* **Materia:** Estructura de Datos
* **Profesor:** Dr. Diego Agustín Ambrossio (Comisión N° 2)
* **Estado:** Finalizado / Testeado

###  Equipo de Desarrollo

| Estudiante | Rol Principal |
| :--- | :--- |
| **Franco Villalva** | Arquitectura de Árboles, Documentación |
| **Oriana Casas** | Lógica de Búsqueda (Grafos/DFS), Interfaz, QA |

---

##  Arquitectura y Estructuras de Datos

El núcleo del proyecto no es solo POO, sino la implementación eficiente de estructuras no lineales:

* **Árboles Generales (N-arios):** Implementación manual usando la estrategia "Primer Hijo, Siguiente Hermano" para la jerarquía de carpetas de usuario.
* **Grafos & DFS (Búsqueda en Profundidad):** Algoritmo recursivo para simular el enrutamiento de red entre diferentes dominios de correo (ej: `hotmail` -> `gmail`).
* **Colas de Prioridad (Heaps):** Uso de `heapq` para gestionar la bandeja de "Importantes", garantizando que los mensajes de prioridad Alta (1) se procesen antes que los de prioridad Baja (3).

---

##  Instrucciones de Instalación y Uso

### 1. Requisitos Previos
* Python 3.13.7 o superior.
* Git instalado.

### 2. Instalación
Clona el repositorio y accede al directorio:

`git clone https://github.com/frankko89/Cliente-de-Correo-Electr-nico-Email-Client-.git`
`cd Cliente-de-Correo-Electr-nico-Email-Client-`

### 3. Ejecución del Programa
Para iniciar la interfaz de consola:

`python código/main.py`

---

## 🧪 Testing y Calidad (QA)

Este proyecto cuenta con una suite de pruebas automatizadas utilizando **Pytest** para validar la integridad de las estructuras de datos.

### Ejecutar los Tests
Para verificar la robustez del sistema, ejecuta el siguiente comando en la raíz del proyecto:

`python -m pytest`

**Cobertura de las pruebas:**
*  **Integridad Estructural:** Verifica que los nodos del árbol de carpetas mantengan sus referencias (hijos/hermanos).
*  **Lógica de Negocio:** Valida el movimiento de mensajes y excepciones.
*  **Algoritmos:** Prueba el ordenamiento del Heap y la búsqueda de caminos en el Grafo de dominios.

---

## 📊 Gestión del Proyecto
El seguimiento de tareas se realizó mediante metodología Kanban en Trello.
🔗 [Ver Tablero de Trello](https://trello.com/invite/b/68cb2f9d6afe8879e2649caf/ATTIafefb4045afbd8ba7891898b48dd02fcF9DAC096/proyecto-de-correos)