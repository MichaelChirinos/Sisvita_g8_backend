from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Persona(db.Model):
    __tablename__='persona'
    id_persona = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100))
    apellido_paterno = db.Column(db.String(100))
    apellido_materno = db.Column(db.String(100))
    tipo_documento   = db.Column(db.String(20))
    documento = db.Column(db.String(15))
    telefono = db.Column(db.String(15)) 
    fecha_nacimiento = db.Column(db.Date)

    def __init__(self,id_persona, nombre, apellido_paterno,apellido_materno,tipo_documento,documento,telefono,fecha_nacimiento=None):
        self.id_persona = id_persona
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.tipo_documento = tipo_documento
        self.documento = documento
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
