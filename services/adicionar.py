"""Script to add a new complaint to the database."""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Local imports
from config.config import HOST, USER, PASSWORD, DATABASE, PORT
from database.operacoesbd import criarConexao, encerrarConexao, listarBancoDados, insertNoBancoDados

conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)

novaReclamacao = (input("Insira sua reclamação: "))

consulta = 'insert into Reclamações (reclamacao) values (%s);'
reclamacoes = listarBancoDados(conexao,consulta)
dados = [ novaReclamacao ]

codigoNovaReclamacao = insertNoBancoDados(conexao,consulta,dados)

if len(novaReclamacao) > 0:
    reclamacoes .append(novaReclamacao)
    print("Reclamação adicionada com sucesso! \nO código é", codigoNovaReclamacao)
else:
    print("Deve ser inserido ao menos 1 caractere!")

encerrarConexao(conexao)
