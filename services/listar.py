import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from database.operacoesbd import *
from config.config import *

conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)

consulta = 'select * from Reclamações'
reclamacoes = listarBancoDados(conexao,consulta)

if len(reclamacoes) > 0:
    print("-- Lista de Reclamações --")
    for item in reclamacoes:
        print(item[0],"-",item[1])

else:
    print("Nenhuma reclamação foi encontrado")

encerrarConexao(conexao)
