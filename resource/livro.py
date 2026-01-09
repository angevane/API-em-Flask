import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import livros
from schemas.livro import LivroSchema, LivroSchemaUpdate

livro_blp = Blueprint(
    "Livros",
    __name__,
    description="Operações relacionadas a livros"
)

@livro_blp.route("/livros")
class LivroList(MethodView):

    @livro_blp.response(200, LivroSchema(many=True))
    def get(self):
        return livros.values()

    @livro_blp.arguments(LivroSchema)
    @livro_blp.response(201, LivroSchema)
    def post(self, livro_dado):
        livro_id = uuid.uuid4().hex
        livro = {**livro_dado, "id": livro_id}
        livros[livro_id] = livro
        return livro


@livro_blp.route("/livro/<string:id_livro>")
class LivroResource(MethodView):

    @livro_blp.response(200, LivroSchema)
    def get(self, id_livro):
        try:
            return livros[id_livro]
        except KeyError:
            abort(404, message="Livro não encontrado")

    @livro_blp.arguments(LivroSchemaUpdate)
    @livro_blp.response(200, LivroSchema)
    def put(self, dados, id_livro):
        try:
            livros[id_livro].update(dados)
            return livros[id_livro]
        except KeyError:
            abort(404, message="Livro não encontrado")

    def delete(self, id_livro):
        try:
            livros.pop(id_livro)
            return {"message": "Livro removido com sucesso"}
        except KeyError:
            abort(404, message="Livro não encontrado")
