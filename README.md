# pps_python_git_docker

Ejercicio de Clase de Puesta en producción segura

## 🚀 Despliegue con Docker Compose (v4.0)

Esta versión utiliza **Docker Compose** para orquestar la aplicación web (Flask) y la base de datos (MongoDB).

### Requisitos

* Docker Desktop instalado y en ejecución.
* Archivo `frases.txt` en la raíz del proyecto.

### Instrucciones de ejecución

Ya no es necesario construir y ejecutar los contenedores por separado. Ahora simplemente usa:

1. **Levantar el ecosistema:**

   ``` bash
   docker compose up --build
   ```