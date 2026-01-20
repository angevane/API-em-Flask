from marshmallow import Schema, fields
from schemas.plain import PlainAutorSchema, PlainLivroSchema

class AutorSchema(PlainAutorSchema):
    livros = fields.List(fields.Nested(PlainLivroSchema()), dump_only=True)

class AutorSchemaUpdate(Schema):
    nome = fields.Str(required=False)
