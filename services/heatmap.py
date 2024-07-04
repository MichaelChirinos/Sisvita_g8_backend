from flask import Blueprint, jsonify, make_response
from model.test import Test
from model.paciente import Paciente
from model.persona import Persona
from model.ubicacion import Ubicacion
from model.semaforo import Semaforo
from model.tipo_test import TipoTest
from model.escala import Escala
from utils.db import db

heatmap_bp = Blueprint('heatmap', __name__)

@heatmap_bp.route('/heatmap/tests', methods=['GET'])
def get_tests_for_heatmap():
    # Obtener todos los tests realizados que tienen un paciente con ubigeo registrado
    tests = Test.query.join(Paciente).join(Persona).filter(Persona.ubigeo.isnot(None)).all()
    
    heatmap_data = []

    for test in tests:
        paciente = Paciente.query.get(test.id_paciente)
        persona = Persona.query.get(paciente.id_persona)
        
        # Obtener la escala y semaforo asociados al test
        escala = Escala.query.get(test.id_rango_escala)
        semaforo = Semaforo.query.filter_by(id_rango_escala=escala.id_rango_escala).first()
        tipo_test = TipoTest.query.get(test.id_tipo_test)
        color = semaforo.color if semaforo else 'gris'  # Color por defecto si no hay semaforo
        
        # Obtener la ubicación basada en el ubigeo de la persona
        ubicacion = Ubicacion.query.get(persona.ubigeo)

        if ubicacion:
            heatmap_data.append({
                'nombre_paciente': f"{persona.nombre} {persona.apellido_paterno}",
                'latitud': ubicacion.latitud,
                'longitud': ubicacion.longitud,
                'color_escala': color,
                'id_tipo_test': test.id_tipo_test,
                'nombre_tipo_test': tipo_test.nombre if tipo_test else 'Desconocido',
                'descripcion_escala': escala.descripcion if escala else 'No disponible',
                'fecha_realizacion': test.fecha_realizacion.strftime('%Y-%m-%d')
            })

    data = {
        'message': 'Datos del heatmap obtenidos correctamente',
        'status': 200,
        'data': heatmap_data
    }

    return make_response(jsonify(data), 200)

@heatmap_bp.route('/heatmap/test-types', methods=['GET'])
def get_test_types():
    tipos_test = TipoTest.query.all()
    test_types = [{'id': tipo.id_tipo_test, 'nombre': tipo.nombre} for tipo in tipos_test]
    
    data = {
        'message': 'Tipos de test obtenidos correctamente',
        'status': 200,
        'data': test_types
    }
    
    return make_response(jsonify(data), 200)
    