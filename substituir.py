from operacoesbd import *

conexao = criarConexao("localhost","root","Futebol06!","ouvidoriabd",3306)

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