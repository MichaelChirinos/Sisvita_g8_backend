from utils.ma import ma
from model.paciente import Paciente
from marshmallow import fields
from schemas.persona import PersonaSchema

class PacienteSchema(ma.Schema):
    class Meta:
        model = Paciente
        fields = (
            'id_paciente',
            'id_persona',
            'fecha_registro',
            'persona'
        )
    persona = fields.Nested(PersonaSchema)

paciente_schema = PacienteSchema()
pacientes_schema = PacienteSchema(many=True)