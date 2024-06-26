from flask import Blueprint, request, jsonify, make_response
from model.especialista import Especialista
from utils.db import db
from schemas.especialista import especialista_schema, especialistas_schema

especialista= Blueprint('especialista', __name__)

@especialista.route('/especialista/v1', methods=['POST'])
def crear_especialista():
    id_especialista = request.json.get("id_especialista")
    id_persona = request.json.get("id_persona")
    colegiatura = request.json.get("colegiatura")

    nuevo_especialista = Especialista(id_especialista,id_persona,colegiatura)

    db.session.add(nuevo_especialista)
    db.session.commit()

    result = especialista_schema.dump(nuevo_especialista)

    data = {
        'message': 'Especialista creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@especialista.route('/especialista/v1/listar', methods=['GET'])
def getEspecialista():
    especialistas = Especialista.query.all()
    result = especialistas_schema.dump(especialistas)
    
    data = {
        'message': 'Especialistas recuperados correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@especialista.route('/especialista/v1/<int:id>', methods=['GET'])
def getOne(id):
    especialista = Especialista.query.get(id)

    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = especialista_schema.dump(especialista)
    data = {
        'message': 'Paciente recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@especialista.route('/especialista/v1/<int:id>', methods=['PUT'])
def updateOne(id):

    especialista = Especialista.query.get(id)

    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    id_especialista = request.json.get("id_especialista")
    id_persona = request.json.get("id_persona")
    colegiatura = request.json.get("colegiatura")

    especialista.id_especialista = id_especialista
    especialista.id_persona = id_persona
    especialista.colegiatura = colegiatura

    db.session.commit()

    result = especialista_schema.dump(especialista)

    data = {
        'message': 'Especialista actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@especialista.route('/especialista/v1/<int:id>', methods=['DELETE'])
def deleteOne(id):
    especialista = Especialista.query.get(id)

    if not especialista:
        data = {
            'message': 'Especialista no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    db.session.delete(especialista)
    db.session.commit()

    data = {
        'message': 'Especialista eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)