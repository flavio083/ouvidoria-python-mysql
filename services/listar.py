"""Script to list all complaints from the database."""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Local imports
from config.config import HOST, USER, PASSWORD, DATABASE, PORT
from database.operacoesbd import criarConexao, encerrarConexao, listarBancoDados

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
