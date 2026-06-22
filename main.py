import sys
from pathlib import Path
 
sys.path.insert(0, str(Path(__file__).parent))
 
from config.config import HOST, USER, PASSWORD, DATABASE, PORT
from database.operacoesbd import criarConexao, encerrarConexao
from menus.menuv2 import run_menu as run_menu_ouvidoria
from menus.menu_estoque import run_menu_estoque
 
 
def main():
    conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)
 
    print("Olá, seja bem-vindo ao sistema!")
 
    opcao = 1
 
    while opcao != 3:
        print('''\n=== MENU PRINCIPAL ===
1) Ouvidoria;
2) Estoque;
3) Sair.
''')
        try:
            opcao = int(input("Digite sua opção: "))
        except ValueError:
            print("Opção inválida.")
            continue
 
        if opcao == 1:
            run_menu_ouvidoria(conexao)
 
        elif opcao == 2:
            run_menu_estoque(conexao)
 
        elif opcao != 3:
            print("Opção Inválida")
 
    encerrarConexao(conexao)
    print("Até logo!")
 
 
if __name__ == "__main__":
    main()