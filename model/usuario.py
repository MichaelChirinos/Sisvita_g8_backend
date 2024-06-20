from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Usuario(db.Model):
    __tablename__='usuario'
    id_usuario = db.Column(db.Integer, primary_key=True,autoincrement=True)
    id_persona  = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    correo = db.Column(db.String(100), nullable=False, unique=True)
    clave = db.Column(db.String(256))  # Incrementar la longitud para almacenar hashes más largos
    is_admin = db.Column(db.String(1), default='0')  # Valor predeterminado

    persona = db.relationship('Persona', backref='usuario')

    def __init__(self, id_usuario, id_persona, correo, clave, is_admin):
        self.id_usuario = id_usuario
        self.id_persona = id_persona
        self.correo = correo
        self.clave = clave
        self.is_admin = is_admin
