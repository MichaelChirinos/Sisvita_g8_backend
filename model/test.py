from utils.db import db
from datetime import date
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import JSON

@dataclass
class Test(db.Model):
    __tablename__ = 'test'
    id_test = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))
    id_tipo_test = db.Column(db.Integer, db.ForeignKey('tipo_test.id_tipo_test'))
    id_rango_escala = db.Column(db.Integer , db.ForeignKey('rango_escala.id_rango_escala'))
    id_tratamiento = db.Column(db.Integer, db.ForeignKey('tratamiento.id_tratamiento'))
    id_medida = db.Column(db.Integer, db.ForeignKey('medida.id_medida'))
    fecha_realizacion = db.Column(db.Date, default=date.today)
    respuestas = db.Column(JSON)  # Usamos JSON para almacenar las respuestas como array
    observacion = db.Column(db.Text, nullable=True)
    confirmar = db.Column(db.Boolean, default=False, nullable=True)
    suma_respuestas = db.Column(db.Integer)

    tipo_test = db.relationship('TipoTest', backref='tests')
    tratamiento = db.relationship('Tratamiento', backref='tests')

    def __init__(self, id_tipo_test,id_paciente,id_rango_escala,id_tratamiento,id_medida, fecha_realizacion,respuestas,suma_respuestas,observacion,confirmar):
        self.id_tipo_test = id_tipo_test
        self.id_paciente = id_paciente
        self.id_rango_escala = id_rango_escala
        self.id_tratamiento = id_tratamiento
        self.id_medida = id_medida
        self.fecha_realizacion = fecha_realizacion
        self.respuestas = respuestas
        self.suma_respuestas = suma_respuestas
        self.observacion = observacion
        self.confirmar = confirmar
