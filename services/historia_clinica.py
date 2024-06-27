from flask import Blueprint, request, jsonify, make_response
from model.historia_clinica import HistoriaClinica
from utils.db import db
from schemas.historia_clinica import HistoriaClinica_schema, HistoriaClinicas_schema

historia_clinica = Blueprint('historia_clinica', __name__)

@historia_clinica.route('/historia_clinica/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-back'
    return jsonify(result)

# Crear una nueva historia clinica
@historia_clinica.route('/historia_clinica/v1/agregar', methods=['POST'])
def crear_historia_clinica():
    id_historia_clinica = request.json.get("id_historia_clinica")
    id_paciente = request.json.get("id_paciente")
    id_especialista = request.json.get("id_especialista")
    fecha_consulta = request.json.get("fecha_consulta")

    historia_clinica = HistoriaClinica(
        id_historia_clinica,
        id_paciente,
        id_especialista,
        fecha_consulta
    )

    db.session.add(historia_clinica)
    db.session.commit()

    result = HistoriaClinica_schema.dump(historia_clinica)

    data = {
        'message': 'Historia clinica creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todas las historias clinicas
@historia_clinica.route('/historia_clinica/v1/listar', methods=['GET'])
def listar_historia_clinica():
    all_historia_clinica = HistoriaClinica.query.all()
    result = HistoriaClinicas_schema.dump(all_historia_clinica)

    data = {
        'message': 'Historias clinicas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar una Historia clinica 
@historia_clinica.route('/historia_clinica/v1/actualizar', methods=['PUT'])
def actualizar_historia_clinica():
    body = request.get_json()
    id_historia_clinica = body.get('id_historia_clinica')

    historia_clinica = HistoriaClinica.query.get(id_historia_clinica)
    if not historia_clinica:
        return jsonify({"error": "Historia clinica no encontrada"}), 404

    historia_clinica.id_paciente = body.get("id_paciente")
    historia_clinica.id_especialista = body.get("id_especialista")
    historia_clinica.fecha_consulta = body.get("fecha_consulta")
    
    db.session.commit()

    result = HistoriaClinica_schema.dump(historia_clinica)

    data = {
        'message': 'Historia clinica actualizada correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)

# Eliminar una Historia Clinica  
@historia_clinica.route('/historia_clinica/v1/eliminar', methods=['DELETE'])
def eliminar_historia_clinica():
    result = {}
    body = request.get_json()
    id_historia_clinica = body.get('id_historia_clinica')

    if id_historia_clinica is None:
        return jsonify({"error": "Falta 'id_historia_clinica' en el cuerpo de la solicitud"}), 400

    historia_clinica = HistoriaClinica.query.get(id_historia_clinica)

    if historia_clinica is None:
        return jsonify({"error": f"historia_clinica con id_historia_clinica {id_historia_clinica} no encontrada"}), 404

    db.session.delete(historia_clinica)
    db.session.commit()

    result["data"] = {}
    result["status_code"] = 200
    result["msg"] = "Se eliminó la historia_clinica sin inconvenientes"

    return jsonify(result), 200
