from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Semaforo(db.Model):
    __tablename__ = 'semaforo'  # Nombre de la tabla en la base de datos
    id_semaforo = db.Column(db.Integer, primary_key=True,autoincrement=True)
    id_rango_escala = db.Column(db.Integer, db.ForeignKey('rango_escala.id_rango_escala'))  
    color = db.Column(db.String(10))


    escala = db.relationship('Escala', backref='semaforo')


    def __init__(self, id_semaforo,id_rango_escala, color):
        self.id_semaforo = id_semaforo
        self.id_rango_escala = id_rango_escala
        self.color = color