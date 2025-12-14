from flask import Flask, jsonify, request

app = Flask(__name__)

livros = []
contador_id = 1

