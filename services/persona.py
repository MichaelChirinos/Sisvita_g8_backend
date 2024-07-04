from flask import Blueprint, request, jsonify, make_response
from model.persona import Persona
from utils.db import db
from schemas.persona import persona_schema, personas_schema

persona_bp = Blueprint('persona', __name__)

@persona_bp.route('/persona/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-back'
    return jsonify(result)

# Listar todas las personas
@persona_bp.route('/persona/v1/listar', methods=['GET'])
def listar_personas():
    all_personas = Persona.query.all()
    result = personas_schema.dump(all_personas)

    data = {
        'message': 'Personas recuperadas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Crear una nueva persona
@persona_bp.route('/persona/v1/agregar', methods=['POST'])
def crear_persona():
    body = request.get_json()
    id_persona = body.get("id_persona")
    nombre = body.get('nombre')
    apellido_paterno = body.get("apellido_paterno")
    apellido_materno = body.get("apellido_materno")
    tipo_documento = body.get("tipo_documento")
    documento = body.get("documento")
    telefono = body.get("telefono")
    fecha_nacimiento = body.get("fecha_nacimiento")
    ubigeo = body.get("ubigeo")

    persona = Persona(
        id_persona=id_persona,
        nombre=nombre,
        apellido_paterno=apellido_paterno,
        apellido_materno=apellido_materno,
        tipo_documento=tipo_documento,
        documento=documento,
        telefono=telefono,
        fecha_nacimiento=fecha_nacimiento,
        ubigeo=ubigeo
    )

    db.session.add(persona)
    db.session.commit()

    result = persona_schema.dump(persona)

    data = {
        'message': 'Persona creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Actualizar una persona por su ID
@persona_bp.route('/persona/v1/actualizar', methods=['POST'])
def actualizar_persona():
    body = request.get_json()
    id_persona = body.get('id_persona')
    nombre = body.get('nombre')
    apellido_paterno = body.get("apellido_paterno")
    apellido_materno = body.get("apellido_materno")
    documento = body.get("documento")
    telefono = body.get("telefono")
    ubigeo = body.get("ubigeo")

    persona = Persona.query.get(id_persona)

    if persona is None:
        return jsonify({"error": f"Persona con id_persona {id_persona} no encontrada"}), 404

    persona.nombre = nombre
    persona.apellido_paterno = apellido_paterno
    persona.apellido_materno = apellido_materno
    persona.documento = documento
    persona.telefono = telefono
    persona.ubigeo = ubigeo

    db.session.commit()

    result = persona_schema.dump(persona)
    
    data = {
        'message': 'Persona actualizada correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)

# Eliminar una persona por su ID
@persona_bp.route('/persona/v1/eliminar', methods=['DELETE'])
def eliminar_persona():
    result = {}
    body = request.get_json()
    id_persona = body.get('id_persona')

    if id_persona is None:
        return jsonify({"error": "Missing 'id_persona' in request body"}), 400

    persona = Persona.query.get(id_persona)

    if persona is None:
        return jsonify({"error": f"Persona con id_persona {id_persona} no encontrada"}), 404

    db.session.delete(persona)
    db.session.commit()

    result["data"] = {}
    result["status_code"] = 200
    result["msg"] = "Se eliminó la persona sin inconvenientes"

    return jsonify(result), 200
