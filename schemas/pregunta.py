from utils.ma import ma
from model.pregunta import Pregunta
from marshmallow import fields
from schemas.tipo_test import TipoTestSchema

class PreguntaSchema(ma.Schema):
    class Meta:
        model = Pregunta
        fields = (
            'id_pregunta',
            'id_tipo_test',
            'descripcion',
            'tipo_test'
        )
        
    tipo_test = fields.Nested(TipoTestSchema)

Pregunta_schema = PreguntaSchema()
Preguntas_schema = PreguntaSchema(many=True)