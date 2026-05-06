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

from config.config import HOST, USER, PASSWORD, DATABASE, PORT

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("admin.html")

def get_conexao():
    """Cria e retorna uma conexão com o banco de dados."""
    conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)
    if conexao is None:
        return None
    return conexao


def serializar_reclamacao(row):
    """Converte uma tupla (codigo, reclamacao) em dicionário."""
    return {"codigo": row[0], "reclamacao": row[1]}



@app.route("/api/reclamacoes", methods=["GET"])
def listar_reclamacoes():
    """Lista todas as reclamações."""
    conexao = get_conexao()
    if conexao is None:
        return jsonify({"erro": "Falha ao conectar ao banco de dados"}), 500

    try:
        consulta = "SELECT * FROM Reclamações"
        reclamacoes = listarBancoDados(conexao, consulta)
        resultado = [serializar_reclamacao(r) for r in reclamacoes]
        return jsonify(resultado), 200
    finally:
        encerrarConexao(conexao)


@app.route("/api/reclamacoes", methods=["POST"])
def criar_reclamacao():
    """Cria uma nova reclamação."""
    dados_json = request.get_json(silent=True)
    if not dados_json or not dados_json.get("reclamacao"):
        return jsonify({"erro": "O campo 'reclamacao' é obrigatório e não pode estar vazio."}), 400

    texto = dados_json["reclamacao"].strip()
    if len(texto) == 0:
        return jsonify({"erro": "Deve ser inserido ao menos 1 caractere!"}), 400

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
    """Pesquisa uma reclamação pelo código."""
    conexao = get_conexao()
    if conexao is None:
        return jsonify({"erro": "Falha ao conectar ao banco de dados"}), 500

    try:
        consulta = "SELECT * FROM Reclamações WHERE codigo = %s"
        reclamacoes = listarBancoDados(conexao, consulta, [codigo])

        if len(reclamacoes) > 0:
            return jsonify(serializar_reclamacao(reclamacoes[0])), 200
        else:
            return jsonify({"erro": "O código informado não é válido."}), 404
    finally:
        encerrarConexao(conexao)


@app.route("/api/reclamacoes/<int:codigo>", methods=["PUT"])
def atualizar_reclamacao(codigo):
    """Atualiza (substitui) uma reclamação existente."""
    dados_json = request.get_json(silent=True)
    if not dados_json or not dados_json.get("reclamacao"):
        return jsonify({"erro": "O campo 'reclamacao' é obrigatório."}), 400

    novo_texto = dados_json["reclamacao"].strip()
    if len(novo_texto) == 0:
        return jsonify({"erro": "Deve ser inserido ao menos 1 caractere!"}), 400

    conexao = get_conexao()
    if conexao is None:
        return jsonify({"erro": "Falha ao conectar ao banco de dados"}), 500

    try:
        consulta = "UPDATE Reclamações SET reclamacao = %s WHERE codigo = %s"
        linhas = atualizarBancoDados(conexao, consulta, [novo_texto, codigo])

        if linhas == 0:
            return jsonify({"erro": "Não possui nenhuma reclamação para o código informado."}), 404

        return jsonify({
            "mensagem": "Reclamação substituída com sucesso!",
            "codigo": codigo,
            "reclamacao": novo_texto,
        }), 200
    finally:
        encerrarConexao(conexao)


@app.route("/api/reclamacoes/<int:codigo>", methods=["DELETE"])
def remover_reclamacao(codigo):
    """Remove uma reclamação pelo código."""
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
    """Retorna a quantidade total de reclamações."""
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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
