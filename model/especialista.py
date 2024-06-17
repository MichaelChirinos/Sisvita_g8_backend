from utils.db import db

from dataclasses import dataclass

@dataclass
class Especialista(db.Model):
    __tablename__ = 'especialista'
    id_especialista = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    especialidad = db.Column(db.String)
    colegiado = db.Column(db.Integer)

    usuario = db.relationship('Usuario', backref='especialista')    

    def __init__(self, id_especialista, id_usuario, especialidad,colegiado):
        self.id_especialista = id_especialista
        self.id_usuario = id_usuario
        self.especialidad = especialidad
        self.colegiado = colegiado
