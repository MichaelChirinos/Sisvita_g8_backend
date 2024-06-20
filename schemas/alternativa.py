from utils.ma import ma
from model.alternativa import Alternativa
from marshmallow import fields
from schemas.tipo_test import TipoTestSchema

class AlternativaSchema(ma.Schema):
    class Meta:
        model = Alternativa
        fields = (
            'id_alternativa',
            'id_tipo_test',
            'descripcion',
            'puntaje',
            'tipo_test'
        )
        
    tipo_test = fields.Nested(TipoTestSchema)

Alternativa_schema = AlternativaSchema()
Alternativas_schema = AlternativaSchema(many=True)