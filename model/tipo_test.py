from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class TipoTest(db.Model):
    __tablename__='tipo_test'
    id_tipo_test = db.Column(db.Integer, primary_key=True)
    nombre  = db.Column(db.String(100))
    descripcion  = db.Column(db.String(255))

    def __init__(self, id_tipo_test, nombre, descripcion):
        self.id_tipo_test = id_tipo_test
        self.nombre = nombre
        self.descripcion = descripcion
