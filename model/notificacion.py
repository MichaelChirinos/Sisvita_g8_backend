from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Notificacion(db.Model):
    __tablename__='notificacion'
    id_notificacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    tipo_mensaje = db.Column(db.String(50))
    mensaje = db.Column(db.String(50))
    
    persona = db.relationship('Persona', backref='notificacion')


    def __init__(self, id_notificacion, id_persona,tipo_mensaje,mensaje):
        self.id_notificacion = id_notificacion
        self.id_persona = id_persona
        self.tipo_mensaje = tipo_mensaje
        self.mensaje = mensaje