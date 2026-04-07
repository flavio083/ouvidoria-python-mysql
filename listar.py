from operacoesbd import *
from conexao import conectar

conexao = conectar()

consulta = 'select * from reclamacoes'
reclamacoes = listarBancoDados(conexao,consulta)

if len(reclamacoes) > 0:
    print("-- Lista de Reclamações --")
    for item in reclamacoes:
        print(item[0],"-",item[1])

else:
    print("Nenhuma reclamação foi encontrado")

encerrarConexao(conexao)
