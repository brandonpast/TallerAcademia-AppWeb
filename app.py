from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
from flask_cors import CORS

CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}}) 

# Endpoint GET para devolver los datos
@app.route('/api/elementos', methods=['GET'])
def obtener_elementos():
    try:
        elementos = [
            {"id": 1, "nombre": "Elemento 10", "descripcion": "Descripción del elemento 10"},
            {"id": 2, "nombre": "Elemento 20", "descripcion": "Descripción del elemento 20"},
            {"id": 3, "nombre": "Elemento 30", "descripcion": "Descripción del elemento 30"}
        ]
        return jsonify(elementos), 200
    except Exception as e:
        return jsonify({"error": "Ocurrió un error"}), 500  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)   
