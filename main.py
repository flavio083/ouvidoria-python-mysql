from conexao import conectar
from operacoesbd import encerrarConexao

conexao = conectar()

# usar a conexão

encerrarConexao(conexao)