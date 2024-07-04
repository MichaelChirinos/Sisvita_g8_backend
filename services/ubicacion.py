from flask import Blueprint, request, jsonify
from model.ubicacion import Ubicacion
from utils.db import db
from schemas.ubicacion import ubicacion_schema, ubicaciones_schema

ubicacion_bp = Blueprint('ubicacion', __name__)

@ubicacion_bp.route('/ubicacion/v1/departamentos', methods=['GET'])
def get_departamentos():
    departamentos = db.session.query(Ubicacion.departamento).distinct().all()
    return jsonify([dep[0] for dep in departamentos])

@ubicacion_bp.route('/ubicacion/v1/provincias', methods=['GET'])
def get_provincias():
    departamento = request.args.get('departamento')
    provincias = db.session.query(Ubicacion.provincia).filter_by(departamento=departamento).distinct().all()
    return jsonify([prov[0] for prov in provincias])

@ubicacion_bp.route('/ubicacion/v1/distritos', methods=['GET'])
def get_distritos():
    provincia = request.args.get('provincia')
    distritos = db.session.query(Ubicacion.distrito, Ubicacion.ubigeo).filter_by(provincia=provincia).all()
    return jsonify([{'distrito': dis[0], 'ubigeo': dis[1]} for dis in distritos])
