from flask import Blueprint, request, jsonify, make_response
from model.notificacion import Notificacion
from utils.db import db
from schemas.notificacion import notificacion_schema, notificaciones_schema

notificacion= Blueprint('notificacion', __name__)

@notificacion.route('/notificacion/v1', methods=['POST'])
def addNotificacion():
    id_notificacion = request.json.get("id_notificacion")
    id_persona = request.json.get("id_persona")
    tipo_mensaje = request.json.get("tipo_mensaje")
    mensaje = request.json.get("mensaje")
    
    nuevo_notificacion = Notificacion(id_notificacion, id_persona ,tipo_mensaje,mensaje)
    
    db.session.add(nuevo_notificacion)
    db.session.commit()
    
    result = notificacion_schema.dump(nuevo_notificacion)
    
    data = {
        'message': 'Notificacion creado correctamente',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(data), 201)

@notificacion.route('/notificacion/v1/listar', methods=['GET'])
def getNotificacion():
    all_notificaciones = Notificacion.query.all()
    result = notificaciones_schema.dump(all_notificaciones)
    
    data = {
        'message': 'Notificaciones recuperados correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@notificacion.route('/notificacion/v1/<int:id>', methods=['PUT'])
def updateNotificaion(id):

    notificacion = Notificacion.query.get(id)

    if not notificacion:
        data = {
            'message': 'Notificacion no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    id_notificacion = request.json.get("id_notificacion")
    id_persona = request.json.get("id_persona")
    tipo_mensaje = request.json.get("tipo_mensaje")
    mensaje = request.json.get("mensaje")

    notificacion.id_notificacion = id_notificacion
    notificacion.id_persona = id_persona
    notificacion.tipo_mensaje = tipo_mensaje
    notificacion.mensaje = mensaje

    db.session.commit()

    result = notificacion_schema.dump(notificacion)

    data = {
        'message': 'Notificacion actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@notificacion.route('/notificacion/v1/<int:id>', methods=['DELETE'])
def deleteOne(id):
    notificacion = Notificacion.query.get(id)

    if not notificacion:
        data = {
            'message': 'Notificacion no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    db.session.delete(notificacion)
    db.session.commit()

    data = {
        'message': 'Notificacion eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)