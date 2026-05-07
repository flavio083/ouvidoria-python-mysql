"""Script to update an existing complaint."""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Local imports
from config.config import HOST, USER, PASSWORD, DATABASE, PORT
from database.operacoesbd import criarConexao, encerrarConexao, atualizarBancoDados

conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)

codigoNovaReclamacao = int(input("Digite o código da reclamação a ser substituida: "))
novaReclamação = input("Digite a nova reclamação: ")

consulta = 'UPDATE Reclamações SET reclamacao = %s WHERE codigo = %s'
dados = [ novaReclamação, codigoNovaReclamacao]

linhasAfetadas = atualizarBancoDados(conexao,consulta,dados)


if linhasAfetadas == 0:
    print("Não possui nenhuma reclamação para o código informado.")
else:
    print("Reclamação substituida com sucesso!")

encerrarConexao(conexao)
