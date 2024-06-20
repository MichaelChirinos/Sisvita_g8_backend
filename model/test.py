from utils.db import db
from datetime import date
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import JSON

@dataclass
class Test(db.Model):
    __tablename__ = 'test'
    id_test = db.Column(db.Integer, primary_key=True)
    id_tipo_test = db.Column(db.Integer, db.ForeignKey('tipo_test.id_tipo_test'))
    fecha_realizacion = db.Column(db.Date, default=date.today)
    respuestas = db.Column(JSON)  # Usamos JSON para almacenar las respuestas como array

    tipo_test = db.relationship('TipoTest', backref='tests')

    def __init__(self, id_tipo_test, fecha_realizacion, respuestas):
        self.id_tipo_test = id_tipo_test
        self.fecha_realizacion = fecha_realizacion
        self.respuestas = respuestas
