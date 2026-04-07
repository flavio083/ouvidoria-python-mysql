# Sistema de Ouvidoria 

## 📋 Visão Geral

Sistema de gerenciamento de reclamações desenvolvido em Python com integração a banco de dados MySQL. O projeto permite listar, registrar, pesquisar, atualizar e remover reclamações enviadas pelos usuários da Ouvidoria da Universidade Unifacisa.

---

## 📁 Estrutura do Projeto

```
OuvidoriaBDGIT/
├── menuv2.py           # Interface principal (Menu interativo)
├── backend.py          # Lógica de negócio (Funções de operação)
├── operacoesbd.py      # Biblioteca de acesso ao banco de dados
├── conexao.py          # Configuração de conexão
├── config.py           # Configurações do sistema
└── [outros arquivos]   # Arquivos auxiliares
```

---

## 🎯 Funcionamento do arquivo menuv2.py

O arquivo `menuv2.py` é a **interface principal do sistema** responsável por gerenciar a interação com o usuário.

### Características principais:

- **Menu Interativo**: Apresenta 7 opções para o usuário escolher
- **Loop Contínuo**: Permanece em execução até o usuário selecionar a opção de sair (opção 7)
- **Tratamento de Conexão**: Estabelece conexão com o banco de dados ao iniciar e a encerra ao finalizar

### Fluxo de Execução:

```
1. Exibe mensagem de boas-vindas
2. Estabelece conexão com o banco de dados via conexao.conectar()
3. Entra em loop infinito mostrando o menu
4. Aguarda entrada do usuário (1-7)
5. Executa função correspondente à opção selecionada
6. Retorna ao menu (até selecionar opção 7)
7. Fecha a conexão e encerra o programa
```

### Opções do Menu:

| Opção | Descrição | Método Backend |
|-------|-----------|---|
| 1 | Listar Reclamações | `listarReclamacoes()` |
| 2 | Registrar nova reclamação | `novaReclamacao()` |
| 3 | Pesquisar reclamação pelo código | `pesquisarReclamacao()` |
| 4 | Atualizar reclamação existente | `substituirReclamacao()` |
| 5 | Remover reclamação pelo código | `removerReclamacao()` |
| 6 | Mostrar quantidade total de reclamações | `quantidadeReclamacao()` |
| 7 | Sair do sistema | `encerrarConexao()` |

### Código do Menu:

```python
from backend import *
from conexao import conectar

opcao = 1
conexao = conectar()

# Loop principal que mantém o menu aberto
while opcao != 7:
    # Exibe opções e captura entrada do usuário
    opcao = int(input("Digite sua opção: "))
    
    # Chama função correspondente do backend
    if opcao == 1:
        listarReclamacoes(conexao)
    # ... e assim por diante
```

---

## 🔧 Métodos em backend.py

O arquivo `backend.py` contém **6 funções principais** que implementam a lógica de negócio. Cada função interage com o banco de dados através da biblioteca `operacoesbd.py`.

### 1. **listarReclamacoes(conexao)**

**Objetivo**: Exibir todas as reclamações cadastradas no banco de dados.

**Funcionamento**:
- Executa consulta SQL: `SELECT * FROM reclamacoes`
- Utiliza método: `listarBancoDados()` da biblioteca operacoesbd
- Se encontrar registros, exibe código e texto de cada reclamação
- Se não houver registros, exibe mensagem de aviso

**Código**:
```python
def listarReclamacoes(conexao):
    consulta = 'select * from reclamacoes'
    reclamacoes = listarBancoDados(conexao, consulta)
    
    if len(reclamacoes) > 0:
        for item in reclamacoes:
            print(item[0], "-", item[1])  # item[0] = código, item[1] = texto
    else:
        print("Nenhuma reclamação foi encontrado")
```

---

### 2. **novaReclamacao(conexao)**

**Objetivo**: Registrar uma nova reclamação no banco de dados.

**Funcionamento**:
- Solicita ao usuário o texto da reclamação
- Executa comando SQL: `INSERT INTO reclamacoes (reclamacao) VALUES (%s)`
- Utiliza método: `insertNoBancoDados()` da biblioteca operacoesbd
- Retorna o ID da nova reclamação gerado pelo banco de dados
- Valida se o texto tem ao menos 1 caractere

**Código**:
```python
def novaReclamacao(conexao):
    novaReclamacao = input("Insira sua reclamação: ")
    consulta = 'insert into reclamacoes (reclamacao) values (%s);'
    dados = [novaReclamacao]
    
    codigoNovaReclamacao = insertNoBancoDados(conexao, consulta, dados)
    
    if len(novaReclamacao) > 0:
        print("Reclamação adicionada com sucesso! \nO código é", codigoNovaReclamacao)
    else:
        print("Deve ser inserido ao menos 1 caractere!")
```

---

### 3. **pesquisarReclamacao(conexao)**

**Objetivo**: Buscar uma reclamação específica pelo seu código.

**Funcionamento**:
- Solicita o código da reclamação ao usuário
- Executa consulta: `SELECT * FROM reclamacoes WHERE codigo = %s`
- Utiliza método: `listarBancoDados()` com parâmetro
- Se encontrar, exibe o texto da reclamação
- Se não encontrar, exibe mensagem de código inválido

**Código**:
```python
def pesquisarReclamacao(conexao):
    codigoReclamacao = int(input("Digite o código da Reclamação: "))
    consulta = 'select * from reclamacoes where codigo = %s'
    dados = [codigoReclamacao]
    
    reclamacoes = listarBancoDados(conexao, consulta, dados)
    
    if len(reclamacoes) > 0:
        print("A reclamação pesquisada foi:", reclamacoes[0][1])
    else:
        print("O código informado não é válido.")
```

---

### 4. **substituirReclamacao(conexao)**

**Objetivo**: Atualizar o texto de uma reclamação existente.

**Funcionamento**:
- Solicita código da reclamação a ser atualizada
- Solicita novo texto da reclamação
- Executa comando: `UPDATE reclamacoes SET reclamacao = %s WHERE codigo = %s`
- Utiliza método: `atualizarBancoDados()` da biblioteca operacoesbd
- Verifica quantas linhas foram afetadas pela atualização

**Código**:
```python
def substituirReclamacao(conexao):
    codigoNovaReclamacao = int(input("Digite o código da reclamação a ser substituida: "))
    novaReclamação = input("Digite a nova reclamação: ")
    
    consulta = 'UPDATE reclamacoes SET reclamacao = %s WHERE codigo = %s'
    dados = [novaReclamação, codigoNovaReclamacao]
    
    linhasAfetadas = atualizarBancoDados(conexao, consulta, dados)
    
    if linhasAfetadas == 0:
        print("Não possui nenhuma reclamação para o código informado.")
    else:
        print("Reclamação substituida com sucesso!")
```

---

### 5. **removerReclamacao(conexao)**

**Objetivo**: Deletar uma reclamação do banco de dados.

**Funcionamento**:
- Solicita código da reclamação a ser removida
- Executa comando: `DELETE FROM reclamacoes WHERE codigo = %s`
- Utiliza método: `excluirBancoDados()` da biblioteca operacoesbd
- Verifica se o código era válido através da contagem de linhas afetadas

**Código**:
```python
def removerReclamacao(conexao):
    codigoReclamacao = int(input("Digite o código da Reclamação a ser Removida: "))
    consulta = 'delete from reclamacoes where codigo = %s'
    dados = [codigoReclamacao]
    
    linhasAfetadas = excluirBancoDados(conexao, consulta, dados)
    
    if linhasAfetadas == 0:
        print("O código informado não é válido.")
    else:
        print("Reclamação removida com sucesso!")
```

---

### 6. **quantidadeReclamacao(conexao)**

**Objetivo**: Exibir o total de reclamações cadastradas.

**Funcionamento**:
- Executa consulta de contagem: `SELECT COUNT(*) FROM reclamacoes`
- Utiliza método: `listarBancoDados()` da biblioteca operacoesbd
- Extrai o valor total (primeiro elemento do resultado)
- Exibe mensagem personalizada de acordo com a quantidade

**Código**:
```python
def quantidadeReclamacao(conexao):
    consulta = 'select count(*) from reclamacoes'
    reclamacoes = listarBancoDados(conexao, consulta)
    
    total = reclamacoes[0][0]
    
    if total <= 0:
        print("Atualmente não temos reclamação.")
    elif total == 1:
        print("Atualmente temos", total, "reclamação.")
    else:
        print("Atualmente temos", total, "reclamações.")
```

---

## 📦 Explicação da Biblioteca operacoesbd.py

A biblioteca `operacoesbd.py` é a **camada de acesso ao banco de dados** que fornece funções reutilizáveis para executar operações CRUD (Create, Read, Update, Delete) de forma segura e estruturada.

### Dependências:
```python
import mysql.connector  # Biblioteca oficial do MySQL para Python
```

---

### Funções da Biblioteca:

#### 1. **criarConexao(endereco, usuario, senha, bancodedados, porta)**

**Objetivo**: Estabelecer conexão com o banco de dados MySQL.

**Parâmetros**:
- `endereco`: IP ou hostname do servidor MySQL
- `usuario`: Usuário do banco de dados
- `senha`: Senha do usuário
- `bancodedados`: Nome do banco de dados
- `porta`: Porta de acesso (padrão: 3306)

**Retorna**: Objeto de conexão ou `None` se falhar

**Características**:
- Trata exceções de conexão
- Exibe mensagem de erro em caso de falha

```python
def criarConexao(endereco, usuario, senha, bancodedados, porta):
    try:
        return mysql.connector.connect(
            host=endereco,
            port=porta,
            user=usuario,
            password=senha,
            database=bancodedados
        )
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None
```

---

#### 2. **encerrarConexao(connection)**

**Objetivo**: Fechar a conexão com o banco de dados.

**Parâmetro**:
- `connection`: Objeto de conexão retornado por `criarConexao()`

**Funcionamento**:
- Verifica se a conexão está ativa
- Fecha a conexão de forma segura

```python
def encerrarConexao(connection):
    if connection:
        connection.close()
```

---

#### 3. **insertNoBancoDados(connection, sql, dados)**

**Objetivo**: Inserir dados no banco de dados com prepared statements.

**Parâmetros**:
- `connection`: Objeto de conexão ativa
- `sql`: Comando SQL com placeholders `%s`
- `dados`: Lista de valores para inserir

**Retorna**: ID da linha inserida (lastrowid) ou `None` se erro

**Características**:
- Usa **prepared statements** para evitar SQL injection
- Faz commit automático
- Reverte transação em caso de erro (rollback)
- Trata exceções do MySQL

```python
def insertNoBancoDados(connection, sql, dados):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, dados)
        connection.commit()
        id = cursor.lastrowid
    except mysql.connector.Error as err:
        print(f"Erro ao inserir no banco de dados: {err}")
        connection.rollback()
        return None
    finally:
        cursor.close()
    return id
```

**Exemplo de uso**:
```python
sql = 'INSERT INTO reclamacoes (reclamacao) VALUES (%s)'
dados = ['Esta é uma reclamação']
id = insertNoBancoDados(conexao, sql, dados)
print(f"Reclamação inserida com ID: {id}")
```

---

#### 4. **listarBancoDados(connection, sql, params=None)**

**Objetivo**: Consultar dados do banco de dados.

**Parâmetros**:
- `connection`: Objeto de conexão ativa
- `sql`: Comando SQL SELECT
- `params`: Lista de parâmetros (opcional)

**Retorna**: Lista de tuplas com os resultados ou lista vazia se erro

**Características**:
- Suporta consultas com e sem parâmetros
- Usa prepared statements
- Retorna todos os resultados com `fetchall()`
- Trata exceções

```python
def listarBancoDados(connection, sql, params=None):
    try:
        cursor = connection.cursor(prepared=True)
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Erro ao listar do banco de dados: {err}")
        return []
    finally:
        cursor.close()
    return results
```

**Exemplos de uso**:
```python
# Sem parâmetros
todas = listarBancoDados(conexao, 'SELECT * FROM reclamacoes')

# Com parâmetros
codigo = 5
resultado = listarBancoDados(conexao, 'SELECT * FROM reclamacoes WHERE codigo = %s', [codigo])
```

---

#### 5. **atualizarBancoDados(connection, sql, dados)**

**Objetivo**: Atualizar registros no banco de dados.

**Parâmetros**:
- `connection`: Objeto de conexão ativa
- `sql`: Comando SQL UPDATE com placeholders
- `dados`: Lista de valores para atualizar

**Retorna**: Número de linhas afetadas pela atualização

**Características**:
- Usa prepared statements
- Faz commit automático
- Reverte em caso de erro (rollback)
- Retorna contagem de linhas modificadas

```python
def atualizarBancoDados(connection, sql, dados):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, dados)
        connection.commit()
        linhasAfetadas = cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar o banco de dados: {err}")
        connection.rollback()
        return 0
    finally:
        cursor.close()
    return linhasAfetadas
```

**Exemplo de uso**:
```python
sql = 'UPDATE reclamacoes SET reclamacao = %s WHERE codigo = %s'
dados = ['Reclamação atualizada', 5]
linhas = atualizarBancoDados(conexao, sql, dados)
if linhas > 0:
    print(f"Atualizadas {linhas} linha(s)")
```

---

#### 6. **excluirBancoDados(connection, sql, dados)**

**Objetivo**: Deletar registros do banco de dados.

**Parâmetros**:
- `connection`: Objeto de conexão ativa
- `sql`: Comando SQL DELETE com placeholders
- `dados`: Lista de valores para identificar o que deletar

**Retorna**: Número de linhas deletadas

**Características**:
- Usa prepared statements
- Faz commit automático
- Reverte em caso de erro (rollback)
- Retorna contagem de linhas apagadas

```python
def excluirBancoDados(connection, sql, dados):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, dados)
        connection.commit()
        linhasAfetadas = cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Erro ao excluir do banco de dados: {err}")
        connection.rollback()
        return 0
    finally:
        cursor.close()
    return linhasAfetadas
```

**Exemplo de uso**:
```python
sql = 'DELETE FROM reclamacoes WHERE codigo = %s'
dados = [5]
linhas = excluirBancoDados(conexao, sql, dados)
if linhas > 0:
    print(f"Deletadas {linhas} linha(s)")
else:
    print("Nenhum registro encontrado com esse código")
```

---

## 🔒 Recursos de Segurança

A biblioteca `operacoesbd.py` implementa várias boas práticas de segurança:

1. **Prepared Statements**: Previnem SQL injection usando placeholders `%s`
2. **Transactions (Commit/Rollback)**: Mantêm integridade dos dados
3. **Try-Except**: Tratamento de exceções e erros de conexão
4. **Cursor Management**: Fecha cursores após uso para liberar recursos
5. **Parâmetros Seguros**: Dados separados do SQL

---

## 🚀 Como Executar

```bash
# 1. Instalar dependências
pip install mysql-connector-python

# 2. Configurar credenciais do banco (em config.py ou conexao.py)

# 3. Executar o programa
python menuv2.py
```

---

## 📊 Fluxo de Dados

```
menuv2.py (Interface)
    ↓
backend.py (Lógica)
    ↓
operacoesbd.py (Acesso ao BD)
    ↓
Banco de Dados MySQL
```

---

## 📝 Resumo

| Arquivo | Responsabilidade |
|---------|---|
| **menuv2.py** | Interface interativa com usuário |
| **backend.py** | Lógica de negócio (CRUD operações) |
| **operacoesbd.py** | Comunicação com banco de dados (prepared statements seguro) |
| **conexao.py** | Gerenciamento de conexão |
| **config.py** | Configurações do sistema |

---

## ✅ Conclusão

Este sistema de ouvidoria é estruturado em três camadas bem definidas:
- **Apresentação**: Captura entrada do usuário
- **Negócio**: Processa as operações
- **Acesso**: Comunica com o banco de dados de forma segura

A separação de responsabilidades facilita manutenção, testes e futuras expansões do sistema.
