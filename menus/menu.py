# Legacy file kept for compatibility.

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from database.operacoesbd import *
from config.config import *

opcao = 1
conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)

print("Olá, tudo bem?\nVenho aqui desejar as boas vindas á Ouvidoria Unifacisa!")

while opcao != 7:
    print('''\n1) Listar Reclamações;\n2) Registrar uma nova reclamação;\n3) Pesquisar uma reclamação pelo código;\n4) Atualizar uma reclamação existente;\n5) Remover uma reclamação pelo código;\n6) Mostrar a quantidade total de reclamações cadastradas;\n7) Opção para sair do sistema.
''')
    opcao = int(input("Digite sua opção: "))

    
    if opcao == 1:
        consulta = 'select * from Reclamações'
        reclamacoes = listarBancoDados(conexao, consulta)

        if len(reclamacoes) > 0:
            print("-- Lista de Reclamações --")
            for item in reclamacoes:
                print(item[0], "-", item[1])

        else:
            print("Nenhuma reclamação foi encontrada")


    elif opcao == 2:
        novaReclamacao = (input("Insira sua reclamação: "))

        consulta = 'insert into Reclamações (reclamacao) values (%s);'
        reclamacoes = listarBancoDados(conexao, consulta)
        dados = [novaReclamacao]

        codigoNovaReclamacao = insertNoBancoDados(conexao, consulta, dados)

        if len(novaReclamacao) > 0:
            reclamacoes.append(novaReclamacao)
            print("Reclamação adicionada com sucesso! \nO código é", codigoNovaReclamacao)
        else:
            print("Deve ser inserido ao menos 1 caractere!")



    elif opcao == 3:
        codigoReclamacao = int(input("Digite o código da Reclamação: "))
        consulta = 'select * from Reclamações where codigo = %s'
        dados = [codigoReclamacao]

        reclamacoes = listarBancoDados(conexao, consulta, dados)

        if len(reclamacoes) > 0:
            print("A reclamação pesquisada foi:", reclamacoes[0][1])
        else:
            print("O código informado não é válido.")
    
  

    elif opcao == 4:
        codigoNovaReclamacao = int(input("Digite o código da reclamação a ser substituida: "))
        novaReclamação = input("Digite a nova reclamação: ")

        consulta = 'UPDATE Reclamações SET reclamacao = %s WHERE codigo = %s'
        dados = [novaReclamação, codigoNovaReclamacao]

        linhasAfetadas = atualizarBancoDados(conexao, consulta, dados)

        if linhasAfetadas == 0:
            print("Não possui nenhuma reclamação para o código informado.")
        else:
            print("Reclamação substituida com sucesso!")
       
    

    elif opcao == 5:
        codigoReclamacao = int(input("Digite o código da Reclamação a ser Removida: "))
        consulta = 'delete from Reclamações where codigo = %s'
        dados = [codigoReclamacao]

        linhasAfetadas = excluirBancoDados(conexao, consulta, dados)

        if linhasAfetadas == 0:
            print("O código informado não é válido.")
        else:
            print("Reclamação removida com sucesso!")

    

    elif opcao == 6:
        consulta = 'select count(*) from Reclamações'
        reclamacoes = listarBancoDados(conexao, consulta)

        total = reclamacoes[0][0]

        if total <= 0:
            print("Atualmente não temos reclamação.")
        elif total == 1:
            print("Atualmente temos", total, "reclamação.")
        else:
            print("Atualmente temos", total, "reclamações.")

    elif opcao != 7:
        print("Opção Inválida")

encerrarConexao(conexao)
print("Foi um prazer ter você aqui hoje! \nOuvidoria Unifacisa agradece.")
