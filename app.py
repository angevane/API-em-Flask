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
