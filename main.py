from operacoesbd import *

conexao = criarConexao("localhost","root","Futebol06!","ouvidoriabd",3306)

#usar a conexao

encerrarConexao(conexao)