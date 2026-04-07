from conexao import conectar
from operacoesbd import *

conexao = conectar()
novaReclamacao = (input("Insira sua reclamação: "))

consulta = 'insert into reclamacoes (reclamacao) values (%s);'
reclamacoes = listarBancoDados(conexao,consulta)
dados = [ novaReclamacao ]

codigoNovaReclamacao = insertNoBancoDados(conexao,consulta,dados)

if len(novaReclamacao) > 0:
    reclamacoes .append(novaReclamacao)
    print("Reclamação adicionada com sucesso! \nO código é", codigoNovaReclamacao)
else:
    print("Deve ser inserido ao menos 1 caractere!")

encerrarConexao(conexao)