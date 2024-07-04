from utils.ma import ma
from marshmallow import fields
from model.persona import Persona
from schemas.ubicacion import UbicacionSchema

class PersonaSchema(ma.Schema):
    class Meta:
        model = Persona
        fields = (
            'id_persona',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'tipo_documento',
            'documento',
            'ubigeo',
            'telefono',
            'fecha_nacimiento',
            'distrito',
            'provincia',
            'departamento'
        )
    ubicacion = fields.Nested(UbicacionSchema)
    
persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)
