from operacoesbd import *

conexao = criarConexao("localhost","root","Futebol06!","ouvidoriabd",3306)

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