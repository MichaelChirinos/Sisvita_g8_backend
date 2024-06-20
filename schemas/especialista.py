from utils.ma import ma
from model.especialista import Especialista
from schemas.persona import PersonaSchema
from marshmallow import fields

class EspecialistaSchema(ma.Schema):
    class Meta:
        model = Especialista
        fields = ('id_especialista', 'id_persona', 'colegiatura', 'persona')

    persona = fields.Nested(PersonaSchema)

especialista_schema = EspecialistaSchema()
especialistas_schema = EspecialistaSchema(many=True)
