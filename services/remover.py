import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from database.operacoesbd import *
from config.config import *

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
