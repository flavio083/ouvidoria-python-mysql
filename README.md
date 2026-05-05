# 🎯 Ouvidoria BDGIT - Complaint Management System

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/mysql-8.0%2B-orange)](https://www.mysql.com/)
[![Status](https://img.shields.io/badge/status-Active-success)](https://github.com/flavio083/ouvidoriaintegrabd)

A Python-based **Complaint Management System** with MySQL database integration. This project implements CRUD operations for managing complaints with a command-line interface and modular database abstraction layer.

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Database Schema](#-database-schema)
- [Project Architecture](#-project-architecture)
- [File Structure & Modules](#-file-structure--modules)
- [Core Modules](#-core-modules)
- [Technologies](#-technologies)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Database Setup](#-database-setup)
- [How to Run](#-how-to-run)
- [Usage Examples](#-usage-examples)
- [Module Documentation](#-module-documentation)
- [Code Structure Details](#-code-structure-details)
- [Author](#-author)

## 📖 Project Overview

**Ouvidoria BDGIT** is a complaint/feedback management system designed for the UNIFACISA Ombudsman's Office. The system allows users to:

- **Register** new complaints via text input
- **List** all registered complaints with ID and description
- **Search** for specific complaints by complaint code
- **Update** complaint descriptions
- **Delete** complaints from the database
- **Count** total number of registered complaints

The project uses a **layered architecture** with separate modules for database operations, business logic, and user interface.

## 🗄️ Database Schema

### Table: `Reclamações`

```sql
CREATE TABLE Reclamações (
    codigo INT PRIMARY KEY AUTO_INCREMENT,
    reclamacao TEXT NOT NULL
);
```

| Column | Type | Constraints |
|--------|------|------------|
| `codigo` | INT | PRIMARY KEY, AUTO_INCREMENT |
| `reclamacao` | TEXT | NOT NULL |

**Current Table Name**: `Reclamações` (with accent)  
**Database Name**: `ouvidoriabd`

---

## 🏗️ Project Architecture

```
┌────────────────────────────────────┐
│  Presentation Layer (CLI)          │
│  - menuv2.py (Main menu)           │
│  - menu.py (Alternative menu)      │
│  - Standalone scripts              │
├────────────────────────────────────┤
│  Backend/Business Logic            │
│  - backend.py (6 business functions) │
├────────────────────────────────────┤
│  Data Access Layer (Database)      │
│  - operacoesbd.py (6 DB functions) │
├────────────────────────────────────┤
│  Configuration                     │
│  - config.py (MySQL connection)    │
│  - config_exemplo.py (template)    │
└────────────────────────────────────┘
```

### Architecture Notes

⚠️ **Current Implementation Pattern**:
- `menuv2.py` implements logic **inline** (does not call `backend.py` functions)
- `menu.py` also implements logic **inline**
- `backend.py` contains abstracted functions but is **not called** by the main menu
- Standalone scripts directly import `operacoesbd.py` and repeat connection/logic code

---

## 📁 File Structure & Modules

```
OuvidoriaBDGIT/
├── operacoesbd.py              # Database abstraction layer ⭐
├── backend.py                  # Business logic functions (not used by menus)
├── menuv2.py                   # Main interactive menu (RECOMMENDED)
├── menu.py                     # Alternative menu version
├── main.py                     # Template file (connection only)
├── adicionar.py                # Standalone: Create complaint
├── listar.py                   # Standalone: List complaints
├── pesquisar.py                # Standalone: Search complaint
├── substituir.py               # Standalone: Update complaint
├── remover.py                  # Standalone: Delete complaint
├── quantidade.py               # Standalone: Count complaints
├── config_exemplo.py           # Configuration template (example)
├── config.py                   # Configuration (actual credentials - NOT in git)
└── requirements.txt            # Python dependencies
```

---

## ⚙️ Core Modules

### 1. **operacoesbd.py** - Data Access Layer

**Purpose**: Database abstraction with prepared statements and error handling

**Imports**:
```python
import mysql.connector
```

**Functions**:

#### `criarConexao(endereco, usuario, senha, bancodedados, porta)`
Creates MySQL connection with error handling.
- **Parameters**: Host, username, password, database name, port
- **Returns**: Connection object or `None` if error
- **Error Handling**: Catches `mysql.connector.Error`

```python
conexao = criarConexao("localhost", "root", "password", "ouvidoriabd", 3306)
```

---

#### `encerrarConexao(connection)`
Safely closes database connection.
- **Parameters**: Connection object
- **Returns**: None

```python
encerrarConexao(conexao)
```

---

#### `insertNoBancoDados(connection, sql, dados)`
Inserts data with prepared statements and transaction support.
- **Parameters**:
  - `connection`: Active connection
  - `sql`: SQL with `%s` placeholders
  - `dados`: List of values to insert
- **Returns**: Last inserted row ID or `None` on error
- **Features**: Prepared statements, AUTO_COMMIT, ROLLBACK on error

```python
sql = 'insert into Reclamações (reclamacao) values (%s)'
dados = ['Nova reclamação']
novo_id = insertNoBancoDados(conexao, sql, dados)
```

---

#### `listarBancoDados(connection, sql, params=None)`
Retrieves data from database with optional parameters.
- **Parameters**:
  - `connection`: Active connection
  - `sql`: SELECT query
  - `params`: Optional list of parameters for WHERE clause
- **Returns**: List of tuples (results) or empty list on error
- **Features**: Prepared statements, supports parameterized queries

```python
# Without parameters
todos = listarBancoDados(conexao, 'select * from Reclamações')

# With parameters
sql = 'select * from Reclamações where codigo = %s'
resultado = listarBancoDados(conexao, sql, [1])
```

---

#### `atualizarBancoDados(connection, sql, dados)`
Updates records with transaction management.
- **Parameters**:
  - `connection`: Active connection
  - `sql`: UPDATE query with placeholders
  - `dados`: Values to update
- **Returns**: Number of affected rows (0 if no match)
- **Features**: Prepared statements, ROLLBACK on error

```python
sql = 'UPDATE Reclamações SET reclamacao = %s WHERE codigo = %s'
dados = ['Reclamação atualizada', 1]
linhas = atualizarBancoDados(conexao, sql, dados)
```

---

#### `excluirBancoDados(connection, sql, dados)`
Deletes records with error handling and rollback.
- **Parameters**:
  - `connection`: Active connection
  - `sql`: DELETE query with placeholders
  - `dados`: Values to identify records
- **Returns**: Number of deleted rows (0 if no match)
- **Features**: Prepared statements, ROLLBACK on error

```python
sql = 'delete from Reclamações where codigo = %s'
dados = [1]
deletados = excluirBancoDados(conexao, sql, dados)
```

---

### 2. **backend.py** - Business Logic Layer

**Purpose**: High-level complaint operations (abstracted functions)

**Imports**:
```python
from operacoesbd import *  # Imports all 6 database functions
```

**⚠️ NOTE**: These functions are defined but **NOT CALLED** by `menuv2.py` or `menu.py`. They are available for import but the current menus implement logic inline.

**Functions**:

#### `listarReclamacoes(conexao)`
Lists all complaints.
- **Input**: Connection object
- **Output**: Prints formatted list or "Nenhuma reclamação foi encontrada"

```python
from backend import *
listarReclamacoes(conexao)
```

---

#### `novaReclamacao(conexao)`
Creates new complaint.
- **Input**: Connection object (prompts user for complaint text)
- **Output**: Success message with new complaint ID or error message

---

#### `pesquisarReclamacao(conexao)`
Searches for complaint by code.
- **Input**: Connection object (prompts user for complaint code)
- **Output**: Complaint text if found or error message

---

#### `substituirReclamacao(conexao)`
Updates complaint description.
- **Input**: Connection object (prompts user for code and new description)
- **Output**: Success message or error message

---

#### `removerReclamacao(conexao)`
Deletes complaint by code.
- **Input**: Connection object (prompts user for complaint code)
- **Output**: Success message or error message

---

#### `quantidadeReclamacao(conexao)`
Displays total complaint count.
- **Input**: Connection object
- **Output**: Formatted message with complaint count

---

### 3. **menuv2.py** - Main Interactive Menu (RECOMMENDED)

**Purpose**: Primary user interface for complaint management

**Imports**:
```python
from backend import *  # Imports database functions
```

**Connection Details** (Hardcoded):
```python
conexao = criarConexao("localhost", "root", "Futebol06!", "ouvidoriabd", 3306)
```

**Menu Structure**:
- Displays 7 menu options in a loop
- Continues until user selects option 7 (exit)
- Each option implements logic **inline** instead of calling `backend.py` functions

**Menu Options**:

| Option | Operation | SQL Query |
|--------|-----------|-----------|
| 1 | List all complaints | `select * from Reclamações` |
| 2 | Register new complaint | `insert into Reclamações (reclamacao) values (%s)` |
| 3 | Search by code | `select * from Reclamações where codigo = %s` |
| 4 | Update complaint | `UPDATE Reclamações SET reclamacao = %s WHERE codigo = %s` |
| 5 | Delete complaint | `delete from Reclamações where codigo = %s` |
| 6 | Count total | `select count(*) from Reclamações` |
| 7 | Exit | `encerrarConexao(conexao)` |

---

### 4. **menu.py** - Alternative Menu

**Purpose**: Alternative interactive menu (similar to `menuv2.py`)

**Imports**:
```python
from operacoesbd import *
```

**Connection Details** (Hardcoded):
```python
conexao = criarConexao("localhost", "root", "Futebol06!", "ouvidoriabd", 3306)
```

**Implementation**: Follows same pattern as `menuv2.py` with inline logic

---

### 5. **Standalone Scripts**

Each script is independent, creates own connection, performs one operation, then closes connection.

#### **adicionar.py** - Add Complaint
```python
from operacoesbd import *
conexao = criarConexao("localhost", "root", "Futebol06!", "ouvidoriabd", 3306)
# Prompts for complaint text
# Inserts into database
# Closes connection
```

---

#### **listar.py** - List Complaints
```python
from operacoesbd import *
conexao = criarConexao("localhost", "root", "Futebol06!", "ouvidoriabd", 3306)
# Retrieves all complaints
# Prints list
# Closes connection
```

---

#### **pesquisar.py** - Search Complaint
```python
from operacoesbd import *
conexao = criarConexao("localhost", "root", "Futebol06!", "ouvidoriabd", 3306)
# Prompts for complaint code
# Retrieves matching complaint
# Prints result
# Closes connection
```

---

#### **substituir.py** - Update Complaint
```python
from operacoesbd import *
conexao = criarConexao("localhost", "root", "Futebol06!", "ouvidoriabd", 3306)
# Prompts for code and new description
# Updates database
# Prints result
# Closes connection
```

---

#### **remover.py** - Delete Complaint
```python
from operacoesbd import *
conexao = criarConexao("localhost", "root", "Futebol06!", "ouvidoriabd", 3306)
# Prompts for complaint code
# Deletes from database
# Prints result
# Closes connection
```

---

#### **quantidade.py** - Count Complaints
```python
from operacoesbd import *
conexao = criarConexao("localhost", "root", "Futebol06!", "ouvidoriabd", 3306)
# Counts total complaints
# Prints count
# Closes connection
```

---

### 6. **main.py** - Template File

**Purpose**: Template/starter file

**Content**:
```python
from operacoesbd import *

conexao = criarConexao("localhost", "root", "Futebol06!", "ouvidoriabd", 3306)
# uso da conexao
encerrarConexao(conexao)
```

**Status**: Contains only connection setup, no actual operations

---

### 7. **config.py** - Actual Configuration

**Content** (Hardcoded credentials):
```python
HOST = "localhost"
USER = "root"
PASSWORD = "Futebol06!"
DATABASE = "ouvidoriabd"
PORT = 3306
```

**Note**: Not currently used by any module (credentials are hardcoded directly in files)

---

### 8. **config_exemplo.py** - Configuration Template

**Purpose**: Template for configuration

**Content**:
```python
HOST = "localhost"
USER = "root"
PASSWORD = "your_password_here"
DATABASE = "ouvidoriabd"
PORT = 3306
```

---

## 🛠️ Technologies

| Technology | Version | Usage |
|-----------|---------|-------|
| Python | 3.8+ | Core language |
| MySQL | 8.0+ | Database |
| mysql-connector-python | 8.0+ | Python-MySQL driver |

**Python Imports Used**:
- `mysql.connector` - MySQL database connection

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- MySQL Server 8.0+
- pip package manager

### Step 1: Clone Repository

```bash
git clone https://github.com/flavio083/ouvidoriaintegrabd.git
cd OuvidoriaBDGIT
```

### Step 2: Create Virtual Environment

**Windows**:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt contents**:
```
mysql-connector-python==8.0.33
```

### Step 4: Verify Installation

```bash
python -c "import mysql.connector; print('MySQL Connector installed')"
```

---

## ⚙️ Configuration

### Current State

⚠️ **Credentials are HARDCODED in source files**:
- `menuv2.py`: `criarConexao("localhost","root","Futebol06!","ouvidoriabd",3306)`
- `menu.py`: Same credentials
- All standalone scripts: Same credentials
- `config.py` and `config_exemplo.py` exist but are NOT USED

### Recommended Configuration Approach

1. **Copy template** (optional):
   ```bash
   cp config_exemplo.py config.py
   ```

2. **Update credentials** in one central place (pending refactoring)

3. **Import from config** instead of hardcoding:
   ```python
   from config import HOST, USER, PASSWORD, DATABASE, PORT
   conexao = criarConexao(HOST, USER, PASSWORD, DATABASE, PORT)
   ```

---

## 🗄️ Database Setup

### Step 1: Create Database

```sql
CREATE DATABASE ouvidoriabd CHARACTER SET utf8mb4;
```

### Step 2: Create Table

```sql
USE ouvidoriabd;

CREATE TABLE Reclamações (
    codigo INT PRIMARY KEY AUTO_INCREMENT,
    reclamacao TEXT NOT NULL
);
```

### Step 3: Sample Data (Optional)

```sql
INSERT INTO Reclamações (reclamacao) VALUES 
('Problema com servidor de email'),
('Sistema lento demais'),
('Falta de documentação');
```

### Step 4: Verify

```sql
SELECT * FROM Reclamações;
```

---

## 🚀 How to Run

### Option 1: Main Interactive Menu (RECOMMENDED)

```bash
python menuv2.py
```

**Output**:
```
Olá, tudo bem?
Venho aqui desejar as boas vindas á Ouvidoria Unifacisa!

1) Listar Reclamações;
2) Registrar uma nova reclamação;
3) Pesquisar uma reclamação pelo código;
4) Atualizar uma reclamação existente;
5) Remover uma reclamação pelo código;
6) Mostrar a quantidade total de reclamações cadastradas;
7) Opção para sair do sistema.

Digite sua opção: 
```

### Option 2: Alternative Menu

```bash
python menu.py
```

### Option 3: Standalone Scripts

```bash
python listar.py        # List all complaints
python adicionar.py     # Add new complaint
python pesquisar.py     # Search complaint
python substituir.py    # Update complaint
python remover.py       # Delete complaint
python quantidade.py    # Count complaints
```

---

## 📖 Usage Examples

### Example 1: List All Complaints

```
Digite sua opção: 1

-- Lista de Reclamações --
1 - Problema com servidor de email
2 - Sistema lento demais
3 - Falta de documentação
```

### Example 2: Add New Complaint

```
Digite sua opção: 2
Insira sua reclamação: Ar condicionado não funciona
Reclamação adicionada com sucesso! 
O código é 4
```

### Example 3: Search Complaint

```
Digite sua opção: 3
Digite o código da Reclamação: 2
A reclamação pesquisada foi: Sistema lento demais
```

### Example 4: Update Complaint

```
Digite sua opção: 4
Digite o código da reclamação a ser substituida: 2
Digite a nova reclamação: Sistema crítico - EXTREMAMENTE lento
Reclamação substituida com sucesso!
```

### Example 5: Delete Complaint

```
Digite sua opção: 5
Digite o código da Reclamação a ser Removida: 2
Reclamação removida com sucesso!
```

### Example 6: View Count

```
Digite sua opção: 6
Atualmente temos 5 reclamações.
```

---

## 📚 Module Documentation

### Database Layer (`operacoesbd.py`)

**Error Handling Pattern**:
```python
try:
    cursor = connection.cursor(prepared=True)
    cursor.execute(sql, dados)
    connection.commit()
    # ... return results
except mysql.connector.Error as err:
    print(f"Erro ao [operation]: {err}")
    connection.rollback()  # Transaction rollback on error
    # ... return default value
finally:
    cursor.close()  # Always close cursor
```

**Key Features**:
- ✅ Prepared statements (`prepared=True`) - prevents SQL injection
- ✅ Transaction management (`commit()`, `rollback()`)
- ✅ Error handling (`mysql.connector.Error`)
- ✅ Resource cleanup (`cursor.close()`)

---

### SQL Queries Used

| Operation | Query |
|-----------|-------|
| Create | `insert into Reclamações (reclamacao) values (%s)` |
| Read All | `select * from Reclamações` |
| Read One | `select * from Reclamações where codigo = %s` |
| Update | `UPDATE Reclamações SET reclamacao = %s WHERE codigo = %s` |
| Delete | `delete from Reclamações where codigo = %s` |
| Count | `select count(*) from Reclamações` |

---

## 🔍 Code Structure Details

### Import Pattern

**All files use**:
```python
from operacoesbd import *
```

This imports all 6 database functions globally.

---

### Connection Pattern

**All files use** (hardcoded):
```python
conexao = criarConexao("localhost", "root", "Futebol06!", "ouvidoriabd", 3306)
```

---

### Menu Loop Pattern (menuv2.py/menu.py)

```python
opcao = 1
while opcao != 7:
    # Display menu
    print(menu_options)
    
    # Get user input
    opcao = int(input("Digite sua opção: "))
    
    # Execute corresponding operation
    if opcao == 1:
        # Inline logic for list
    elif opcao == 2:
        # Inline logic for create
    # ... etc
    
# Close connection after loop
encerrarConexao(conexao)
```

---

### Standalone Script Pattern

```python
from operacoesbd import *

# Create connection
conexao = criarConexao("localhost", "root", "Futebol06!", "ouvidoriabd", 3306)

# Get user input
user_input = input("Prompt: ")

# Build query
sql = "..."
dados = [user_input]

# Execute operation
resultado = listarBancoDados(conexao, sql, dados)  # or insert/update/delete

# Print results
print(resultado)

# Close connection
encerrarConexao(conexao)
```

---

## 👨‍💻 Author

**Flavio Silva**

- GitHub: [@flavio083](https://github.com/flavio083)
- Repository: [ouvidoriaintegrabd](https://github.com/flavio083/ouvidoriaintegrabd)

---

## 📝 Notes & Observations

### Current Implementation Status

✅ **What Works**:
- Database abstraction layer (`operacoesbd.py`)
- All CRUD operations functional
- Error handling and transaction management
- Interactive menu interface
- Multiple entry points (menu vs standalone scripts)

⚠️ **Areas for Improvement**:
- Backend functions (`backend.py`) defined but not used by menus
- Credentials hardcoded in all files (not externalized)
- Code duplication across menu and standalone scripts
- `config.py` defined but not imported by any module
- `main.py` is only a template

### Recommended Refactoring

1. **Consolidate configuration**: Use `config.py` for all credentials
2. **Use backend layer**: Have `menuv2.py` call `backend.py` functions instead of inline logic
3. **DRY principle**: Remove duplicate connection code from standalone scripts
4. **Secure credentials**: Move hardcoded passwords to environment variables
5. **Error messages**: Add more specific error feedback to users

---

**Documentation generated from actual source code analysis**  
Last updated: 2024
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
