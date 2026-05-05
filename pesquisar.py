from operacoesbd import *

conexao = criarConexao("localhost","root","Futebol06!","ouvidoriabd",3306)

codigoReclamacao = int(input("Digite o código da Reclamação: "))
consulta = 'select * from Reclamações where codigo = %s'
dados = [codigoReclamacao]

reclamacoes = listarBancoDados(conexao,consulta,dados)

if len(reclamacoes) > 0:
    print("A reclamação pesquisada foi:", reclamacoes[0][1])
else:
    print("O código informado não é válido.")

encerrarConexao(conexao)