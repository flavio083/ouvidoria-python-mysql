"""Script to delete a complaint from the database."""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Local imports
from config.config import HOST, USER, PASSWORD, DATABASE, PORT
from database.operacoesbd import criarConexao, encerrarConexao, excluirBancoDados

conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)

codigoReclamacao = int(input("Digite o código da Reclamação a ser Removida: "))
consulta = 'delete from Reclamações where codigo = %s'
dados = [ codigoReclamacao ]

linhasAfetadas = excluirBancoDados(conexao,consulta,dados)

if linhasAfetadas == 0:
    print("O código informado não é válido.")
else:
    print("Reclamação removida com sucesso!")

encerrarConexao(conexao)
