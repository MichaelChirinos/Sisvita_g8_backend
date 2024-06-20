from flask import Blueprint, request, jsonify, make_response
from model.evaluacion import Evaluacion
from model.test import Test
from utils.db import db
from schemas.evaluacion import Evaluacion_schema, Evaluaciones_schema

evaluacion = Blueprint('evaluacion', __name__)

# Obtener mensaje de prueba
@evaluacion.route('/evaluacion/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-back'
    return jsonify(result)

# Crear una nueva evaluacion
@evaluacion.route('/evaluacion/v1/agregar', methods=['POST'])
def crear_evaluacion():
    id_historia_clinica = request.json.get("id_historia_clinica")
    id_test = request.json.get("id_test")

    # Obtener el test y calcular la suma de las respuestas
    test = Test.query.get(id_test)
    if not test:
        return jsonify({"error": "Test no encontrado"}), 404

    suma_respuestas = sum(map(int, test.respuestas))

    evaluacion = Evaluacion(
        id_historia_clinica=id_historia_clinica,
        id_test=id_test,
        suma_respuestas=suma_respuestas
    )

    db.session.add(evaluacion)
    db.session.commit()

    result = Evaluacion_schema.dump(evaluacion)

    data = {
        'message': 'Evaluación creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las evaluaciones
@evaluacion.route('/evaluacion/v1/listar', methods=['GET'])
def listar_evaluaciones():
    all_evaluaciones = Evaluacion.query.all()
    result = Evaluaciones_schema.dump(all_evaluaciones)

    data = {
        'message': 'Evaluaciones recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar una evaluación
@evaluacion.route('/evaluacion/v1/actualizar/<int:id_evaluacion>', methods=['PUT'])
def actualizar_evaluacion(id_evaluacion):
    evaluacion = Evaluacion.query.get(id_evaluacion)
    if not evaluacion:
        return jsonify({"error": "Evaluación no encontrada"}), 404

    id_historia_clinica = request.json.get("id_historia_clinica")
    id_test = request.json.get("id_test")

    # Obtener el test y calcular la suma de las respuestas
    test = Test.query.get(id_test)
    if not test:
        return jsonify({"error": "Test no encontrado"}), 404

    suma_respuestas = sum(map(int, test.respuestas))

    evaluacion.id_historia_clinica = id_historia_clinica
    evaluacion.id_test = id_test
    evaluacion.suma_respuestas = suma_respuestas

    db.session.commit()

    result = Evaluacion_schema.dump(evaluacion)

    data = {
        'message': 'Evaluación actualizada correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)

# Eliminar una evaluación
@evaluacion.route('/evaluacion/v1/eliminar/<int:id_evaluacion>', methods=['DELETE'])
def eliminar_evaluacion(id_evaluacion):
    evaluacion = Evaluacion.query.get(id_evaluacion)
    if not evaluacion:
        return jsonify({"error": f"Evaluación con id {id_evaluacion} no encontrada"}), 404

    db.session.delete(evaluacion)
    db.session.commit()

    data = {
        'message': 'Evaluación eliminada correctamente',
        'status': 200,
        'data': {}
    }

    return make_response(jsonify(data), 200)
