from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

# Endpoint raíz para el Hola Mundo (localhost:5000)
@app.route('/')
def home():
    return "Hola, mundo"

# Endpoint para obtener las frases en formato JSON
@app.route('/frotar/<int:n_frases>', methods=['GET'])
def get_frases(n_frases):
    # Llamamos a la función que devuelve la lista
    lista_frases = frotar(n_frases)
    # Devolvemos la lista convertida a JSON
    return jsonify(lista_frases)

if __name__ == '__main__':
    # Ejecutamos el servidor en el puerto 5000
    app.run(host='0.0.0.0', port=5000, debug=True)