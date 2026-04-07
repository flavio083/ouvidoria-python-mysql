from conexao import conectar
from operacoesbd import *

conexao = conectar()
codigoNovaReclamacao = int(input("Digite o código da reclamação a ser substituida: "))
novaReclamação = input("Digite a nova reclamação: ")

consulta = 'UPDATE reclamacoes SET reclamacao = %s WHERE codigo = %s'
dados = [ novaReclamação, codigoNovaReclamacao]

linhasAfetadas = atualizarBancoDados(conexao,consulta,dados)


if linhasAfetadas == 0:
    print("Não possui nenhuma reclamação para o código informado.")
else:
    print("Reclamação substituida com sucesso!")

encerrarConexao(conexao)