from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensagem": "API de Gestão de Livros ativa!"})

if __name__ == "__main__":
    app.run(debug=True)
