from utils.ma import ma
from model.notificacion import Notificacion
from marshmallow import fields
from schemas.persona import PersonaSchema

class NotificacionSchema(ma.Schema):
    class Meta:
        model = Notificacion
        fields = (
            'id_notificacion',
            'id_persona',
            'tipo_mensaje',
            'mensaje',
            'persona'
        )

    persona = fields.Nested(PersonaSchema)

notificacion_schema = PersonaSchema()
notificaciones_schema = PersonaSchema(many=True)

