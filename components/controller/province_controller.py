from flask import Blueprint, request, jsonify
from components.model.province_model import (
    obtener_provincias,
    insertar_provincia,
    actualizar_provincia,
    eliminar_provincia
)

provincia_bp = Blueprint('provincia', __name__)

@provincia_bp.route('/api/provincias', methods=['GET'])
def listar_provincias():
    try:
        provincias = obtener_provincias()
        return jsonify(provincias), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@provincia_bp.route('/api/provincias', methods=['POST'])
def agregar_provincia():
    try:
        data = request.get_json()
        resultado = insertar_provincia(data)
        return jsonify(resultado), 201 if "message" in resultado else 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@provincia_bp.route('/api/provincias/<int:provinciaid>/<paisid>', methods=['PUT'])
def modificar_provincia(provinciaid, paisid):
    try:
        data = request.get_json()
        resultado = actualizar_provincia(provinciaid, paisid, data)
        return jsonify(resultado), 200 if "message" in resultado else 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@provincia_bp.route('/api/provincias/<int:provinciaid>/<paisid>', methods=['DELETE'])
def borrar_provincia(provinciaid, paisid):
    try:
        resultado = eliminar_provincia(provinciaid, paisid)
        return jsonify(resultado), 200 if "message" in resultado else 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
