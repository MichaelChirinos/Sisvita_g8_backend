from utils.ma import ma
from model.semaforo import Semaforo
from marshmallow import fields
from schemas.escala import EscalaSchema

<<<<<<< HEAD
=======

>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
class AlternativaSchema(ma.Schema):
    class Meta:
        model = Semaforo
        fields = (
            'id_semaforo',
            'id_rango_escala',
            'color',
            'escala'
        )
<<<<<<< HEAD
        
    escala = fields.Nested(EscalaSchema)

=======

    escala = fields.Nested(EscalaSchema)


>>>>>>> baf12906ccd0196cebf65f37d6a3f5182101a291
Semaforo_schema = AlternativaSchema()
Semaforos_schema = AlternativaSchema(many=True)