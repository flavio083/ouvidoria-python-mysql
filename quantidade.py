from conexao import conectar
from operacoesbd import *

conexao = conectar()
consulta = 'select count(*) from reclamacoes'
reclamacoes = listarBancoDados(conexao,consulta)

total = reclamacoes[0][0]

if total <= 0:
    print("Atualmente não temos reclamação.")
elif total == 1:
    print("Atualmente temos", total, "reclamação.")
else:
    print("Atualmente temos", total, "reclamações.")

encerrarConexao(conexao)