from utils.ma import ma
from model.test import Test
from marshmallow import fields
from schemas.estudiante import EstudianteSchema

class TestSchema(ma.Schema):
    class Meta:
        model = Test
        fields = (
            'id_test',
            'id_estudiante',
            'total_Inquietud',
            'Categoria_Inquietud',
            'total_Ansiedad_Fisiologica',
            'Categoria_Ansiedad_Fisiologica',
            'total_Estres_Preocupaciones',
            'Categoria_Estres_Preocupaciones',
            'total_Ansiedad_Examenes',
            'Categoria_Ansiedad_Examenes',
            'total_Mentira',
            'Categoria_Mentira'
        )
    estudiante = fields.Nested(EstudianteSchema)

test_schema = TestSchema()
tests_schema = TestSchema(many=True)

