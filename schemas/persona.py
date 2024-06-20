from utils.ma import ma
from marshmallow import fields

class PersonaSchema(ma.Schema):
    id_persona = fields.Integer()
    nombre = fields.String()
    apellido_paterno = fields.String()
    apellido_materno = fields.String()
    tipo_documento = fields.String()
    documento = fields.String()
    telefono = fields.Integer()
    fecha_nacimiento = fields.Date()
    
persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)
