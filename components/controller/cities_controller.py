from flask import Blueprint, request, jsonify
from components.model.poblacion_model import (
    obtener_poblaciones,
    insertar_poblacion,
    actualizar_poblacion,
    eliminar_poblacion
)

poblacion_bp = Blueprint('poblacion', __name__)

@poblacion_bp.route('/api/poblaciones', methods=['GET'])
def listar_poblaciones():
    try:
        poblaciones = obtener_poblaciones()
        return jsonify(poblaciones), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@poblacion_bp.route('/api/poblaciones', methods=['POST'])
def agregar_poblacion():
    data = request.get_json()
    resultado = insertar_poblacion(data)
    return jsonify(resultado), 201 if "message" in resultado else 400

@poblacion_bp.route('/api/poblaciones/<int:poblacionid>', methods=['PUT'])
def modificar_poblacion(poblacionid):
    data = request.get_json()
    resultado = actualizar_poblacion(poblacionid, data)
    return jsonify(resultado), 200 if "message" in resultado else 400

@poblacion_bp.route('/api/poblaciones/<int:poblacionid>', methods=['DELETE'])
def borrar_poblacion(poblacionid):
    resultado = eliminar_poblacion(poblacionid)
    return jsonify(resultado), 200 if "message" in resultado else 400
