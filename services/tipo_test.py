from flask import Blueprint, request, jsonify, make_response
from model.tipo_test import TipoTest
from utils.db import db
from schemas.tipo_test import TipoTest_schema, TipoTests_schema

tipo_test = Blueprint('tipo_test', __name__)

# Obtener mensaje de prueba
@tipo_test.route('/tipo_test/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-back'
    return jsonify(result)

# Crear un nuevo tipo de test
@tipo_test.route('/tipo_test/v1/agregar', methods=['POST'])
def crear_tipo_test():
    nombre = request.json.get("nombre")
    descripcion = request.json.get("descripcion")

    tipo_test = TipoTest(
        id_tipo_test=None,  # SQLAlchemy manejará el autoincremento
        nombre=nombre,
        descripcion=descripcion
    )

    db.session.add(tipo_test)
    db.session.commit()

    result = TipoTest_schema.dump(tipo_test)

    data = {
        'message': 'Tipo de test creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todos los tipos de test
@tipo_test.route('/tipo_test/v1/listar', methods=['GET'])
def listar_tipo_test():
    all_tipo_test = TipoTest.query.all()
    result = TipoTests_schema.dump(all_tipo_test)

    data = {
        'message': 'Tipos de test recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar un tipo de test
@tipo_test.route('/tipo_test/v1/actualizar/<int:id_tipo_test>', methods=['PUT'])
def actualizar_tipo_test(id_tipo_test):
    tipo_test = TipoTest.query.get(id_tipo_test)
    if not tipo_test:
        return jsonify({"error": "Tipo de test no encontrado"}), 404

    nombre = request.json.get("nombre")
    descripcion = request.json.get("descripcion")

    tipo_test.nombre = nombre
    tipo_test.descripcion = descripcion

    db.session.commit()

    result = TipoTest_schema.dump(tipo_test)

    data = {
        'message': 'Tipo de test actualizado correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)

# Eliminar un tipo de test
@tipo_test.route('/tipo_test/v1/eliminar/<int:id_tipo_test>', methods=['DELETE'])
def eliminar_tipo_test(id_tipo_test):
    tipo_test = TipoTest.query.get(id_tipo_test)
    if not tipo_test:
        return jsonify({"error": f"Tipo de test con id {id_tipo_test} no encontrado"}), 404

    db.session.delete(tipo_test)
    db.session.commit()

    data = {
        'message': 'Tipo de test eliminado correctamente',
        'status': 200,
        'data': {}
    }

    return make_response(jsonify(data), 200)
