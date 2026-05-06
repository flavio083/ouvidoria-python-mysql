import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from database.operacoesbd import *
from config.config import *

conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)

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
