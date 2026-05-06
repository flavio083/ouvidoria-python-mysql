import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from database.operacoesbd import *
from config.config import *

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
