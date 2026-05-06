import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from database.operacoesbd import *
from config.config import *

conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)

#usar a conexao

encerrarConexao(conexao)