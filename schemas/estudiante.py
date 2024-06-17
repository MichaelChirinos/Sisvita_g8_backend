from utils.ma import ma
from model.estudiante import Estudiante
from marshmallow import fields
from schemas.usuario import UsuarioSchema

class EstudianteSchema(ma.Schema):
    class Meta:
        model = Estudiante
        fields = (
            'id_estudiante',
            'id_usuario',
            'codigo_estudiante',
            'usuario'

        )
    usuario = fields.Nested(UsuarioSchema)

estudiante_schema = EstudianteSchema()
estudiantes_schema = EstudianteSchema(many=True)