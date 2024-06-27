from flask import Blueprint, request, jsonify, make_response
from model.semaforo import Semaforo
from utils.db import db
from schemas.semaforo import Semaforo_schema, Semaforos_schema

<<<<<<< HEAD
semaforo = Blueprint('semaforo', __name__)

=======

semaforo = Blueprint('semaforo', __name__)


>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
# Obtener mensaje de prueba
@semaforo.route('/semaforo/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-back'
    return jsonify(result)

<<<<<<< HEAD
=======

>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
# Crear una nueva alternativa
@semaforo.route('/semaforo/v1/agregar', methods=['POST'])
def crear_semaforo():
    id_rango_escala = request.json.get("id_rango_escala")
    color = request.json.get("color")

<<<<<<< HEAD
=======

>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
    semaforo = Semaforo(
        id_semaforo=None,  
        id_rango_escala=id_rango_escala,
        color=color
    )

<<<<<<< HEAD
    db.session.add(semaforo)
    db.session.commit()

    result = Semaforo_schema.dump(semaforo)

=======

    db.session.add(semaforo)
    db.session.commit()


    result = Semaforo_schema.dump(semaforo)


>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
    data = {
        'message': 'semaforo creado correctamente',
        'status': 201,
        'data': result
    }

<<<<<<< HEAD
    return make_response(jsonify(data), 201)

=======

    return make_response(jsonify(data), 201)


>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
# Listar todas los semaforos
@semaforo.route('/semaforo/v1/listar/<int:id_rango_escala>', methods=['GET'])
def listar_semaforos(id_rango_escala):
    all_semaforos = Semaforo.query.filter_by(id_rango_escala=id_rango_escala).all()
    result = Semaforos_schema.dump(all_semaforos)

<<<<<<< HEAD
=======

>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
    data = {
        'message': 'semaforos recuperados correctamente',
        'status': 200,
        'data': result
    }

<<<<<<< HEAD
    return make_response(jsonify(data), 200)

=======

    return make_response(jsonify(data), 200)


>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
# Actualizar una alternativa
@semaforo.route('/semaforo/v1/actualizar/<int:id_semaforo>', methods=['PUT'])
def actualizar_semaforo(id_semaforo):
    semaforo = Semaforo.query.get(id_semaforo)
    if not semaforo:
        return jsonify({"error": "semaforo no encontrada"}), 404

<<<<<<< HEAD
    id_rango_escala = request.json.get("id_rango_escala")
    color = request.json.get("color") 
=======

    id_rango_escala = request.json.get("id_rango_escala")
    color = request.json.get("color")

>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291

    semaforo.id_rango_escala = id_rango_escala
    semaforo.color = color

<<<<<<< HEAD
    db.session.commit()

    result = Semaforo_schema.dump(semaforo)

=======

    db.session.commit()


    result = Semaforo_schema.dump(semaforo)


>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
    data = {
        'message': 'semaforo actualizada correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)

<<<<<<< HEAD
=======

>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
# Eliminar una semaforo
@semaforo.route('/semaforo/v1/eliminar/<int:id_semaforo>', methods=['DELETE'])
def eliminar_semaforo(id_semaforo):
    semaforo = Semaforo.query.get(id_semaforo)
    if not semaforo:
        return jsonify({"error": f"semaforo con id {id_semaforo} no encontrada"}), 404

<<<<<<< HEAD
    db.session.delete(semaforo)
    db.session.commit()

=======

    db.session.delete(semaforo)
    db.session.commit()


>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
    data = {
        'message': 'semaforo eliminada correctamente',
        'status': 200,
        'data': {}
    }

<<<<<<< HEAD
    return make_response(jsonify(data), 200)
=======

    return make_response(jsonify(data), 200)
>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
