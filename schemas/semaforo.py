from utils.ma import ma
from model.semaforo import Semaforo
from marshmallow import fields
from schemas.escala import EscalaSchema

class AlternativaSchema(ma.Schema):
    class Meta:
        model = Semaforo
        fields = (
            'id_semaforo',
            'id_rango_escala',
            'color',
            'escala'
        )

    escala = fields.Nested(EscalaSchema)


Semaforo_schema = AlternativaSchema()
Semaforos_schema = AlternativaSchema(many=True)