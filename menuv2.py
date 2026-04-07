from backend import *
from conexao import conectar

opcao = 1
conexao = conectar()

print("Olá, tudo bem?\nVenho aqui desejar as boas vindas á Ouvidoria Unifacisa!")

while opcao != 7:
    print('''\n1) Listar Reclamações;\n2) Registrar uma nova reclamação;\n3) Pesquisar uma reclamação pelo código;\n4) Atualizar uma reclamação existente;\n5) Remover uma reclamação pelo código;\n6) Mostrar a quantidade total de reclamações cadastradas;\n7) Opção para sair do sistema.
''')
    opcao = int(input("Digite sua opção: "))


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
        print("Opção Inválida")

encerrarConexao(conexao)
print("Foi um prazer ter você aqui hoje! \nOuvidoria Unifacisa agradece.")