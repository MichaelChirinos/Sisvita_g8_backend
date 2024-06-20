from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Pregunta(db.Model):
    __tablename__='pregunta'
    id_pregunta = db.Column(db.Integer, primary_key=True)
    id_tipo_test  = db.Column(db.Integer, db.ForeignKey('tipo_test.id_tipo_test'))
    descripcion  = db.Column(db.String(255))

    tipo_test = db.relationship('TipoTest', backref='pregunta')

    def __init__(self, id_pregunta,id_tipo_test, descripcion):
        self.id_pregunta = id_pregunta
        self.id_tipo_test = id_tipo_test
        self.descripcion = descripcion
