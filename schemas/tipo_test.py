from utils.ma import ma
from marshmallow import fields

class TipoTestSchema(ma.Schema):
    id_tipo_test = fields.Integer()
    nombre = fields.String()
    descripcion = fields.String()

TipoTest_schema = TipoTestSchema()
TipoTests_schema = TipoTestSchema(many=True)
