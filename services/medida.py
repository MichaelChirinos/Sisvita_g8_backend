from flask import Blueprint, request, jsonify, make_response
from model.medida import Medida
from utils.db import db
from schemas.medida import medida_schema, medidas_schema


medida = Blueprint('medida', __name__)


# Obtener mensaje de prueba
@medida.route('/medida/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-back'
    return jsonify(result)

# Crear una nueva alternativa
@medida.route('/medida/v1/agregar', methods=['POST'])
def crear_medida():
    id_especialista = request.json.get("id_especialista")
    descripcion = request.json.get("descripcion")

    medida = Medida(
        id_medida=None,  # SQLAlchemy manejará el autoincremento
        id_especialista=id_especialista,
        descripcion=descripcion
    )


    db.session.add(medida)
    db.session.commit()


    result = medida_schema.dump(medida)


    data = {
        'message': 'Medida creada correctamente',
        'status': 201,
        'data': result
    }


    return make_response(jsonify(data), 201)


# Listar todas las alternativas
@medida.route('/medida/v1/listar/<int:id_especialista>', methods=['GET'])
def listar_medidas(id_especialista):
    all_medidas = Medida.query.filter_by(id_especialista=id_especialista).all()
    result = medidas_schema.dump(all_medidas)

    data = {
        'message': 'Medidas recuperadas correctamente',
        'status': 200,
        'data': result
    }


    return make_response(jsonify(data), 200)


# Actualizar una Medida
@medida.route('/medida/v1/actualizar/<int:id_especialista>', methods=['PUT'])
def actualizar_medida(id_especialista):
    alternativa = Medida.query.get(id_especialista)
    if not alternativa:
        return jsonify({"error": "Alternativa no encontrada"}), 404


    id_especialista = request.json.get("id_especialista")
    descripcion = request.json.get("descripcion")


    alternativa.id_tid_especialistaipo_test = id_especialista
    alternativa.descripcion = descripcion


    db.session.commit()


    result = medida_schema.dump(medida)


    data = {
        'message': 'Medida actualizada correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)

# Eliminar una medida
@medida.route('/medida/v1/eliminar/<int:id_medida>', methods=['DELETE'])
def eliminar_medida(id_medida):
    medida = Medida.query.get(id_medida)
    if not medida:
        return jsonify({"error": f"Medida con id {id_medida} no encontrada"}), 404


    db.session.delete(medida)
    db.session.commit()


    data = {
        'message': 'Medida eliminada correctamente',
        'status': 200,
        'data': {}
    }

    return make_response(jsonify(data), 200)
