from sqlalchemy.orm import relationship
from utils.db import db
from datetime import date
from dataclasses import dataclass

class RespuestaUsuario(db.Model):
    __tablename__ = 'respuesta_usuario'
    
    id_respuesta = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    respuesta_1 = db.Column(db.String(30), nullable=False)
    respuesta_2 = db.Column(db.String(30), nullable=False)
    respuesta_3 = db.Column(db.String(30), nullable=False)
    respuesta_4 = db.Column(db.String(30), nullable=False)
    respuesta_5 = db.Column(db.String(30), nullable=False)
    respuesta_6 = db.Column(db.String(30), nullable=False)
    respuesta_7 = db.Column(db.String(30), nullable=False)
    suma_respuestas = db.Column(db.Integer, nullable=False, default=0)  # Add the sum field here

    usuario = relationship("Usuario", backref="respuestausuario")

    def __init__(self, id_usuario, respuesta_1, respuesta_2, respuesta_3, respuesta_4, respuesta_5, respuesta_6, respuesta_7):
        self.id_usuario = id_usuario
        self.respuesta_1 = respuesta_1
        self.respuesta_2 = respuesta_2
        self.respuesta_3 = respuesta_3
        self.respuesta_4 = respuesta_4
        self.respuesta_5 = respuesta_5
        self.respuesta_6 = respuesta_6
        self.respuesta_7 = respuesta_7
        self.suma_respuestas = self.calcular_suma_respuestas()

    def calcular_suma_respuestas(self):
        conversion = {'Casi ningún día': 0, 'Ocasionalmente': 1, 'Frecuentemente': 2, 'Casi todos los días': 3}
        return (
            conversion[self.respuesta_1] +
            conversion[self.respuesta_2] +
            conversion[self.respuesta_3] +
            conversion[self.respuesta_4] +
            conversion[self.respuesta_5] +
            conversion[self.respuesta_6] +
            conversion[self.respuesta_7]
        )
