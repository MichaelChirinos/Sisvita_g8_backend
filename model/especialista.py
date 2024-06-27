from utils.db import db
from dataclasses import dataclass

@dataclass
class Especialista(db.Model):
    __tablename__ = 'especialista'
    id_especialista = db.Column(db.Integer, primary_key=True,autoincrement=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    colegiatura = db.Column(db.String(15))

    persona = db.relationship('Persona', backref='especialista', lazy=True)

    def __init__(self, id_especialista,id_persona, colegiatura):
        self.id_especialista = id_especialista
        self.id_persona = id_persona
        self.colegiatura = colegiatura
