from utils.ma import ma
from model.test import Test
from marshmallow import fields
from schemas.tipo_test import TipoTestSchema
from schemas.escala import EscalaSchema
from schemas.paciente import PacienteSchema
from schemas.tratamiento import TratamientoSchema  
from schemas.medida import MedidaSchema
<<<<<<< HEAD
=======

>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291

class TestSchema(ma.Schema):
    class Meta:
        model = Test
        fields = (
            'id_test',
            'id_paciente',
            'id_tipo_test',
            'id_rango_escala',
            'id_medida',
            'fecha_realizacion',
            'respuestas',
            'suma_respuestas',
            'id_tratamiento',
            'observacion',
            'confirmar',
            'paciente',
            'escala',
            'tipo_test',
            'tratamiento',
            'medida'
        )


    tipo_test = fields.Nested(TipoTestSchema)
    escala = fields.Nested(EscalaSchema)
    paciente = fields.Nested(PacienteSchema)
    tratamiento = fields.Nested(TratamientoSchema)  
    medida = fields.Nested(MedidaSchema)
<<<<<<< HEAD
=======

>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291

Test_schema = TestSchema()
Tests_schema = TestSchema(many=True)