# pps_python_git_docker
Ejercicio de Clase de Puesta en producción segura
## 🐳 Despliegue con Docker (v3.0)
Esta aplicación está dockerizada para garantizar un entorno estable.

### Requisitos
* Docker Desktop instalado y en ejecución.

### Instrucciones de ejecución
1. **Construir la imagen:**
   ```bash
   docker build -t bayeta-app .
Desplegar el contenedor:

Bash
docker run -d -p 5000:5000 --name contenedor-bayeta bayeta-app
Acceso: Abre tu navegador en http://localhost:5000/frotar/5 (donde 5 es el número de frases deseadas).