import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from database.operacoesbd import (
    criarConexao,
    encerrarConexao,
    listarBancoDados,
    insertNoBancoDados,
    atualizarBancoDados,
    excluirBancoDados,
)
from config.config import (
    DB_HOST,
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
    DB_PORT,
)

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


def get_conexao():
    return criarConexao(
    DB_HOST,
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
    DB_PORT
)

def _serialize_complaint(row):
    return {"codigo": row[0], "reclamacao": row[1]}


def _validate_complaint_text(text):
    text = text.strip()
    if len(text) == 0:
        return None, "Deve ser inserido ao menos 1 caractere!"
    return text, None



@app.route("/api/reclamacoes", methods=["GET"])
def listar_reclamacoes():
    conexao = get_conexao()
    if conexao is None:
        return jsonify({"erro": "Falha ao conectar ao banco de dados"}), 500

    try:
        consulta = "SELECT * FROM Reclamações"
        reclamacoes = listarBancoDados(conexao, consulta)
        return jsonify([_serialize_complaint(r) for r in reclamacoes]), 200
    finally:
        encerrarConexao(conexao)


@app.route("/api/reclamacoes", methods=["POST"])
def criar_reclamacao():
    dados = request.get_json(silent=True)
    if not dados or not dados.get("reclamacao"):
        return jsonify({"erro": "Campo 'reclamacao' é obrigatório."}), 400

    texto, erro = _validate_complaint_text(dados["reclamacao"])
    if erro:
        return jsonify({"erro": erro}), 400

    conexao = get_conexao()
    if conexao is None:
        return jsonify({"erro": "Falha ao conectar ao banco de dados"}), 500

    try:
        consulta = "INSERT INTO Reclamações (reclamacao) VALUES (%s);"
        novo_id = insertNoBancoDados(conexao, consulta, [texto])

        if novo_id is None:
            return jsonify({"erro": "Erro ao inserir reclamação no banco."}), 500

        return jsonify({
            "mensagem": "Reclamação adicionada com sucesso!",
            "codigo": novo_id,
            "reclamacao": texto,
        }), 201
    finally:
        encerrarConexao(conexao)


@app.route("/api/reclamacoes/<int:codigo>", methods=["GET"])
def pesquisar_reclamacao(codigo):
    conexao = get_conexao()
    if conexao is None:
        return jsonify({"erro": "Falha ao conectar ao banco de dados"}), 500

    try:
        consulta = "SELECT * FROM Reclamações WHERE codigo = %s"
        reclamacoes = listarBancoDados(conexao, consulta, [codigo])

        if reclamacoes:
            return jsonify(_serialize_complaint(reclamacoes[0])), 200
        return jsonify({"erro": "O código informado não é válido."}), 404
    finally:
        encerrarConexao(conexao)


@app.route("/api/reclamacoes/<int:codigo>", methods=["PUT"])
def atualizar_reclamacao(codigo):
    dados = request.get_json(silent=True)
    if not dados or not dados.get("reclamacao"):
        return jsonify({"erro": "Campo 'reclamacao' é obrigatório."}), 400

    novo_texto, erro = _validate_complaint_text(dados["reclamacao"])
    if erro:
        return jsonify({"erro": erro}), 400

    conexao = get_conexao()
    if conexao is None:
        return jsonify({"erro": "Falha ao conectar ao banco de dados"}), 500

    try:
        consulta = "UPDATE Reclamações SET reclamacao = %s WHERE codigo = %s"
        linhas = atualizarBancoDados(conexao, consulta, [novo_texto, codigo])

        if linhas == 0:
            return jsonify({"erro": "Não existe reclamação para o código informado."}), 404

        return jsonify({
            "mensagem": "Reclamação substituída com sucesso!",
            "codigo": codigo,
            "reclamacao": novo_texto,
        }), 200
    finally:
        encerrarConexao(conexao)


@app.route("/api/reclamacoes/<int:codigo>", methods=["DELETE"])
def remover_reclamacao(codigo):
    conexao = get_conexao()
    if conexao is None:
        return jsonify({"erro": "Falha ao conectar ao banco de dados"}), 500

    try:
        consulta = "DELETE FROM Reclamações WHERE codigo = %s"
        linhas = excluirBancoDados(conexao, consulta, [codigo])

        if linhas == 0:
            return jsonify({"erro": "O código informado não é válido."}), 404

        return jsonify({"mensagem": "Reclamação removida com sucesso!"}), 200
    finally:
        encerrarConexao(conexao)


@app.route("/api/reclamacoes/quantidade", methods=["GET"])
def quantidade_reclamacoes():
    conexao = get_conexao()
    if conexao is None:
        return jsonify({"erro": "Falha ao conectar ao banco de dados"}), 500

    try:
        consulta = "SELECT COUNT(*) FROM Reclamações"
        resultado = listarBancoDados(conexao, consulta)
        total = resultado[0][0] if resultado else 0
        return jsonify({"total": total}), 200
    finally:
        encerrarConexao(conexao)


import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000))
    )