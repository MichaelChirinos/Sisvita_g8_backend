from flask import Blueprint, request, jsonify, make_response
from model.semaforo import Semaforo
from utils.db import db
from schemas.semaforo import Semaforo_schema, Semaforos_schema


semaforo = Blueprint('semaforo', __name__)


# Obtener mensaje de prueba
@semaforo.route('/semaforo/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-back'
    return jsonify(result)


# Crear una nueva alternativa
@semaforo.route('/semaforo/v1/agregar', methods=['POST'])
def crear_semaforo():
    id_rango_escala = request.json.get("id_rango_escala")
    color = request.json.get("color")


    semaforo = Semaforo(
        id_semaforo=None,  
        id_rango_escala=id_rango_escala,
        color=color
    )


    db.session.add(semaforo)
    db.session.commit()


    result = Semaforo_schema.dump(semaforo)


    data = {
        'message': 'semaforo creado correctamente',
        'status': 201,
        'data': result
    }


    return make_response(jsonify(data), 201)


# Listar todas los semaforos
@semaforo.route('/semaforo/v1/listar/<int:id_rango_escala>', methods=['GET'])
def listar_semaforos(id_rango_escala):
    all_semaforos = Semaforo.query.filter_by(id_rango_escala=id_rango_escala).all()
    result = Semaforos_schema.dump(all_semaforos)


    data = {
        'message': 'semaforos recuperados correctamente',
        'status': 200,
        'data': result
    }


    return make_response(jsonify(data), 200)


# Actualizar una alternativa
@semaforo.route('/semaforo/v1/actualizar/<int:id_semaforo>', methods=['PUT'])
def actualizar_semaforo(id_semaforo):
    semaforo = Semaforo.query.get(id_semaforo)
    if not semaforo:
        return jsonify({"error": "semaforo no encontrada"}), 404


    id_rango_escala = request.json.get("id_rango_escala")
    color = request.json.get("color")


    semaforo.id_rango_escala = id_rango_escala
    semaforo.color = color


    db.session.commit()


    result = Semaforo_schema.dump(semaforo)


    data = {
        'message': 'semaforo actualizada correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)


# Eliminar una semaforo
@semaforo.route('/semaforo/v1/eliminar/<int:id_semaforo>', methods=['DELETE'])
def eliminar_semaforo(id_semaforo):
    semaforo = Semaforo.query.get(id_semaforo)
    if not semaforo:
        return jsonify({"error": f"semaforo con id {id_semaforo} no encontrada"}), 404


    db.session.delete(semaforo)
    db.session.commit()


    data = {
        'message': 'semaforo eliminada correctamente',
        'status': 200,
        'data': {}
    }


    return make_response(jsonify(data), 200)