from flask import Flask, jsonify, request

app = Flask(__name__)

# "Banco de dados" em memória
livros = []
contador_id = 1


# =========================
# ROTA INICIAL
# =========================
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensagem": "API RESTful de Gestão de Livros",
        "rotas": {
            "GET /livros": "Listar todos os livros",
            "GET /livros/<id>": "Buscar livro por ID",
            "POST /livros": "Cadastrar novo livro",
            "PUT /livros/<id>": "Atualizar livro",
            "DELETE /livros/<id>": "Excluir livro"
        }
    })


# =========================
# CREATE — criar livro
# =========================
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


# =========================
# READ — listar todos
# =========================
@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)


# =========================
# READ — buscar por ID
# =========================
@app.route("/livros/<int:id>", methods=["GET"])
def buscar_livro(id):
    for livro in livros:
        if livro["id"] == id:
            return jsonify(livro)

    return jsonify({"erro": "Livro não encontrado"}), 404


# =========================
# UPDATE — atualizar livro
# =========================
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


# =========================
# DELETE — excluir livro
# =========================
@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):
    for livro in livros:
        if livro["id"] == id:
            livros.remove(livro)
            return jsonify({"mensagem": "Livro removido com sucesso"})

    return jsonify({"erro": "Livro não encontrado"}), 404


# =========================
# EXECUÇÃO
# =========================
if __name__ == "__main__":
    app.run(debug=True)