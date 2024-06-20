from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Escala(db.Model):
    __tablename__='rango_escala'
    id_rango_escala = db.Column(db.Integer, primary_key=True)
    id_tipo_test  = db.Column(db.Integer, db.ForeignKey('tipo_test.id_tipo_test'))
    puntaje_minimo  = db.Column(db.String(3))
    puntaje_maximo = db.Column(db.String(3))
    descripcion = db.Column(db.String(255))

    tipo_test = db.relationship('TipoTest', backref='rango_escala')

    def __init__(self, id_rango_escala,id_tipo_test, puntaje_minimo,puntaje_maximo,descripcion):
        self.id_rango_escala = id_rango_escala
        self.id_tipo_test = id_tipo_test
        self.puntaje_minimo = puntaje_minimo
        self.puntaje_maximo = puntaje_maximo
        self.descripcion = descripcion        
