from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Tratamiento(db.Model):
    __tablename__='tratamiento'
    id_tratamiento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion  = db.Column(db.String(255))

    def __init__(self, id_tratamiento, descripcion):
        self.id_tratamiento = id_tratamiento
        self.descripcion = descripcion
