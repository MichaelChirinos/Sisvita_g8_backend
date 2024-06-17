from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Usuario(db.Model):
    __tablename__='usuario'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    dni = db.Column(db.Integer)
    telefono = db.Column(db.Integer)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    clave = db.Column(db.String(256))  # Incrementar la longitud para almacenar hashes más largos
    fecha_nacimiento = db.Column(db.Date)
    sexo = db.Column(db.String(1))

    def __init__(self, nombre, apellido, dni, telefono, correo, clave, fecha_nacimiento=None, sexo=None):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.correo = correo
        self.clave = clave
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
