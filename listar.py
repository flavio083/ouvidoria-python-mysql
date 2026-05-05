from operacoesbd import *

conexao = criarConexao("localhost","root","Futebol06!","ouvidoriabd",3306)

consulta = 'select * from Reclamações'
reclamacoes = listarBancoDados(conexao,consulta)

if len(reclamacoes) > 0:
    print("-- Lista de Reclamações --")
    for item in reclamacoes:
        print(item[0],"-",item[1])

else:
    print("Nenhuma reclamação foi encontrado")

encerrarConexao(conexao)
