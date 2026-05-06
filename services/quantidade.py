import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from database.operacoesbd import *
from config.config import *

conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)

consulta = 'select count(*) from Reclamações'
reclamacoes = listarBancoDados(conexao,consulta)

total = reclamacoes[0][0]

if total <= 0:
    print("Atualmente não temos reclamação.")
elif total == 1:
    print("Atualmente temos", total, "reclamação.")
else:
    print("Atualmente temos", total, "reclamações.")

encerrarConexao(conexao)
