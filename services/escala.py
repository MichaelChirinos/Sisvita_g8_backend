from flask import Blueprint, request, jsonify, make_response
from model.escala import Escala
from utils.db import db
from schemas.escala import Escala_schema, Escalas_schema

escala = Blueprint('escala', __name__)

# Obtener mensaje de prueba
@escala.route('/escala/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-back'
    return jsonify(result)

# Crear una nueva escala
@escala.route('/escala/v1/agregar', methods=['POST'])
def crear_escala():
    id_tipo_test = request.json.get("id_tipo_test")
    puntaje_minimo = request.json.get("puntaje_minimo")
    puntaje_maximo = request.json.get("puntaje_maximo")
    descripcion = request.json.get("descripcion")

    escala = Escala(
        id_rango_escala=None,  # SQLAlchemy manejará el autoincremento
        id_tipo_test=id_tipo_test,
        puntaje_minimo=puntaje_minimo,
        puntaje_maximo=puntaje_maximo,
        descripcion=descripcion
    )

    db.session.add(escala)
    db.session.commit()

    result = Escala_schema.dump(escala)

    data = {
        'message': 'Escala creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las escalas
@escala.route('/escala/v1/listar', methods=['GET'])
def listar_escalas():
    all_escalas = Escala.query.all()
    result = Escalas_schema.dump(all_escalas)

    data = {
        'message': 'Escalas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar una escala
@escala.route('/escala/v1/actualizar/<int:id_rango_escala>', methods=['PUT'])
def actualizar_escala(id_rango_escala):
    escala = Escala.query.get(id_rango_escala)
    if not escala:
        return jsonify({"error": "Escala no encontrada"}), 404

    id_tipo_test = request.json.get("id_tipo_test")
    puntaje_minimo = request.json.get("puntaje_minimo")
    puntaje_maximo = request.json.get("puntaje_maximo")
    descripcion = request.json.get("descripcion")

    escala.id_tipo_test = id_tipo_test
    escala.puntaje_minimo = puntaje_minimo
    escala.puntaje_maximo = puntaje_maximo
    escala.descripcion = descripcion

    db.session.commit()

    result = Escala_schema.dump(escala)

    data = {
        'message': 'Escala actualizada correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)

# Eliminar una escala
@escala.route('/escala/v1/eliminar/<int:id_rango_escala>', methods=['DELETE'])
def eliminar_escala(id_rango_escala):
    escala = Escala.query.get(id_rango_escala)
    if not escala:
        return jsonify({"error": f"Escala con id {id_rango_escala} no encontrada"}), 404

    db.session.delete(escala)
    db.session.commit()

    data = {
        'message': 'Escala eliminada correctamente',
        'status': 200,
        'data': {}
    }

    return make_response(jsonify(data), 200)
