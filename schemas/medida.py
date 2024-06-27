from utils.ma import ma
from model.medida import Medida
from schemas.especialista import EspecialistaSchema
from marshmallow import fields

<<<<<<< HEAD
=======

>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
class MedidaSchema(ma.Schema):
    class Meta:
        model = Medida
        fields = ('id_medida','id_especialista','descripcion', 'especialista')

<<<<<<< HEAD
    especialista = fields.Nested(EspecialistaSchema)

=======

    especialista = fields.Nested(EspecialistaSchema)


>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
medida_schema = MedidaSchema()
medidas_schema = MedidaSchema(many=True)
