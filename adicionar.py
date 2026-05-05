from operacoesbd import *

conexao = criarConexao("localhost","root","Futebol06!","ouvidoriabd",3306)

novaReclamacao = (input("Insira sua reclamação: "))

consulta = 'insert into Reclamações (reclamacao) values (%s);'
reclamacoes = listarBancoDados(conexao,consulta)
dados = [ novaReclamacao ]

codigoNovaReclamacao = insertNoBancoDados(conexao,consulta,dados)

if len(novaReclamacao) > 0:
    reclamacoes .append(novaReclamacao)
    print("Reclamação adicionada com sucesso! \nO código é", codigoNovaReclamacao)
else:
    print("Deve ser inserido ao menos 1 caractere!")

encerrarConexao(conexao)