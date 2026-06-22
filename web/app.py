import sys
import os
from pathlib import Path
from functools import wraps

sys.path.insert(0, str(Path(__file__).parent.parent))

from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    Response,
)
from flask_cors import CORS

from database.operacoesbd import (
    criarConexao,
    encerrarConexao,
    listarBancoDados,
    insertNoBancoDados,
    atualizarBancoDados,
    excluirBancoDados,
)

from config.config_exemplo import (
    DB_HOST,
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
    DB_PORT,
    DB_ADMIN_USER,
    DB_ADMIN_PASSWORD,
)

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = False

CORS(
    app,
    origins=[
        "https://ouvidoria-python-mysql.onrender.com"
    ]
)



def check_auth(username, password):
    return (
        username == DB_ADMIN_USER
        and password == DB_ADMIN_PASSWORD
    )


def authenticate():
    return Response(
        "Acesso não autorizado.",
        401,
        {
            "WWW-Authenticate": 'Basic realm="Admin Area"'
        },
    )


def require_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.authorization

        if not auth:
            return authenticate()

        if not check_auth(
            auth.username,
            auth.password,
        ):
            return authenticate()

        return func(*args, **kwargs)

    return decorated


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/admin")
@require_auth
def admin():
    return render_template("admin.html")


@app.route("/estoque")
def estoque():
    return render_template("estoque.html")


@app.route("/admin/estoque")
@require_auth
def admin_estoque():
    return render_template("admin_estoque.html")



def get_conexao():
    return criarConexao(
        DB_HOST,
        DB_USER,
        DB_PASSWORD,
        DB_NAME,
        DB_PORT,
    )



def _serialize_complaint(row):
    return {
        "codigo": row[0],
        "reclamacao": row[1],
    }


def _validate_complaint_text(text):
    text = text.strip()

    if len(text) == 0:
        return None, "Deve ser inserido ao menos 1 caractere!"

    return text, None



def _serialize_product(row):
    return {
        "id": row[0],
        "nome": row[1],
        "categoria": row[2],
        "quantidade": row[3],
        "preco": float(row[4]),
        "fornecedor": row[5],
    }


def _validate_product(dados):
    nome = (dados.get("nome") or "").strip()
    categoria = (dados.get("categoria") or "").strip()
    fornecedor = (dados.get("fornecedor") or "").strip()

    if not nome:
        return None, "Campo 'nome' é obrigatório."
    if not categoria:
        return None, "Campo 'categoria' é obrigatório."
    if not fornecedor:
        return None, "Campo 'fornecedor' é obrigatório."

    try:
        quantidade = int(dados.get("quantidade", 0))
    except (ValueError, TypeError):
        return None, "Campo 'quantidade' deve ser um número inteiro."

    try:
        preco = float(dados.get("preco", 0))
    except (ValueError, TypeError):
        return None, "Campo 'preco' deve ser um número válido."

    return {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco,
        "fornecedor": fornecedor,
    }, None


# RECLAMAÇÕES

@app.route("/api/reclamacoes", methods=["GET"])
def listar_reclamacoes():
    conexao = get_conexao()

    if conexao is None:
        return jsonify({
            "erro": "Falha ao conectar ao banco de dados"
        }), 500

    try:
        consulta = "SELECT * FROM Reclamações"
        reclamacoes = listarBancoDados(conexao, consulta)

        return jsonify([
            _serialize_complaint(r)
            for r in reclamacoes
        ]), 200

    finally:
        encerrarConexao(conexao)


@app.route("/api/reclamacoes", methods=["POST"])
def criar_reclamacao():
    dados = request.get_json(silent=True)

    if not dados or not dados.get("reclamacao"):
        return jsonify({
            "erro": "Campo 'reclamacao' é obrigatório."
        }), 400

    texto, erro = _validate_complaint_text(dados["reclamacao"])

    if erro:
        return jsonify({"erro": erro}), 400

    conexao = get_conexao()

    if conexao is None:
        return jsonify({
            "erro": "Falha ao conectar ao banco de dados"
        }), 500

    try:
        consulta = (
            "INSERT INTO Reclamações "
            "(reclamacao) VALUES (%s);"
        )

        novo_id = insertNoBancoDados(conexao, consulta, [texto])

        if novo_id is None:
            return jsonify({
                "erro": "Erro ao inserir reclamação no banco."
            }), 500

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
        return jsonify({
            "erro": "Falha ao conectar ao banco de dados"
        }), 500

    try:
        consulta = "SELECT * FROM Reclamações WHERE codigo = %s"
        reclamacoes = listarBancoDados(conexao, consulta, [codigo])

        if reclamacoes:
            return jsonify(_serialize_complaint(reclamacoes[0])), 200

        return jsonify({
            "erro": "O código informado não é válido."
        }), 404

    finally:
        encerrarConexao(conexao)


@app.route("/api/reclamacoes/<int:codigo>", methods=["PUT"])
def atualizar_reclamacao(codigo):
    dados = request.get_json(silent=True)

    if not dados or not dados.get("reclamacao"):
        return jsonify({
            "erro": "Campo 'reclamacao' é obrigatório."
        }), 400

    novo_texto, erro = _validate_complaint_text(dados["reclamacao"])

    if erro:
        return jsonify({"erro": erro}), 400

    conexao = get_conexao()

    if conexao is None:
        return jsonify({
            "erro": "Falha ao conectar ao banco de dados"
        }), 500

    try:
        consulta = (
            "UPDATE Reclamações "
            "SET reclamacao = %s "
            "WHERE codigo = %s"
        )

        linhas = atualizarBancoDados(
            conexao, consulta, [novo_texto, codigo]
        )

        if linhas == 0:
            return jsonify({
                "erro": "Não existe reclamação para o código informado."
            }), 404

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
        return jsonify({
            "erro": "Falha ao conectar ao banco de dados"
        }), 500

    try:
        consulta = "DELETE FROM Reclamações WHERE codigo = %s"
        linhas = excluirBancoDados(conexao, consulta, [codigo])

        if linhas == 0:
            return jsonify({
                "erro": "O código informado não é válido."
            }), 404

        return jsonify({
            "mensagem": "Reclamação removida com sucesso!"
        }), 200

    finally:
        encerrarConexao(conexao)


@app.route("/api/reclamacoes/quantidade", methods=["GET"])
def quantidade_reclamacoes():
    conexao = get_conexao()

    if conexao is None:
        return jsonify({
            "erro": "Falha ao conectar ao banco de dados"
        }), 500

    try:
        consulta = "SELECT COUNT(*) FROM Reclamações"
        resultado = listarBancoDados(conexao, consulta)
        total = resultado[0][0] if resultado else 0

        return jsonify({"total": total}), 200

    finally:
        encerrarConexao(conexao)

# PRODUTOS

@app.route("/api/produtos", methods=["GET"])
def listar_produtos():
    conexao = get_conexao()

    if conexao is None:
        return jsonify({
            "erro": "Falha ao conectar ao banco de dados"
        }), 500

    try:
        consulta = "SELECT * FROM Produtos ORDER BY id ASC"
        produtos = listarBancoDados(conexao, consulta)

        return jsonify([
            _serialize_product(p)
            for p in produtos
        ]), 200

    finally:
        encerrarConexao(conexao)


@app.route("/api/produtos", methods=["POST"])
def criar_produto():
    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({
            "erro": "Dados inválidos."
        }), 400

    produto, erro = _validate_product(dados)

    if erro:
        return jsonify({"erro": erro}), 400

    conexao = get_conexao()

    if conexao is None:
        return jsonify({
            "erro": "Falha ao conectar ao banco de dados"
        }), 500

    try:
        consulta = (
            "INSERT INTO Produtos "
            "(nome, categoria, quantidade, preco, fornecedor) "
            "VALUES (%s, %s, %s, %s, %s)"
        )

        novo_id = insertNoBancoDados(
            conexao,
            consulta,
            [
                produto["nome"],
                produto["categoria"],
                produto["quantidade"],
                produto["preco"],
                produto["fornecedor"],
            ],
        )

        if novo_id is None:
            return jsonify({
                "erro": "Erro ao inserir produto no banco."
            }), 500

        return jsonify({
            "mensagem": "Produto cadastrado com sucesso!",
            "id": novo_id,
            **produto,
        }), 201

    finally:
        encerrarConexao(conexao)


@app.route("/api/produtos/<int:produto_id>", methods=["GET"])
def pesquisar_produto(produto_id):
    conexao = get_conexao()

    if conexao is None:
        return jsonify({
            "erro": "Falha ao conectar ao banco de dados"
        }), 500

    try:
        consulta = "SELECT * FROM Produtos WHERE id = %s"
        produtos = listarBancoDados(conexao, consulta, [produto_id])

        if produtos:
            return jsonify(_serialize_product(produtos[0])), 200

        return jsonify({
            "erro": "O código informado não é válido."
        }), 404

    finally:
        encerrarConexao(conexao)


@app.route("/api/produtos/<int:produto_id>", methods=["PUT"])
def atualizar_produto(produto_id):
    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({"erro": "Dados inválidos."}), 400

    produto, erro = _validate_product(dados)

    if erro:
        return jsonify({"erro": erro}), 400

    conexao = get_conexao()

    if conexao is None:
        return jsonify({
            "erro": "Falha ao conectar ao banco de dados"
        }), 500

    try:
        consulta = (
            "UPDATE Produtos SET "
            "nome = %s, categoria = %s, quantidade = %s, "
            "preco = %s, fornecedor = %s "
            "WHERE id = %s"
        )

        linhas = atualizarBancoDados(
            conexao,
            consulta,
            [
                produto["nome"],
                produto["categoria"],
                produto["quantidade"],
                produto["preco"],
                produto["fornecedor"],
                produto_id,
            ],
        )

        if linhas == 0:
            return jsonify({
                "erro": "Não existe produto para o código informado."
            }), 404

        return jsonify({
            "mensagem": "Produto atualizado com sucesso!",
            "id": produto_id,
            **produto,
        }), 200

    finally:
        encerrarConexao(conexao)


@app.route("/api/produtos/<int:produto_id>", methods=["DELETE"])
def remover_produto(produto_id):
    conexao = get_conexao()

    if conexao is None:
        return jsonify({
            "erro": "Falha ao conectar ao banco de dados"
        }), 500

    try:
        consulta = "DELETE FROM Produtos WHERE id = %s"
        linhas = excluirBancoDados(conexao, consulta, [produto_id])

        if linhas == 0:
            return jsonify({
                "erro": "O código informado não é válido."
            }), 404

        return jsonify({
            "mensagem": "Produto removido com sucesso!"
        }), 200

    finally:
        encerrarConexao(conexao)


@app.route("/api/produtos/resumo", methods=["GET"])
def resumo_produtos():
    conexao = get_conexao()

    if conexao is None:
        return jsonify({
            "erro": "Falha ao conectar ao banco de dados"
        }), 500

    try:
        consulta = (
            "SELECT COUNT(*), "
            "COALESCE(SUM(quantidade), 0), "
            "COALESCE(SUM(quantidade * preco), 0) "
            "FROM Produtos"
        )

        resultado = listarBancoDados(conexao, consulta)
        row = resultado[0] if resultado else (0, 0, 0)

        return jsonify({
            "total_produtos": row[0],
            "total_itens": int(row[1]),
            "valor_total": float(row[2]),
        }), 200

    finally:
        encerrarConexao(conexao)


@app.route("/api/produtos/alerta", methods=["GET"])
def produtos_alerta():
    limite = request.args.get("limite", 5, type=int)
    conexao = get_conexao()

    if conexao is None:
        return jsonify({
            "erro": "Falha ao conectar ao banco de dados"
        }), 500

    try:
        consulta = (
            "SELECT * FROM Produtos "
            "WHERE quantidade <= %s "
            "ORDER BY quantidade ASC"
        )

        produtos = listarBancoDados(conexao, consulta, [limite])

        return jsonify([
            _serialize_product(p)
            for p in produtos
        ]), 200

    finally:
        encerrarConexao(conexao)



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
    )