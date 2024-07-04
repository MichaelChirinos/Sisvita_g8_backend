from utils.ma import ma
from marshmallow import fields

class UbicacionSchema(ma.Schema):
    ubigeo = fields.String()
    distrito = fields.String()
    provincia = fields.String()
    departamento = fields.String()
    poblacion = fields.Integer()
    superficie = fields.Float()
    longitud = fields.Float()
    latitud = fields.Float()
    
ubicacion_schema = UbicacionSchema()
ubicaciones_schema = UbicacionSchema(many=True)