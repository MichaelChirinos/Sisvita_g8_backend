from flask import Blueprint, request, jsonify, make_response
from model.paciente import Paciente
from utils.db import db
from schemas.paciente import paciente_schema, pacientes_schema

paciente = Blueprint('paciente', __name__)


@paciente.route('/paciente/v1', methods=['POST'])
def addPaciente():
    id_paciente = request.json.get("id_paciente")
    id_persona = request.json.get("id_persona")
    fecha_registro = request.json.get("fecha_registro")
    
    paciente = Paciente(id_paciente, id_persona, fecha_registro )
    db.session.add(paciente)
    db.session.commit()

    result = paciente_schema.dump(paciente)

    data = {
        'message': 'Paciente creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@paciente.route('/paciente/v1/listar', methods=['GET'])
def getPacientes():
    pacientes = Paciente.query.all()
    result = pacientes_schema.dump(pacientes)

    data = {
        'message': 'Pacientes recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@paciente.route('/paciente/v1/<int:id>', methods=['GET'])
def getOne(id):
    paciente = Paciente.query.get(id)

    if not paciente:
        data = {
            'message': 'Paciente no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = paciente_schema.dump(paciente)
    data = {
        'message': 'Paciente recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)


@paciente.route('/paciente/v1/<int:id>', methods=['PUT'])
def updatePaciente(id):
    nuevo_paciente = Paciente.query.get(id)

    if not nuevo_paciente:
        data = {
            'message': 'Paciente no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    id_paciente = request.json.get("id_paciente")
    id_persona = request.json.get("id_persona")
    fecha_registro = request.json.get("colegiado")

    paciente.id_paciente = id_paciente
    paciente.id_persona = id_persona
    paciente.fecha_registro = fecha_registro

    db.session.commit()

    result = paciente_schema.dump(nuevo_paciente)

    data = {
        'message': 'Estudiante actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@paciente.route('/estudiante/v1/<int:id>', methods=['DELETE'])
def deleteOne(id):

    paciente = Paciente.query.get(id)

    if not paciente:
        data = {
            'message': 'Paciente no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    db.session.delete(paciente)
    db.session.commit()

    data = {
        'message': 'Paciente eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)