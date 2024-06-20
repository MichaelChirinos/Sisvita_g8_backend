from flask import Blueprint, request, jsonify, make_response
from model.alternativa import Alternativa
from utils.db import db
from schemas.alternativa import Alternativa_schema, Alternativas_schema

alternativa = Blueprint('alternativa', __name__)

# Obtener mensaje de prueba
@alternativa.route('/alternativa/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-back'
    return jsonify(result)

# Crear una nueva alternativa
@alternativa.route('/alternativa/v1/agregar', methods=['POST'])
def crear_alternativa():
    id_tipo_test = request.json.get("id_tipo_test")
    descripcion = request.json.get("descripcion")
    puntaje = request.json.get("puntaje")

    alternativa = Alternativa(
        id_alternativa=None,  # SQLAlchemy manejará el autoincremento
        id_tipo_test=id_tipo_test,
        descripcion=descripcion,
        puntaje=puntaje
    )

    db.session.add(alternativa)
    db.session.commit()

    result = Alternativa_schema.dump(alternativa)

    data = {
        'message': 'Alternativa creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las alternativas
@alternativa.route('/alternativa/v1/listar/<int:id_tipo_test>', methods=['GET'])
def listar_alternativas(id_tipo_test):
    all_alternativas = Alternativa.query.filter_by(id_tipo_test=id_tipo_test).all()
    result = Alternativas_schema.dump(all_alternativas)

    data = {
        'message': 'Alternativas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar una alternativa
@alternativa.route('/alternativa/v1/actualizar/<int:id_alternativa>', methods=['PUT'])
def actualizar_alternativa(id_alternativa):
    alternativa = Alternativa.query.get(id_alternativa)
    if not alternativa:
        return jsonify({"error": "Alternativa no encontrada"}), 404

    id_tipo_test = request.json.get("id_tipo_test")
    descripcion = request.json.get("descripcion")
    puntaje = request.json.get("puntaje")

    alternativa.id_tipo_test = id_tipo_test
    alternativa.descripcion = descripcion
    alternativa.puntaje = puntaje

    db.session.commit()

    result = Alternativa_schema.dump(alternativa)

    data = {
        'message': 'Alternativa actualizada correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)

# Eliminar una alternativa
@alternativa.route('/alternativa/v1/eliminar/<int:id_alternativa>', methods=['DELETE'])
def eliminar_alternativa(id_alternativa):
    alternativa = Alternativa.query.get(id_alternativa)
    if not alternativa:
        return jsonify({"error": f"Alternativa con id {id_alternativa} no encontrada"}), 404

    db.session.delete(alternativa)
    db.session.commit()

    data = {
        'message': 'Alternativa eliminada correctamente',
        'status': 200,
        'data': {}
    }

    return make_response(jsonify(data), 200)
