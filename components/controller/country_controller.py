from flask import Blueprint, request, jsonify
from components.model.country_model import (
    obtener_paises,
    insertar_pais,
    actualizar_pais_en_db,
    eliminar_pais_de_db
)

pais_bp = Blueprint('pais', __name__)

# Obtener todos los países
@pais_bp.route('/api/paises', methods=['GET'])
def listar_paises():
    try:
        paises = obtener_paises()
        return jsonify(paises), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Crear nuevo país
@pais_bp.route('/api/paises', methods=['POST'])
def agregar_pais():
    try:
        data = request.get_json()
        resultado = insertar_pais(data)
        return jsonify(resultado), 201 if "message" in resultado else 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Actualizar país existente
@pais_bp.route('/api/paises/<paisid>', methods=['PUT'])
def actualizar_pais(paisid):
    try:
        data = request.get_json()
        resultado = actualizar_pais_en_db(paisid, data)
        return jsonify(resultado), 200 if "message" in resultado else 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Eliminar país
@pais_bp.route('/api/paises/<paisid>', methods=['DELETE'])
def eliminar_pais(paisid):
    try:
        resultado = eliminar_pais_de_db(paisid)
        return jsonify(resultado), 200 if "message" in resultado else 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
