from flask import Flask, jsonify, request
from flask_smorest import abort
import uuid

from db import livros

app = Flask(__name__)

# =========================
# GET /livros
# =========================
@app.get('/livros')
def listar_livros():
    return jsonify({"Livros": list(livros.values())}), 200


# =========================
# GET /livro/<id>
# =========================
@app.get('/livro/<string:id_livro>')
def buscar_livro_por_id(id_livro):
    try:
        return jsonify(livros[id_livro]), 200
    except KeyError:
        abort(404, message="Livro não encontrado.")


# =========================
# GET /livro?titulo=XPTO
# =========================
@app.get('/livro')
def buscar_livro_por_titulo():
    titulo = request.args['titulo']

    for livro in livros.values():
        if livro['titulo'] == titulo:
            return jsonify(livro), 200

    abort(404, message="Livro não encontrado.")


# =========================
# POST /livro
# =========================
@app.post('/livro')
def criar_livro():
    dados = request.get_json()
    livro_id = uuid.uuid4().hex

    livro_novo = {
        **dados,
        "id": livro_id
    }

    livros[livro_id] = livro_novo

    return jsonify(livro_novo), 201


# =========================
# PUT /livro/<id>
# =========================
@app.put('/livro/<string:id_livro>')
def atualizar_livro(id_livro):
    dados_novos = request.get_json()

    for livro in livros.values():
        if livro['id'] == id_livro:
            livro.update(dados_novos)
            return jsonify({"livro atualizado": livro}), 200

    abort(404, message="Livro não encontrado.")


# =========================
# DELETE /livro/<id>
# =========================
@app.delete('/livro/<string:id_livro>')
def deletar_livro(id_livro):
    try:
        livros.pop(id_livro)
        return jsonify({"message": "Livro removido com sucesso"}), 200
    except KeyError:
        abort(404, message="Livro não encontrado.")