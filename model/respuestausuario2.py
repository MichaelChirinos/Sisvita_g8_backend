from sqlalchemy.orm import relationship
from utils.db import db
from datetime import date
from dataclasses import dataclass

class RespuestaUsuario2(db.Model):
    __tablename__ = 'respuesta_usuario_2'
    
    id_respuesta2 = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    respuesta_1 = db.Column(db.String(30), nullable=False)
    respuesta_2 = db.Column(db.String(30), nullable=False)
    respuesta_3 = db.Column(db.String(30), nullable=False)
    respuesta_4 = db.Column(db.String(30), nullable=False)
    respuesta_5 = db.Column(db.String(30), nullable=False)
    respuesta_6 = db.Column(db.String(30), nullable=False)
    respuesta_7 = db.Column(db.String(30), nullable=False)
    respuesta_8 = db.Column(db.String(30), nullable=False)
    respuesta_9 = db.Column(db.String(30), nullable=False)
    respuesta_10 = db.Column(db.String(30), nullable=False)
    respuesta_11 = db.Column(db.String(30), nullable=False)
    respuesta_12 = db.Column(db.String(30), nullable=False)
    respuesta_13 = db.Column(db.String(30), nullable=False)
    respuesta_14 = db.Column(db.String(30), nullable=False)
    respuesta_15 = db.Column(db.String(30), nullable=False)
    respuesta_16 = db.Column(db.String(30), nullable=False)
    respuesta_17 = db.Column(db.String(30), nullable=False)
    respuesta_18 = db.Column(db.String(30), nullable=False)
    respuesta_19 = db.Column(db.String(30), nullable=False)
    respuesta_20 = db.Column(db.String(30), nullable=False)
    suma_respuestas2 = db.Column(db.Integer, nullable=False, default=0)  # Add the sum field here

    usuario = relationship("Usuario", backref="respuestausuario2")

    def __init__(self, id_usuario, respuesta_1, respuesta_2, respuesta_3, respuesta_4, respuesta_5, respuesta_6, respuesta_7,respuesta_8,respuesta_9,respuesta_10,respuesta_11,respuesta_12,respuesta_13,respuesta_14,respuesta_15,respuesta_16,respuesta_17,respuesta_18,respuesta_19,respuesta_20):
        self.id_usuario = id_usuario
        self.respuesta_1 = respuesta_1
        self.respuesta_2 = respuesta_2
        self.respuesta_3 = respuesta_3
        self.respuesta_4 = respuesta_4
        self.respuesta_5 = respuesta_5
        self.respuesta_6 = respuesta_6
        self.respuesta_7 = respuesta_7
        self.respuesta_8 = respuesta_8
        self.respuesta_9 = respuesta_9
        self.respuesta_10 = respuesta_10
        self.respuesta_11 = respuesta_11
        self.respuesta_12 = respuesta_12
        self.respuesta_13 = respuesta_13
        self.respuesta_14 = respuesta_14
        self.respuesta_15 = respuesta_15
        self.respuesta_16 = respuesta_16
        self.respuesta_17 = respuesta_17
        self.respuesta_18 = respuesta_18
        self.respuesta_19 = respuesta_19
        self.respuesta_20 = respuesta_20
        self.suma_respuestas2 = self.calcular_suma_respuestas2()

    def calcular_suma_respuestas2(self):
        conversion = {'Nunca': 0, 'A veces': 1, 'A menudo': 2, 'Siempre': 3}
        return (
            conversion[self.respuesta_1] +
            conversion[self.respuesta_2] +
            conversion[self.respuesta_3] +
            conversion[self.respuesta_4] +
            conversion[self.respuesta_5] +
            conversion[self.respuesta_6] +
            conversion[self.respuesta_7] +
            conversion[self.respuesta_8] +
            conversion[self.respuesta_9] +
            conversion[self.respuesta_10] +
            conversion[self.respuesta_11] +
            conversion[self.respuesta_12] +
            conversion[self.respuesta_13] +
            conversion[self.respuesta_14] +
            conversion[self.respuesta_15] +
            conversion[self.respuesta_16] +
            conversion[self.respuesta_17] +
            conversion[self.respuesta_18] +
            conversion[self.respuesta_19] +
            conversion[self.respuesta_20]
        )
