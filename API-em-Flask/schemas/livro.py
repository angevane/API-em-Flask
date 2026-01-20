from marshmallow import Schema, fields
from schemas.plain import PlainLivroSchema

class LivroSchema(PlainLivroSchema):
    autor_id = fields.Int(required=True)

class LivroSchemaUpdate(Schema):
    titulo = fields.Str(required=False)
    ano = fields.Int(required=False)
    autor_id = fields.Int(required=False)
