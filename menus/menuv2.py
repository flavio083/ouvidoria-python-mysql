import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from services.backend import (listarReclamacoes,novaReclamacao,pesquisarReclamacao,substituirReclamacao,removerReclamacao,quantidadeReclamacao,)

from database.operacoesbd import (criarConexao,encerrarConexao,)

from config.config import (HOST,USER,PASSWORD,DATABASE,PORT,)


def run_menu():
    conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)

    print("Olá, tudo bem?")
    print("Venho aqui desejar as boas vindas á Ouvidoria Unifacisa!")

    opcao = 0

    while opcao != 7:
        print("\n1) Listar Reclamações;")
        print("2) Registrar uma nova reclamação;")
        print("3) Pesquisar uma reclamação pelo código;")
        print("4) Atualizar uma reclamação existente;")
        print("5) Remover uma reclamação pelo código;")
        print("6) Mostrar a quantidade total de reclamações cadastradas;")
        print("7) Opção para sair do sistema.")

        try:
            opcao = int(input("\nDigite sua opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue

        if opcao == 1:
            listarReclamacoes(conexao)

        elif opcao == 2:
            novaReclamacao(conexao)

        elif opcao == 3:
            pesquisarReclamacao(conexao)

        elif opcao == 4:
            substituirReclamacao(conexao)

        elif opcao == 5:
            removerReclamacao(conexao)

        elif opcao == 6:
            quantidadeReclamacao(conexao)

        elif opcao != 7:
            print("Opção inválida")

    encerrarConexao(conexao)
    print("Foi um prazer ter você aqui hoje! \nOuvidoria Unifacisa agradece.")


if __name__ == "__main__":
    run_menu()