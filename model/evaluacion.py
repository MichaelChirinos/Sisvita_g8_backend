from utils.db import db
from dataclasses import dataclass

@dataclass
class Evaluacion(db.Model):
    __tablename__ = 'evaluacion'
    id_evaluacion = db.Column(db.Integer, primary_key=True)
    id_historia_clinica = db.Column(db.Integer, nullable=False)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    suma_respuestas = db.Column(db.Integer)

    test = db.relationship('Test', backref='evaluaciones')

    def __init__(self, id_historia_clinica, id_test, suma_respuestas):
        self.id_historia_clinica = id_historia_clinica
        self.id_test = id_test
        self.suma_respuestas = suma_respuestas
