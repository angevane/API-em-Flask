from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.livro import LivroModel
from models.autor import AutorModel
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
        return LivroModel.query.all()

    @livro_blp.arguments(LivroSchema)
    @livro_blp.response(201, LivroSchema)
    def post(self, livro_dado):
        if not AutorModel.query.get(livro_dado["autor_id"]):
            abort(404, message="Autor não encontrado")

        livro = LivroModel(**livro_dado)

        try:
            db.session.add(livro)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(400, message="Erro ao criar livro")

        return livro


@livro_blp.route("/livros/<int:id_livro>")
class LivroResource(MethodView):

    @livro_blp.response(200, LivroSchema)
    def get(self, id_livro):
        livro = LivroModel.query.get(id_livro)
        if not livro:
            abort(404, message="Livro não encontrado")
        return livro

    @livro_blp.arguments(LivroSchemaUpdate)
    @livro_blp.response(200, LivroSchema)
    def put(self, dados, id_livro):
        livro = LivroModel.query.get(id_livro)
        if not livro:
            abort(404, message="Livro não encontrado")

        for campo, valor in dados.items():
            setattr(livro, campo, valor)

        if "autor_id" in dados:
            if not AutorModel.query.get(dados["autor_id"]):
                abort(404, message="Autor não encontrado")

        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(400, message="Erro ao atualizar livro")

        return livro

    @livro_blp.response(200)
    def delete(self, id_livro):
        livro = LivroModel.query.get(id_livro)
        if not livro:
            abort(404, message="Livro não encontrado")

        try:
            db.session.delete(livro)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(400, message="Erro ao deletar livro")

        return {"message": "Livro removido com sucesso"}

