from flask import Blueprint, request, jsonify, make_response
from model.tratamiento import Tratamiento
from utils.db import db
from schemas.tratamiento import Tratamiento_schema, Tratamientos_schema

tratamiento = Blueprint('tratamiento', __name__)

# Obtener mensaje de prueba
@tratamiento.route('/tratamiento/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-back'
    return jsonify(result)

# Crear un nuevo tipo de test
@tratamiento.route('/tratamiento/v1/agregar', methods=['POST'])
def crear_tratamiento():
    descripcion = request.json.get("descripcion")

    tratamiento = Tratamiento(
        id_tratamiento=None,  # SQLAlchemy manejará el autoincremento
        descripcion=descripcion
    )

    db.session.add(tratamiento)
    db.session.commit()

    result = Tratamiento_schema.dump(tratamiento)
    data = {
        'message': 'Tratamiento creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todos los tipos de test
@tratamiento.route('/tratamiento/v1/listar', methods=['GET'])
def listar_tratamiento():
    all_tratamiento = Tratamiento.query.all()
    result = []
    for tratamiento in all_tratamiento:
        result.append({
            'id_tratamiento': tratamiento.id_tratamiento,
            'descripcion': tratamiento.descripcion
        })

    data = {
        'message': 'Tratamientos recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)


# Actualizar un tipo de test
@tratamiento.route('/tratamiento/v1/actualizar/<int:id_tratamiento>', methods=['PUT'])
def actualizar_tratamiento(id_tratamiento):
    tratamiento = Tratamiento.query.get(id_tratamiento)
    if not tratamiento:
        return jsonify({"error": "Tratamiento no encontrado"}), 404

    descripcion = request.json.get("descripcion")

    tratamiento.descripcion = descripcion

    db.session.commit()

    result = Tratamiento_schema.dump(tratamiento)

    data = {
        'message': 'Tipo de test actualizado correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)

# Eliminar un tipo de test
@tratamiento.route('/tratamiento/v1/eliminar/<int:id_tratamiento>', methods=['DELETE'])
def eliminar_tratamiento(id_tratamiento):
    tratamiento = Tratamiento.query.get(id_tratamiento)
    if not tratamiento:
        return jsonify({"error": f"Tipo de test con id {id_tratamiento} no encontrado"}), 404

    db.session.delete(tratamiento)
    db.session.commit()

    data = {
        'message': 'Tipo de test eliminado correctamente',
        'status': 200,
        'data': {}
    }

    return make_response(jsonify(data), 200)
