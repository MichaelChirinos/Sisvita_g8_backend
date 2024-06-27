from utils.ma import ma
from marshmallow import fields

<<<<<<< HEAD
=======

>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
class TratamientoSchema(ma.Schema):
    id_tipo_test = fields.Integer()
    descripcion = fields.String()

<<<<<<< HEAD
Tratamiento_schema = TratamientoSchema()
Tratamientos_schema = TratamientoSchema(many=True)
=======

Tratamiento_schema = TratamientoSchema()
Tratamientos_schema = TratamientoSchema(many=True)
>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
