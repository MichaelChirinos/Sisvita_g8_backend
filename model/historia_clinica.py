from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class HistoriaClinica(db.Model):
    __tablename__='historia_clinica'
    id_historia_clinica = db.Column(db.Integer, primary_key=True)
    id_paciente  = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))
    id_especialista  = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'))
    fecha_consulta = db.Column(db.Date)

    paciente = db.relationship('Paciente', backref='historia_clinica')
    especialista = db.relationship('Especialista', backref = 'historia_clinica')

    def __init__(self, id_historia_clinica, id_paciente, id_especialista, fecha_consulta):
        self.id_historia_clinica = id_historia_clinica
        self.id_paciente = id_paciente
        self.id_especialista = id_especialista
        self.fecha_consulta = fecha_consulta
