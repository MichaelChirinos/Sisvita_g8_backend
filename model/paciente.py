from utils.db import db
from dataclasses import dataclass

@dataclass
class Paciente(db.Model):
    __tablename__ = 'paciente'
    id_paciente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_persona  = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    fecha_registro = db.Column(db.Date)
    
    persona = db.relationship('Persona', backref='paciente')

    def __init__(self, id_paciente, id_persona,fecha_registro):
        self.id_paciente = id_paciente
        self.id_persona = id_persona
        self.fecha_registro = fecha_registro

                
