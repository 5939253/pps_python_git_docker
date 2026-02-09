# --- FASE 1: Resolución de dependencias ---
FROM python:3.11-slim AS builder

WORKDIR /app

# Copiamos el archivo de requisitos
COPY requirements.txt .

# Instalamos las dependencias en una carpeta temporal
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# --- FASE 2: Ejecución ---
FROM python:3.11-slim

WORKDIR /app

# Copiamos solo las dependencias instaladas de la fase anterior
COPY --from=builder /install /usr/local

# Copiamos el código de la aplicación
COPY . .

# Exponemos el puerto 5000 que es el de Flask
EXPOSE 5000

# Comando para arrancar la aplicación
CMD ["python", "app.py"]