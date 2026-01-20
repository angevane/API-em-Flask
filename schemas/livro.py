from marshmallow import Schema, fields

class LivroSchema(Schema):
    id = fields.Str(required=False)
    titulo = fields.Str(required=True)
    autor = fields.Str(required=True)
    ano = fields.Int(required=True)

class LivroSchemaUpdate(Schema):
    titulo = fields.Str(required=False)
    autor = fields.Str(required=False)
    ano = fields.Int(required=False)
