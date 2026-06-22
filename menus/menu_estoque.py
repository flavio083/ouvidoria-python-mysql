import sys
from pathlib import Path
 
sys.path.insert(0, str(Path(__file__).parent.parent))
 
from config.config import HOST, USER, PASSWORD, DATABASE, PORT
from database.operacoesbd import criarConexao, encerrarConexao
from services.backend_estoque import (
    listarProdutos,
    novoProduto,
    pesquisarProduto,
    atualizarQuantidade,
    atualizarPreco,
    removerProduto,
    alertaEstoqueBaixo,
    resumoEstoque,
)
 
 
def run_menu_estoque(conexao=None):
    conexao_local = conexao is None
    if conexao_local:
        conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)
 
    opcao = 1
 
    while opcao != 9:
        print('''\n=== MÓDULO DE ESTOQUE ===
1) Listar produtos;
2) Cadastrar novo produto;
3) Pesquisar produto pelo código;
4) Atualizar quantidade de um produto;
5) Atualizar preço de um produto;
6) Remover produto pelo código;
7) Ver produtos com estoque baixo;
8) Resumo geral do estoque;
9) Voltar ao menu principal.
''')
        try:
            opcao = int(input("Digite sua opção: "))
        except ValueError:
            print("Opção inválida.")
            continue
 
        if opcao == 1:
            listarProdutos(conexao)
 
        elif opcao == 2:
            novoProduto(conexao)
 
        elif opcao == 3:
            pesquisarProduto(conexao)
 
        elif opcao == 4:
            atualizarQuantidade(conexao)
 
        elif opcao == 5:
            atualizarPreco(conexao)
 
        elif opcao == 6:
            removerProduto(conexao)
 
        elif opcao == 7:
            alertaEstoqueBaixo(conexao)
 
        elif opcao == 8:
            resumoEstoque(conexao)
 
        elif opcao != 9:
            print("Opção Inválida")
 
    if conexao_local:
        encerrarConexao(conexao)
 
 
if __name__ == "__main__":
    run_menu_estoque()
 