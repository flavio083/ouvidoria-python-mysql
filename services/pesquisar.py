"""Script to search for a complaint by ID."""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Local imports
from config.config import HOST, USER, PASSWORD, DATABASE, PORT
from database.operacoesbd import criarConexao, encerrarConexao, listarBancoDados

conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)

codigoReclamacao = int(input("Digite o código da Reclamação: "))
consulta = 'select * from Reclamações where codigo = %s'
dados = [codigoReclamacao]

reclamacoes = listarBancoDados(conexao,consulta,dados)

if len(reclamacoes) > 0:
    print("A reclamação pesquisada foi:", reclamacoes[0][1])
else:
    print("O código informado não é válido.")

encerrarConexao(conexao)
