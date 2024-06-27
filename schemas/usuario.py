from utils.ma import ma
from model.usuario import Usuario
from marshmallow import fields
from schemas.persona import PersonaSchema

class UsuarioSchema(ma.Schema):
    class Meta:
        model = Usuario
        fields = (
            'id_usuario',
            'id_persona',
            'correo',
            'clave',
            'is_admin',
            'persona'
        )

    persona = fields.Nested(PersonaSchema)

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

