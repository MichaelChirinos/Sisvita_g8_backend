from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Alternativa(db.Model):
    __tablename__='alternativa'
    id_alternativa = db.Column(db.Integer, primary_key=True)
    id_tipo_test  = db.Column(db.Integer, db.ForeignKey('tipo_test.id_tipo_test'))
    descripcion  = db.Column(db.String(255))
    puntaje = db.Column(db.Integer)

    tipo_test = db.relationship('TipoTest', backref='alternativa')

    def __init__(self, id_alternativa,id_tipo_test, descripcion,puntaje):
        self.id_alternativa = id_alternativa
        self.id_tipo_test = id_tipo_test
        self.descripcion = descripcion
        self.puntaje = puntaje        
