from utils.ma import ma
from model.medida import Medida
from schemas.especialista import EspecialistaSchema
from marshmallow import fields


class MedidaSchema(ma.Schema):
    class Meta:
        model = Medida
        fields = ('id_medida','id_especialista','descripcion', 'especialista')


    especialista = fields.Nested(EspecialistaSchema)


medida_schema = MedidaSchema()
medidas_schema = MedidaSchema(many=True)
