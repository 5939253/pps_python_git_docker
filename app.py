from flask import Flask, jsonify
from bayeta import frotar, inicializar

app = Flask(__name__)

# Inicializamos la BBDD al arrancar
inicializar()

@app.route('/')
def home():
    return "La Bayeta con MongoDB está lista."

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def get_frases(n_frases):
    return jsonify(frotar(n_frases))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)