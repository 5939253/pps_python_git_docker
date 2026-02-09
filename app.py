import time
from flask import Flask, jsonify, request
from bayeta import frotar, inicializar, insertar_frases

app = Flask(__name__)

# Esperamos 5 segundos para dar tiempo a que Mongo arranque
print("Esperando a que la base de datos esté lista...")
time.sleep(5)

try:
    inicializar()
except Exception as e:
    print(f"Error inicializando: {e}")

# Inicializamos la BBDD al arrancar
inicializar()

@app.route('/')
def home():
    return "La Bayeta con MongoDB está lista."

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def get_frases(n_frases):
    return jsonify(frotar(n_frases))

@app.route('/frotar/add', methods=['POST'])
def add_frases():
    # Obtenemos el JSON enviado por el cliente
    datos = request.get_json()
    
    # Esperamos un formato como: {"frases": ["frase 1", "frase 2"]}
    if datos and 'frases' in datos:
        insertar_frases(datos['frases'])
        return jsonify({"status": "success", "message": "Frases añadidas"}), 200
    else:
        return jsonify({"status": "error", "message": "Formato JSON inválido"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)