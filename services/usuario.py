from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from model.usuario import Usuario
from model.persona import Persona 
from model.paciente import Paciente
from model.especialista import Especialista
from utils.db import db
from schemas.usuario import usuario_schema,usuarios_schema
from schemas.persona import PersonaSchema
import bcrypt

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/usuario/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-back'
    return jsonify(result)

# Crear un nuevo usuario
@usuario_bp.route('/usuario/v1/agregar', methods=['POST'])
def crear_usuario():
    body = request.get_json()
    id_usuario = request.json.get("id_usuario")
    id_persona = request.json.get("id_persona")
    correo = body.get("correo")
    clave = body.get("clave")
    is_admin = body.get("is_admin")

    # Hashing de la contraseña
    hashed_clave = bcrypt.hashpw(clave.encode('utf-8'), bcrypt.gensalt())

    usuario = Usuario(
        id_usuario=id_usuario,
        id_persona=id_persona,
        correo=correo,
        clave=hashed_clave.decode('utf-8'),  # Almacenar como cadena
        is_admin=is_admin
    )

    db.session.add(usuario)
    db.session.commit()

    result = usuario_schema.dump(usuario)

    data = {
        'message': 'Usuario creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Listar todos los usuarios
@usuario_bp.route('/usuario/v1/listar', methods=['GET'])
def listar_usuarios():
    all_users = Usuario.query.all()
    result = usuarios_schema.dump(all_users)

    data = {
        'message': 'Usuarios recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar un usuario por su ID
@usuario_bp.route('/usuario/v1/actualizar', methods=['POST'])
def actualizar_usuario():
    body = request.get_json()
    id_usuario = body.get('id_usuario')
    correo = body.get("correo")
    clave = body.get("clave")
    is_admin = body.get("is_admin")

    usuario = Usuario.query.get(id_usuario)

    if usuario is None:
        return jsonify({"error": f"Usuario con id {id_usuario} no encontrado"}), 404

    usuario.correo = correo
    usuario.is_admin = is_admin

    # Actualizar la contraseña con hashing
    if clave:
        hashed_clave = bcrypt.hashpw(clave.encode('utf-8'), bcrypt.gensalt())
        usuario.clave = hashed_clave.decode('utf-8')

    db.session.commit()

    result = usuario_schema.dump(usuario)

    data = {
        'message': 'Usuario actualizado correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)


# Eliminar un usuario por su ID
@usuario_bp.route('/usuario/v1/eliminar', methods=['DELETE'])
def eliminar_usuario():
    result = {}
    body = request.get_json()
    id_usuario = body.get('id_usuario')

    if id_usuario is None:
        return jsonify({"error": "Missing 'id_usuario' in request body"}), 400

    usuario = Usuario.query.get(id_usuario)

    if usuario is None:
        return jsonify({"error": f"Persona with id_persona {id_usuario} not found"}), 404

    db.session.delete(usuario)
    db.session.commit()

    result["data"] = {}
    result["status_code"] = 200
    result["msg"] = "Se elimino la persona sin inconvenientes"

    return jsonify(result), 200

# Login de usuario para paciente
@usuario_bp.route('/usuario/v1/login/paciente', methods=['POST'])
def login_paciente():
    body = request.get_json()
    correo = body.get('correo')
    clave = body.get('clave')

    if not correo or not clave:
        return make_response(jsonify({"message": "Faltan el correo o la clave"}), 400)

    usuario = Usuario.query.filter_by(correo=correo).first()

    if not usuario or not bcrypt.checkpw(clave.encode('utf-8'), usuario.clave.encode('utf-8')):
        return make_response(jsonify({"message": "Correo o clave incorrecta"}), 401)

    # Verificar si el usuario está asociado con un paciente
    paciente = Paciente.query.filter_by(id_persona=usuario.id_persona).first()
    if not paciente:
        return make_response(jsonify({"message": "El usuario no está registrado como paciente"}), 403)

    persona = usuario.persona

    access_token = create_access_token(identity=usuario.id_usuario, additional_claims={
        'correo': usuario.correo,
        'id_persona': persona.id_persona,
        'id_paciente': paciente.id_paciente,  # Incluye id_paciente en las claims
        'nombre': persona.nombre,
        'apellido_paterno': persona.apellido_paterno,
        'apellido_materno': persona.apellido_materno,
        'documento': persona.documento,
        'telefono': persona.telefono,
        'fecha_nacimiento': persona.fecha_nacimiento,
        'ubigeo' : persona.ubigeo
    })

    result = usuario_schema.dump(usuario)
    persona_schema = PersonaSchema()
    persona_data = persona_schema.dump(persona)

    data = {
        'message': 'Login exitoso',
        'status': 200,
        'data': {
            'usuario': result,
            'persona': persona_data,
            'access_token': access_token
        }
    }

    return make_response(jsonify(data), 200)

# Login de usuario para especialista
@usuario_bp.route('/usuario/v1/login/especialista', methods=['POST'])
def login_especialista():
    body = request.get_json()
    correo = body.get('correo')
    clave = body.get('clave')

    if not correo or not clave:
        return make_response(jsonify({"message": "Faltan el correo o la clave"}), 400)

    usuario = Usuario.query.filter_by(correo=correo).first()

    if not usuario or not bcrypt.checkpw(clave.encode('utf-8'), usuario.clave.encode('utf-8')):
        return make_response(jsonify({"message": "Correo o clave incorrecta"}), 401)

    # Verificar si el usuario está asociado con un especialista
    especialista = Especialista.query.filter_by(id_persona=usuario.id_persona).first()
    if not especialista:
        return make_response(jsonify({"message": "El usuario no está registrado como especialista"}), 403)

    persona = usuario.persona

    access_token = create_access_token(identity=usuario.id_usuario, additional_claims={
        'correo': usuario.correo,
        'id_persona': persona.id_persona,
        'id_especialista': especialista.id_especialista,
        'nombre': persona.nombre,
        'apellido_paterno': persona.apellido_paterno,
        'apellido_materno': persona.apellido_materno,
        'documento': persona.documento,
        'telefono': persona.telefono,
        'fecha_nacimiento': persona.fecha_nacimiento
    })

    result = usuario_schema.dump(usuario)
    persona_schema = PersonaSchema()  
    persona_data = persona_schema.dump(persona)

    data = {
        'message': 'Login exitoso',
        'status': 200,
        'data': {
            'usuario': result,
            'persona': persona_data,
            'access_token': access_token
        }
    }

    return make_response(jsonify(data), 200)