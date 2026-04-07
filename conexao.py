from operacoesbd import criarConexao
from config import *


def conectar():
    return criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)
