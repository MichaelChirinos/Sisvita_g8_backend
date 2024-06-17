from flask import Blueprint, request, jsonify, make_response
from model.respuestausuario import RespuestaUsuario
from utils.db import db

respuestausuario_bp = Blueprint('respuestausuario', __name__)

# Diccionario para convertir las respuestas
conversion = {'Casi ningún día': 0, 'Ocasionalmente': 1, 'Frecuentemente': 2, 'Casi todos los días': 3}

@respuestausuario_bp.route('/respuesta-usuario/v1/agregar/<int:id_usuario>', methods=['POST'])
def registrar_respuesta_usuario(id_usuario):
    body = request.get_json()
    respuestas = body.get('respuestas')  # Se espera una lista de respuestas

    if not id_usuario or not respuestas or len(respuestas) != 7:
        return make_response(jsonify({'message': 'Faltan contestar preguntas o longitud de respuestas incorrecta', 'status': 400}), 400)

    # Convertir las respuestas de 'A', 'B', 'C', 'D' a 0, 1, 2, 3
    respuestas_convertidas = [conversion[respuesta] for respuesta in respuestas]

    # Crear y guardar la respuesta del usuario
    respuestausuario = RespuestaUsuario(
        id_usuario=id_usuario,
        respuesta_1=respuestas[0],  # Guardamos la respuesta original ('A', 'B', 'C', 'D')
        respuesta_2=respuestas[1],
        respuesta_3=respuestas[2],
        respuesta_4=respuestas[3],
        respuesta_5=respuestas[4],
        respuesta_6=respuestas[5],
        respuesta_7=respuestas[6]
    )

    # Calcular la suma de las respuestas convertidas y asignarla a la columna suma_respuestas
    respuestausuario.suma_respuestas = sum(respuestas_convertidas)

    db.session.add(respuestausuario)
    db.session.commit()

    result = {
        'message': 'Respuestas de usuario registradas correctamente', 
        'status': 201,
        'suma_respuestas': respuestausuario.suma_respuestas
    }

    return make_response(jsonify(result), 201)
