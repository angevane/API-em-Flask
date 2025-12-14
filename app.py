from flask import Flask, jsonify, request

app = Flask(__name__)

livros = []
contador_id = 1


@app.route("/livros", methods=["POST"])
def criar_livro():
    global contador_id
    dados = request.json

    livro = {
        "id": contador_id,
        "titulo": dados["titulo"],
        "autor": dados["autor"],
        "ano": dados["ano"]
    }

    livros.append(livro)
    contador_id += 1

    return jsonify(livro), 201


@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)



@app.route("/livros/<int:id>", methods=["GET"])
def buscar_livro(id):
    for livro in livros:
        if livro["id"] == id:
            return jsonify(livro)
    return jsonify({"erro": "Livro não encontrado"}), 404



@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    dados = request.json

    for livro in livros:
        if livro["id"] == id:
            livro["titulo"] = dados.get("titulo", livro["titulo"])
            livro["autor"] = dados.get("autor", livro["autor"])
            livro["ano"] = dados.get("ano", livro["ano"])
            return jsonify(livro)

    return jsonify({"erro": "Livro não encontrado"}), 404
