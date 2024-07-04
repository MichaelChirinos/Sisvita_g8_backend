from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Ubicacion(db.Model):
    __tablename__ = 'ubicaciones'
    ubigeo = db.Column(db.String(6), primary_key=True)
    distrito = db.Column(db.String(255))
    provincia = db.Column(db.String(255))
    departamento = db.Column(db.String(255))
    poblacion = db.Column(db.Integer)
    superficie = db.Column(db.Float)
    longitud = db.Column(db.Float)
    latitud = db.Column(db.Float)

    def __init__(self,ubigeo, distrito, provincia,departamento,poblacion,superficie,longitud,latitud):
        self.ubigeo = ubigeo
        self.distrito = distrito
        self.provincia = provincia
        self.departamento = departamento
        self.poblacion = poblacion
        self.superficie = superficie
        self.longitud = longitud
        self.latitud = latitud
