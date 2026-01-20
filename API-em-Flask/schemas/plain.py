from marshmallow import Schema, fields

class PlainAutorSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)

class PlainLivroSchema(Schema):
    id = fields.Int(dump_only=True)
    titulo = fields.Str(required=True)
    ano = fields.Int(required=True)
