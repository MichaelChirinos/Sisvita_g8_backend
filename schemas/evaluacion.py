from utils.ma import ma
from model.evaluacion import Evaluacion
from marshmallow import fields
from schemas.test import TestSchema

class EvaluacionSchema(ma.Schema):
    class Meta:
        model = Evaluacion
        fields = (
            'id_evaluacion',
            'id_historia_clinica',
            'id_test',
            'suma_respuestas',
            'test'
        )

    test = fields.Nested(TestSchema)

Evaluacion_schema = EvaluacionSchema()
Evaluaciones_schema = EvaluacionSchema(many=True)
