from flask import Blueprint, request, jsonify, make_response
from model.respuestausuario2 import RespuestaUsuario2
from utils.db import db

respuestausuario2_bp = Blueprint('respuestausuario2', __name__)

# Diccionario para convertir las respuestas
conversion = {'Nunca': 0, 'A veces': 1, 'A menudo': 2, 'Siempre': 3}

@respuestausuario2_bp.route('/respuesta-usuario2/v1/agregar/<int:id_usuario>', methods=['POST'])
def registrar_respuesta_usuario2(id_usuario):
    body = request.get_json()
    respuestas2 = body.get('respuestas2')  # Se espera una lista de respuestas

    if not id_usuario or not respuestas2 or len(respuestas2) != 20:
        return make_response(jsonify({'message': 'Faltan contestar preguntas o longitud de respuestas incorrecta', 'status': 400}), 400)

    # Convertir las respuestas de 'A', 'B', 'C', 'D' a 0, 1, 2, 3
    respuestas_convertidas2 = [conversion[respuesta2] for respuesta2 in respuestas2]

    # Crear y guardar la respuesta del usuario
    respuestausuario2 = RespuestaUsuario2(
        id_usuario=id_usuario,
        respuesta_1=respuestas2[0],  # Guardamos la respuesta original ('A', 'B', 'C', 'D')
        respuesta_2=respuestas2[1],
        respuesta_3=respuestas2[2],
        respuesta_4=respuestas2[3],
        respuesta_5=respuestas2[4],
        respuesta_6=respuestas2[5],
        respuesta_7=respuestas2[6],
        respuesta_8=respuestas2[7],
        respuesta_9=respuestas2[8],
        respuesta_10=respuestas2[9],
        respuesta_11=respuestas2[10],
        respuesta_12=respuestas2[11],
        respuesta_13=respuestas2[12],
        respuesta_14=respuestas2[13],
        respuesta_15=respuestas2[14],
        respuesta_16=respuestas2[15],
        respuesta_17=respuestas2[16],
        respuesta_18=respuestas2[17],
        respuesta_19=respuestas2[18],
        respuesta_20=respuestas2[19]
    )

    # Calcular la suma de las respuestas convertidas y asignarla a la columna suma_respuestas
    respuestausuario2.suma_respuestas2 = sum(respuestas_convertidas2)

    db.session.add(respuestausuario2)
    db.session.commit()

    result = {
        'message': 'Respuestas de usuario registradas correctamente', 
        'status': 201,
        'suma_respuestas2': respuestausuario2.suma_respuestas2
    }

    return make_response(jsonify(result), 201)
