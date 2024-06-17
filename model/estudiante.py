from utils.db import db
from dataclasses import dataclass

@dataclass
class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    id_estudiante = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    codigo_estudiante = db.Column(db.Integer)

    usuario = db.relationship('Usuario', backref='estudiante')

    def __init__(self, id_estudiante, id_usuario, codigo_estudiante):
        self.id_estudiante = id_estudiante
        self.id_usuario = id_usuario
        self.codigo_estudiante = codigo_estudiante
