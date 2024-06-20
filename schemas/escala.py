from utils.ma import ma
from model.escala import Escala
from marshmallow import fields
from schemas.tipo_test import TipoTestSchema

class EscalaSchema(ma.Schema):
    class Meta:
        model = Escala
        fields = (
            'id_rango_escala',
            'id_tipo_test',
            'puntaje_minimo',
            'puntaje_maximo',
            'descripcion',
            'tipo_test'
        )
        
    tipo_test = fields.Nested(TipoTestSchema)

Escala_schema = EscalaSchema()
Escalas_schema = EscalaSchema(many=True)