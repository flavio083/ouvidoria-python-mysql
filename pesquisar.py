from conexao import conectar
from operacoesbd import *

conexao = conectar()

codigoReclamacao = int(input("Digite o código da Reclamação: "))
consulta = 'select * from reclamacoes where codigo = %s'
dados = [codigoReclamacao]

reclamacoes = listarBancoDados(conexao,consulta,dados)

if len(reclamacoes) > 0:
    print("A reclamação pesquisada foi:", reclamacoes[0][1])
else:
    print("O código informado não é válido.")

encerrarConexao(conexao)