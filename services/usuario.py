from flask import Blueprint, request, jsonify, make_response
from model.usuario import Usuario
from utils.db import db
from schemas.usuario import usuario_schema, usuarios_schema

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
    nombre = body.get('nombre')
    apellido = body.get("apellido")
    dni = body.get("dni")
    telefono = body.get("telefono")
    correo = body.get("correo")
    clave = body.get("clave")
    fecha_nacimiento = body.get("fecha_nacimiento")
    sexo = body.get("sexo")

    usuario = Usuario(
        nombre=nombre,
        apellido=apellido,
        dni=dni,
        telefono=telefono,
        correo=correo,
        clave=clave,  
        fecha_nacimiento=fecha_nacimiento,
        sexo=sexo
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

# Obtener un usuario por su ID
@usuario_bp.route('/usuario/v1/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    result = usuario_schema.dump(usuario)

    data = {
        'message': 'Usuario recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar un usuario por su ID
@usuario_bp.route('/usuario/v1/actualizar', methods=['POST'])
def actualizar_usuario():
    body = request.get_json()
    id_usuario = body.get('id_usuario')
    nombre = body.get('nombre')
    apellido = body.get("apellido")
    dni = body.get("dni")
    telefono = body.get("telefono")
    correo = body.get("correo")
    clave = body.get("clave")
    fecha_nacimiento = body.get("fecha_nacimiento")
    sexo = body.get("sexo")

    usuario = Usuario.query.get(id_usuario)

    if usuario is None:
        return jsonify({"error": f"Persona with id_persona {id_usuario} not found"}), 404

    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.dni = dni
    usuario.telefono = telefono
    usuario.correo = correo

    # Actualizar la contraseña sin hashing
    if clave:
        usuario.clave = clave

    usuario.fecha_nacimiento = fecha_nacimiento
    usuario.sexo = sexo

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

# Login de usuario
@usuario_bp.route('/usuario/v1/login-persona', methods=['POST'])
def login():
    body = request.get_json()
    correo = body.get('correo')
    clave = body.get('clave')

    if not correo or not clave:
        return make_response(jsonify({"message": "Faltan el correo o la clave"}), 400)

    usuario = Usuario.query.filter_by(correo=correo).first()

    # Comparar la contraseña en texto claro
    if not usuario or usuario.clave != clave:
        return make_response(jsonify({"message": "Correo o clave incorrecta"}), 401)

    # Aquí se devuelve el id_usuario junto con el mensaje de éxito
    result = usuario_schema.dump(usuario)

    data = {
        'message': 'Login exitoso',
        'status': 200,
        'data': {
            'id_usuario': usuario.id_usuario,
            'usuario': result
        }
    }

    return make_response(jsonify(data), 200)