from utils.ma import ma
from marshmallow import fields

class UsuarioSchema(ma.Schema):
    id_usuario = fields.Integer()
    nombre = fields.String()
    apellido = fields.String()
    dni = fields.Integer()
    telefono = fields.Integer()
    correo = fields.String()
    clave = fields.String()
    fecha_nacimiento = fields.Date()
    sexo = fields.String()
    
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
