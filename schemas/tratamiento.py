from utils.ma import ma
from marshmallow import fields

class TratamientoSchema(ma.Schema):
    id_tipo_test = fields.Integer()
    descripcion = fields.String()

Tratamiento_schema = TratamientoSchema()
Tratamientos_schema = TratamientoSchema(many=True)
