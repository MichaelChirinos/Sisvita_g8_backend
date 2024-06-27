from utils.db import db
from dataclasses import dataclass

<<<<<<< HEAD
=======

>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
@dataclass
class Medida(db.Model):
    __tablename__ = 'medida'
    id_medida = db.Column(db.Integer, primary_key=True,autoincrement=True)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'))
    descripcion = db.Column(db.String(100))

<<<<<<< HEAD
    especialista = db.relationship('Especialista', backref='medida', lazy=True)

    def __init__(self, id_medida,id_especialista, descripcion):
        self.id_medida = id_medida
        self.id_especialista = id_especialista
        self.descripcion = descripcion
=======

    especialista = db.relationship('Especialista', backref='medida', lazy=True)


    def __init__(self, id_medida,id_especialista, descripcion):
        self.id_medida = id_medida
        self.id_especialista = id_especialista
        self.descripcion = descripcion
>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
