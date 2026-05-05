from operacoesbd import *

def listarReclamacoes(conexao):
    consulta = 'select * from Reclamações'
    reclamacoes = listarBancoDados(conexao, consulta)

    if len(reclamacoes) > 0:
        print("-- Lista de Reclamações --")
        for item in reclamacoes:
            print(item[0], "-", item[1])

    else:
        print("Nenhuma reclamação foi encontrada")


def novaReclamacao(conexao):
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


def  pesquisarReclamacao(conexao):
    codigoReclamacao = int(input("Digite o código da Reclamação: "))
    consulta = 'select * from Reclamações where codigo = %s'
    dados = [codigoReclamacao]

    reclamacoes = listarBancoDados(conexao, consulta, dados)

    if len(reclamacoes) > 0:
        print("A reclamação pesquisada foi:", reclamacoes[0][1])
    else:
        print("O código informado não é válido.")


def substituirReclamacao(conexao):
    codigoNovaReclamacao = int(input("Digite o código da reclamação a ser substituida: "))
    novaReclamação = input("Digite a nova reclamação: ")

    consulta = 'UPDATE Reclamações SET reclamacao = %s WHERE codigo = %s'
    dados = [novaReclamação, codigoNovaReclamacao]

    linhasAfetadas = atualizarBancoDados(conexao, consulta, dados)

    if linhasAfetadas == 0:
        print("Não possui nenhuma reclamação para o código informado.")
    else:
        print("Reclamação substituida com sucesso!")

def removerReclamacao(conexao):
    codigoReclamacao = int(input("Digite o código da Reclamação a ser Removida: "))
    consulta = 'delete from Reclamações where codigo = %s'
    dados = [codigoReclamacao]

    linhasAfetadas = excluirBancoDados(conexao, consulta, dados)

    if linhasAfetadas == 0:
        print("O código informado não é válido.")
    else:
        print("Reclamação removida com sucesso!")


def quantidadeReclamacao(conexao):
    consulta = 'select count(*) from Reclamações'
    reclamacoes = listarBancoDados(conexao, consulta)

    total = reclamacoes[0][0]

    if total <= 0:
        print("Atualmente não temos reclamação.")
    elif total == 1:
        print("Atualmente temos", total, "reclamação.")
    else:
        print("Atualmente temos", total, "reclamações.")