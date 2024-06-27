from utils.ma import ma
from model.historia_clinica import HistoriaClinica
from marshmallow import fields
from schemas.paciente import PersonaSchema
from schemas.especialista import EspecialistaSchema

class HistoriaClinicaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = HistoriaClinica
        load_instance = True
        include_fk = True
        fields = (
            'id_historia_clinica',
            'id_paciente',
            'id_especialista',
            'fecha_consulta',
            'paciente',
            'especialista'
        )
    paciente = fields.Nested(PersonaSchema)
    especialista = fields.Nested(EspecialistaSchema)

HistoriaClinica_schema = HistoriaClinicaSchema()
HistoriaClinicas_schema = HistoriaClinicaSchema(many=True)
