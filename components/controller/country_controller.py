from flask import Blueprint, request, jsonify
from ..model.country_model import insertar_pais

pais_bp = Blueprint('pais', __name__)

@pais_bp.route('/api/paises', methods=['POST'])
def agregar_pais():
    data = request.json
    return jsonify(insertar_pais(data))