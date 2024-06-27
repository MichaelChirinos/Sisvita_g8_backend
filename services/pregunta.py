from flask import Blueprint, request, jsonify, make_response
from model.pregunta import Pregunta
from utils.db import db
from schemas.pregunta import Pregunta_schema, Preguntas_schema

pregunta = Blueprint('pregunta', __name__)

# Obtener mensaje de prueba
@pregunta.route('/pregunta/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-back'
    return jsonify(result)

# Crear una nueva pregunta
@pregunta.route('/pregunta/v1/agregar', methods=['POST'])
def crear_pregunta():
    id_tipo_test = request.json.get("id_tipo_test")
    descripcion = request.json.get("descripcion")

    pregunta = Pregunta(
        id_pregunta=None,  # SQLAlchemy manejará el autoincremento
        id_tipo_test=id_tipo_test,
        descripcion=descripcion
    )

    db.session.add(pregunta)
    db.session.commit()

    result = Pregunta_schema.dump(pregunta)

    data = {
        'message': 'Pregunta creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las preguntas
@pregunta.route('/pregunta/v1/listar/<int:id_tipo_test>', methods=['GET'])
def listar_preguntas(id_tipo_test):
    all_preguntas = Pregunta.query.filter_by(id_tipo_test=id_tipo_test).all()
    result = Preguntas_schema.dump(all_preguntas)

    data = {
        'message': 'Preguntas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar una pregunta
@pregunta.route('/pregunta/v1/actualizar/<int:id_pregunta>', methods=['PUT'])
def actualizar_pregunta(id_pregunta):
    pregunta = Pregunta.query.get(id_pregunta)
    if not pregunta:
        return jsonify({"error": "Pregunta no encontrada"}), 404

    id_tipo_test = request.json.get("id_tipo_test")
    descripcion = request.json.get("descripcion")

    pregunta.id_tipo_test = id_tipo_test
    pregunta.descripcion = descripcion

    db.session.commit()

    result = Pregunta_schema.dump(pregunta)

    data = {
        'message': 'Pregunta actualizada correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)

# Eliminar una pregunta
@pregunta.route('/pregunta/v1/eliminar/<int:id_pregunta>', methods=['DELETE'])
def eliminar_pregunta(id_pregunta):
    pregunta = Pregunta.query.get(id_pregunta)
    if not pregunta:
        return jsonify({"error": f"Pregunta con id {id_pregunta} no encontrada"}), 404

    db.session.delete(pregunta)
    db.session.commit()

    data = {
        'message': 'Pregunta eliminada correctamente',
        'status': 200,
        'data': {}
    }

    return make_response(jsonify(data), 200)
