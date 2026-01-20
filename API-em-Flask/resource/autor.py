from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import autores
from schemas.autor import AutorSchema, AutorSchemaUpdate

autor_blp = Blueprint(
    "Autores",
    __name__,
    description="Operações relacionadas a autores"
)

@autor_blp.route("/autores")
class AutorList(MethodView):

    @autor_blp.response(200, AutorSchema(many=True))
    def get(self):
        return autores.values()

    @autor_blp.arguments(AutorSchema)
    @autor_blp.response(201, AutorSchema)
    def post(self, autor_dados):
        autor_id = len(autores) + 1
        autor = {**autor_dados, "id": autor_id}
        autores[autor_id] = autor
        return autor


@autor_blp.route("/autor/<int:autor_id>")
class AutorResource(MethodView):

    @autor_blp.response(200, AutorSchema)
    def get(self, autor_id):
        try:
            return autores[autor_id]
        except KeyError:
            abort(404, message="Autor não encontrado")

    @autor_blp.arguments(AutorSchemaUpdate)
    @autor_blp.response(200, AutorSchema)
    def put(self, dados, autor_id):
        try:
            autores[autor_id].update(dados)
            return autores[autor_id]
        except KeyError:
            abort(404, message="Autor não encontrado")

    def delete(self, autor_id):
        try:
            autores.pop(autor_id)
            return {"message": "Autor removido com sucesso"}
        except KeyError:
            abort(404, message="Autor não encontrado")
