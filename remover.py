from operacoesbd import *

conexao = criarConexao("localhost","root","Futebol06!","ouvidoriabd",3306)

codigoReclamacao = int(input("Digite o código da Reclamação a ser Removida: "))
consulta = 'delete from Reclamações where codigo = %s'
dados = [ codigoReclamacao ]

linhasAfetadas = excluirBancoDados(conexao,consulta,dados)

if linhasAfetadas == 0:
    print("O código informado não é válido.")
else:
    print("Reclamação removida com sucesso!")

encerrarConexao(conexao)