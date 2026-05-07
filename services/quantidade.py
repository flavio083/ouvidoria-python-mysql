"""Script to count and display total number of complaints."""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Local imports
from config.config import HOST, USER, PASSWORD, DATABASE, PORT
from database.operacoesbd import criarConexao, encerrarConexao, listarBancoDados

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
