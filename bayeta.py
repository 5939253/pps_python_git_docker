import os
from pymongo import MongoClient

def instanciar():
    mongo_url = os.environ.get('MONGO_URL', 'mongodb://db:27017/')
    cliente = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
    bd = cliente['bayeta']
    return bd['frases_auspiciosas']

# 2. Inicialización: Carga datos desde el fichero si la BBDD está vacía
def inicializar(fichero="frases.txt"):
    coleccion = instanciar()
    
    # Solo insertamos si la colección está vacía
    if coleccion.count_documents({}) == 0:
        if os.path.exists(fichero):
            with open(fichero, 'r', encoding='utf-8') as f:
                # Creamos la lista de diccionarios para Mongo
                frases = [{"frase": linea.strip()} for linea in f if linea.strip()]
            
            if frases:
                coleccion.insert_many(frases)
                print(f"Base de datos inicializada con {len(frases)} frases.")
        else:
            print("Error: No se encuentra el fichero de frases.")

# 3. Consulta: Obtiene N frases aleatorias de Mongo
def consultar(n_frases: int = 1) -> list:
    coleccion = instanciar()
    
    pipeline = [{"$sample": {"size": n_frases}}]
    resultados = list(coleccion.aggregate(pipeline))
    
    # Extraemos solo el texto de la frase
    return [r['frase'] for r in resultados]

# Esta función es la que llama app.py
def frotar(n_frases: int = 1) -> list:
    return consultar(n_frases)