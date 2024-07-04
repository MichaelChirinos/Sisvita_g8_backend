from flask import Blueprint, request, jsonify, make_response
from model.test import Test
from model.escala import Escala 
from model.tipo_test import TipoTest
from model.paciente import Paciente
from model.persona import Persona
from model.semaforo import Semaforo
from model.tratamiento import Tratamiento
from model.medida import Medida
from utils.db import db
from schemas.test import Test_schema, Tests_schema

test = Blueprint('test', __name__)

# Obtener mensaje de prueba
@test.route('/test/v1', methods=['GET'])
def getMensaje():
    result = {"data": 'flask-crud-back'}
    return jsonify(result)

# Crear un nuevo test
@test.route('/test/v1/agregar', methods=['POST'])
def crear_test():
    id_paciente = request.json.get("id_paciente")
    id_tipo_test = request.json.get("id_tipo_test")
    fecha_realizacion = request.json.get("fecha_realizacion")
    respuestas = request.json.get("respuestas")
    suma_respuestas = sum(respuestas)
    # Nuevos campos
    id_tratamiento = request.json.get("id_tratamiento")
    id_medida = request.json.get("id_medida")
    observacion = request.json.get("observacion")
    confirmar = request.json.get("confirmar", False)

    # Obtener el rango de escala basado en suma_respuestas y id_tipo_test
    escala = Escala.query.filter(
        Escala.id_tipo_test == id_tipo_test,
        Escala.puntaje_minimo <= suma_respuestas,
        Escala.puntaje_maximo >= suma_respuestas
    ).first()
    id_rango_escala = escala.id_rango_escala if escala else None

    test = Test(
        id_paciente=id_paciente,
        id_tipo_test=id_tipo_test,
        id_rango_escala=id_rango_escala,
        fecha_realizacion=fecha_realizacion,
        respuestas=respuestas,
        suma_respuestas=suma_respuestas,
        id_tratamiento=id_tratamiento,
        id_medida = id_medida,
        observacion=observacion,
        confirmar=confirmar
    )

    db.session.add(test)
    db.session.commit()

    result = Test_schema.dump(test)

    data = {
        'message': 'Test creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)


# Listar todos los tests
@test.route('/test/v1/listar', methods=['GET'])
def listar_tests():
    tests = Test.query.all()
    
    result = []
    color_translation = {
        'rojo': 'red',
        'verde': 'green',
        'amarillo': 'yellow',
        'gris': 'gray'  # Por defecto
    }
    for t in tests:
        tipo_test = TipoTest.query.get(t.id_tipo_test)
        paciente = Paciente.query.get(t.id_paciente)
        persona = Persona.query.get(paciente.id_persona) if paciente else None
        escala = Escala.query.get(t.id_rango_escala)
        semaforo = Semaforo.query.filter_by(id_rango_escala=t.id_rango_escala).first()
        color = semaforo.color if semaforo else 'gris'
        color_english = color_translation.get(color, 'gray')
        tratamiento = Tratamiento.query.get(t.id_tratamiento)
        medida = Medida.query.get(t.id_medida)
        nombre_completo = f"{persona.nombre} {persona.apellido_paterno} {persona.apellido_materno}" if persona else 'Desconocido'
        documento = persona.documento if persona else 'Desconocido'
        result.append({
            'id_test': t.id_test,
            'id_tipo_test': t.id_tipo_test,
            'nombre_paciente': nombre_completo,
            'documento_paciente': documento,
            'nombre_tipo_test': tipo_test.nombre if tipo_test else 'Desconocido',
            'fecha_realizacion': t.fecha_realizacion,
            'descripcion': escala.descripcion if escala else 'No disponible',
            'suma_respuestas': t.suma_respuestas,
            'color': color_english,
            'tratamiento': tratamiento.descripcion if tratamiento else 'No disponible',
            'medida' : medida.descripcion if medida else 'No disponible',
            'observacion': t.observacion,
            'confirmar': t.confirmar
        })
    
    data = {
        'message': 'Tests recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar un test
@test.route('/test/v1/actualizar/<int:id_test>', methods=['PUT'])
def actualizar_test(id_test):
    test = Test.query.get(id_test)
    if not test:
        return jsonify({"error": "Test no encontrado"}), 404


    # Nuevos campos
    id_tratamiento = request.json.get("id_tratamiento")
    id_medida = request.json.get("id_medida")
    observacion = request.json.get("observacion")
    confirmar = request.json.get("confirmar", False)
    

    test.id_tratamiento = id_tratamiento
    test.id_medida = id_medida
    test.observacion = observacion
    test.confirmar = confirmar

    db.session.commit()

    result = Test_schema.dump(test)

    data = {
        'message': 'Test actualizado correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)

# Eliminar un test
@test.route('/test/v1/eliminar/<int:id_test>', methods=['DELETE'])
def eliminar_test(id_test):
    test = Test.query.get(id_test)
    if not test:
        return jsonify({"error": f"Test con id {id_test} no encontrado"}), 404

    db.session.delete(test)
    db.session.commit()

    data = {
        'message': 'Test eliminado correctamente',
        'status': 200,
        'data': {}
    }

    return make_response(jsonify(data), 200)

@test.route('/test/v1/paciente/<int:id_paciente>', methods=['GET'])
def listar_tests_por_paciente(id_paciente):
    tests = Test.query.filter_by(id_paciente=id_paciente).all()
    
    result = []
    for t in tests:
        tipo_test = TipoTest.query.get(t.id_tipo_test)
        escala = Escala.query.get(t.id_rango_escala)
        tratamiento = Tratamiento.query.get(t.id_tratamiento)
        medida = Medida.query.get(t.id_medida)
        result.append({
            'id_test': t.id_test,
            'id_tipo_test': t.id_tipo_test,
            'nombre_tipo_test': tipo_test.nombre if tipo_test else 'Desconocido',
            'fecha_realizacion': t.fecha_realizacion,
            'descripcion': escala.descripcion if escala else 'No disponible',
            'suma_respuestas': t.suma_respuestas,
            'tratamiento': tratamiento.descripcion if tratamiento else 'No disponible',
            'medida' : medida.descripcion if medida else 'No disponible',
            'observacion': t.observacion,
            'confirmar': t.confirmar
        })
    
    data = {
        'message': 'Tests recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener detalle del test
@test.route('/test/v1/detalle/<int:id_test>', methods=['GET'])
def detalle_test(id_test):
    test = Test.query.filter_by(id_test=id_test).all()
    
    result = []
    for t in test:
        tipo_test = TipoTest.query.get(t.id_tipo_test)
        paciente = Paciente.query.get(t.id_paciente)
        persona = Persona.query.get(paciente.id_persona) if paciente else None
        escala = Escala.query.get(t.id_rango_escala)
        tratamiento = Tratamiento.query.get(t.id_tratamiento)
        medida = Medida.query.get(t.id_medida)
        documento = persona.documento if persona else 'Desconocido'
        nombre_completo = f"{persona.nombre} {persona.apellido_paterno} {persona.apellido_materno}" if persona else 'Desconocido'
        result.append({
            'id_test': t.id_test,
            'id_tipo_test': t.id_tipo_test,
            'nombre_paciente': nombre_completo,
            'documento_paciente': documento,
            'nombre_tipo_test': tipo_test.nombre if tipo_test else 'Desconocido',
            'fecha_realizacion': t.fecha_realizacion,
            'descripcion': escala.descripcion if escala else 'No disponible',
            'suma_respuestas': t.suma_respuestas,
            'tratamiento': tratamiento.descripcion if tratamiento else 'No disponible',
            'medida' : medida.descripcion if medida else 'No disponible',
            'observacion': t.observacion,
            'confirmar': t.confirmar
        })

    data = {
        'message': 'Detalle del test recuperado correctamente',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


# Confirmar un test
@test.route('/test/v1/confirmar/<int:id_test>', methods=['PUT'])
def confirmar_test(id_test):
    test = Test.query.get(id_test)
    if not test:
        return jsonify({"error": "Test no encontrado"}), 404

    # Actualizar el campo confirmar
    test.confirmar = True
    
    db.session.commit()

    result = Test_schema.dump(test)

    data = {
        'message': 'Test confirmado correctamente',
        'status': 202,
        'data': result
    }
    return make_response(jsonify(data), 202)

