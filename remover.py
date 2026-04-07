from conexao import conectar
from operacoesbd import *

conexao = conectar()
codigoReclamacao = int(input("Digite o código da Reclamação a ser Removida: "))
consulta = 'delete from reclamacoes where codigo = %s'
dados = [ codigoReclamacao ]

linhasAfetadas = excluirBancoDados(conexao,consulta,dados)

if linhasAfetadas == 0:
    print("O código informado não é válido.")
else:
    print("Reclamação removida com sucesso!")

encerrarConexao(conexao)