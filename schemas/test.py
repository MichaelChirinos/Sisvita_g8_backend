from utils.ma import ma
from model.test import Test
from marshmallow import fields
from schemas.tipo_test import TipoTestSchema

class TestSchema(ma.Schema):
    class Meta:
        model = Test
        fields = (
            'id_test',
            'id_tipo_test',
            'fecha_realizacion',
            'respuestas',
            'tipo_test'
        )

    tipo_test = fields.Nested(TipoTestSchema)

Test_schema = TestSchema()
Tests_schema = TestSchema(many=True)
