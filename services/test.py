from flask import Blueprint, request, jsonify, make_response
from model.test import Test
from utils.db import db
from schemas.test import Test_schema, Tests_schema

test = Blueprint('test', __name__)

# Obtener mensaje de prueba
@test.route('/test/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-back'
    return jsonify(result)

# Crear un nuevo test
@test.route('/test/v1/agregar', methods=['POST'])
def crear_test():
    id_tipo_test = request.json.get("id_tipo_test")
    fecha_realizacion = request.json.get("fecha_realizacion")
    respuestas = request.json.get("respuestas")

    test = Test(
        id_tipo_test=id_tipo_test,
        fecha_realizacion=fecha_realizacion,
        respuestas=respuestas
    )

    db.session.add(test)
    db.session.commit()

    result = Test_schema.dump(test)

    data = {
        'message': 'Test creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todos los tests
@test.route('/test/v1/listar', methods=['GET'])
def listar_tests():
    all_tests = Test.query.all()
    result = Tests_schema.dump(all_tests)

    data = {
        'message': 'Tests recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar un test
@test.route('/test/v1/actualizar/<int:id_test>', methods=['PUT'])
def actualizar_test(id_test):
    test = Test.query.get(id_test)
    if not test:
        return jsonify({"error": "Test no encontrado"}), 404

    id_tipo_test = request.json.get("id_tipo_test")
    fecha_realizacion = request.json.get("fecha_realizacion")
    respuestas = request.json.get("respuestas")

    test.id_tipo_test = id_tipo_test
    test.fecha_realizacion = fecha_realizacion
    test.respuestas = respuestas

    db.session.commit()

    result = Test_schema.dump(test)

    data = {
        'message': 'Test actualizado correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)

# Eliminar un test
@test.route('/test/v1/eliminar/<int:id_test>', methods=['DELETE'])
def eliminar_test(id_test):
    test = Test.query.get(id_test)
    if not test:
        return jsonify({"error": f"Test con id {id_test} no encontrado"}), 404

    db.session.delete(test)
    db.session.commit()

    data = {
        'message': 'Test eliminado correctamente',
        'status': 200,
        'data': {}
    }

    return make_response(jsonify(data), 200)
