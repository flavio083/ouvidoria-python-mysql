# 🎯 Ouvidoria BDGIT - Complaint Management System

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/mysql-8.0%2B-orange)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Active-success)](https://github.com/flavio083/ouvidoriaintegrabd)

A robust and modular **Complaint Management System** built in Python with MySQL database integration. This project demonstrates professional backend development practices with clean architecture, separation of concerns, and comprehensive database operations handling.

## 📋 Table of Contents

- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [Folder Structure](#-folder-structure)
- [Technologies](#-technologies)
- [Installation Guide](#-installation-guide)
- [Configuration Guide](#-configuration-guide)
- [Database Setup](#-database-setup)
- [How to Run](#-how-to-run)
- [Usage Examples](#-usage-examples)
- [API Operations](#-api-operations)
- [Security Features](#-security-features)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [License](#-license)

## ✨ Features

### Core Functionalities

- ✅ **Create Complaints** - Register new complaints with automatic ID assignment
- ✅ **List All Complaints** - Display all complaints with ID and description
- ✅ **Search Complaints** - Find specific complaints by complaint code
- ✅ **Update Complaints** - Modify existing complaint descriptions
- ✅ **Delete Complaints** - Remove complaints from the system
- ✅ **Count Complaints** - Display total number of registered complaints

### Technical Highlights

- 🔐 **Prepared Statements** - SQL injection prevention with MySQL prepared statements
- 🛡️ **Error Handling** - Comprehensive exception handling for database operations
- 💾 **Transaction Management** - Rollback support for failed operations
- 🏗️ **Modular Architecture** - Clean separation between UI, business logic, and database layers
- 📝 **Logging & Feedback** - User-friendly console feedback for all operations
- 🔌 **Connection Management** - Efficient database connection handling

## 🏛️ Project Architecture

The project follows a **Three-Layer Architecture Pattern** for optimal code organization and maintainability:

```
┌─────────────────────────────────────┐
│     Presentation Layer (UI)         │
│  - menuv2.py (CLI Menu Interface)   │
├─────────────────────────────────────┤
│    Business Logic Layer             │
│  - backend.py (Operations Handler)  │
├─────────────────────────────────────┤
│    Data Access Layer (Database)     │
│  - operacoesbd.py (DB Operations)   │
├─────────────────────────────────────┤
│    Configuration Layer              │
│  - config.py (Connection Settings)  │
└─────────────────────────────────────┘
```

### Layer Responsibilities

| Layer | Files | Responsibility |
|-------|-------|-----------------|
| **UI** | `menuv2.py` | User interaction, menu display, input handling |
| **Business Logic** | `backend.py` | Core complaint operations coordination |
| **Database** | `operacoesbd.py` | SQL execution, connection management, CRUD operations |
| **Config** | `config_exemplo.py`, `config.py` | Database credentials and connection parameters |

## 📁 Folder Structure

```
OuvidoriaBDGIT/
├── 📄 README.md                    # Project documentation (this file)
├── 📄 requirements.txt             # Python dependencies
├── 📄 config_exemplo.py            # Configuration template
├── 📄 config.py                    # Actual configuration (git-ignored)
├── 📄 menuv2.py                    # Main CLI menu interface ⭐
├── 📄 menu.py                      # Alternative menu version
├── 📄 main.py                      # Application entry point
├── 📄 backend.py                   # Business logic layer
├── 📄 operacoesbd.py               # Database operations layer
├── 📄 adicionar.py                 # Create complaint (standalone)
├── 📄 listar.py                    # List complaints (standalone)
├── 📄 pesquisar.py                 # Search complaint (standalone)
├── 📄 remover.py                   # Delete complaint (standalone)
├── 📄 substituir.py                # Update complaint (standalone)
├── 📄 quantidade.py                # Count complaints (standalone)
└── 📄 .gitignore                   # Git ignore rules
```

## 🛠️ Technologies

### Backend Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.8+ | Core programming language |
| **MySQL** | 8.0+ | Relational database |
| **mysql-connector-python** | 8.0+ | Python-MySQL driver |

### Key Libraries

```
mysql-connector-python==8.0.33
```

### Development Tools

- **IDE**: PyCharm / VS Code
- **Version Control**: Git / GitHub
- **Package Manager**: pip

## 📦 Installation Guide

### Prerequisites

- **Python 3.8+** installed on your system
- **MySQL Server 8.0+** installed and running
- **pip** package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/flavio083/ouvidoriaintegrabd.git
cd OuvidoriaBDGIT
```

### Step 2: Create Virtual Environment

**On Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Expected output:
```
Successfully installed mysql-connector-python-8.0.33
```

### Step 4: Verify Installation

```bash
python -c "import mysql.connector; print('MySQL Connector installed successfully!')"
```

## ⚙️ Configuration Guide

### Step 1: Copy Configuration Template

```bash
cp config_exemplo.py config.py
```

### Step 2: Edit config.py

Open `config.py` and update with your MySQL credentials:

```python
# config.py
HOST = "localhost"           # MySQL host address
USER = "root"                # MySQL username
PASSWORD = "your_password"   # Your MySQL password
DATABASE = "ouvidoriabd"     # Database name
PORT = 3306                  # MySQL port (default: 3306)
```

### Configuration Template Reference

**config_exemplo.py** (DO NOT EDIT):
```python
HOST = "localhost"
USER = "root"
PASSWORD = "your_password_here"
DATABASE = "ouvidoriabd"
PORT = 3306
```

### Important Security Notes

⚠️ **NEVER commit actual credentials to version control!**

- Add `config.py` to `.gitignore`
- Always use `config_exemplo.py` as a template
- Use environment variables for production deployments

## 🗄️ Database Setup

### Step 1: Create Database

Connect to MySQL and execute:

```sql
CREATE DATABASE ouvidoriabd CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### Step 2: Create Complaints Table

```sql
USE ouvidoriabd;

CREATE TABLE Reclamações (
    codigo INT PRIMARY KEY AUTO_INCREMENT,
    reclamacao TEXT NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Step 3: Insert Sample Data (Optional)

```sql
INSERT INTO Reclamações (reclamacao) VALUES 
('Email server issues'),
('System running slow'),
('Missing documentation');
```

### Step 4: Verify Connection

Run the application to test database connectivity:

```bash
python menuv2.py
```

## 🚀 How to Run

### Running the Interactive Menu (Recommended)

```bash
python menuv2.py
```

**Expected Output:**
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

### Running Standalone Modules

Each operation can also be run individually:

```bash
python listar.py      # List all complaints
python adicionar.py   # Add new complaint
python pesquisar.py   # Search complaint
python substituir.py  # Update complaint
python remover.py     # Delete complaint
python quantidade.py  # Count complaints
```

## 📖 Usage Examples

### Example 1: Interactive Menu Session

```
Digite sua opção: 1

-- Lista de Reclamações --
1 - Email server issues
2 - System running slow
3 - Missing documentation
```

### Example 2: Adding a New Complaint

```
Digite sua opção: 2
Insira sua reclamação: Air conditioning not working properly
Reclamação adicionada com sucesso! 
O código é 4
```

### Example 3: Searching for a Complaint

```
Digite sua opção: 3
Digite o código da Reclamação: 2
A reclamação pesquisada foi: System running slow
```

### Example 4: Updating a Complaint

```
Digite sua opção: 4
Digite o código da reclamação a ser substituida: 2
Digite a nova reclamação: System extremely slow - CRITICAL
Reclamação substituida com sucesso!
```

### Example 5: Deleting a Complaint

```
Digite sua opção: 5
Digite o código da Reclamação a ser Removida: 2
Reclamação removida com sucesso!
```

### Example 6: Viewing Statistics

```
Digite sua opção: 6
Atualmente temos 5 reclamações.
```

## 🔧 API Operations

### Database Operations Module (`operacoesbd.py`)

The `operacoesbd.py` module provides the **data access layer** with six core functions for CRUD operations:

#### 1. **criarConexao()** - Create Connection

```python
conexao = criarConexao(host, user, password, database, port)
```

Establishes connection with MySQL database with error handling.

#### 2. **encerrarConexao()** - Close Connection

```python
encerrarConexao(conexao)
```

Safely closes database connection.

#### 3. **insertNoBancoDados()** - Insert Records

```python
novo_id = insertNoBancoDados(conexao, sql_query, dados)
```

Insert data with prepared statements and transaction support.

#### 4. **listarBancoDados()** - Read Records

```python
resultados = listarBancoDados(conexao, sql_query, parametros)
```

Retrieve data with optional parameters.

#### 5. **atualizarBancoDados()** - Update Records

```python
linhas_afetadas = atualizarBancoDados(conexao, sql_query, dados)
```

Update records with transaction management.

#### 6. **excluirBancoDados()** - Delete Records

```python
linhas_deletadas = excluirBancoDados(conexao, sql_query, dados)
```

Delete records with error handling and rollback support.

### Backend Layer (`backend.py`)

```python
from backend import *

# High-level operations
listarReclamacoes(conexao)           # List all complaints
novaReclamacao(conexao)              # Register new complaint
pesquisarReclamacao(conexao)         # Search complaint by code
substituirReclamacao(conexao)        # Update complaint
removerReclamacao(conexao)           # Delete complaint
quantidadeReclamacao(conexao)        # Display total count
```

## 🔐 Security Features

### Implemented

- ✅ **Prepared Statements** - Protection against SQL injection
- ✅ **Error Handling** - Graceful error management
- ✅ **Transaction Rollback** - Data consistency on failures
- ✅ **Connection Validation** - Safe connection handling

### Recommended for Production

- 🔒 Use environment variables for credentials
- 🔒 Implement authentication and authorization
- 🔒 Add input validation and sanitization
- 🔒 Enable MySQL SSL connections
- 🔒 Implement audit logging
- 🔒 Rate limiting for API endpoints

## 📈 Future Improvements

### Phase 2 - Enhanced Features
- [ ] Web API REST endpoints (Flask/FastAPI)
- [ ] Web-based dashboard interface
- [ ] User authentication system
- [ ] Role-based access control (RBAC)
- [ ] Complaint categories and tagging

### Phase 3 - Advanced Functionality
- [ ] Email notifications for complaint updates
- [ ] File attachment support
- [ ] Comment threads on complaints
- [ ] SLA tracking and management
- [ ] Advanced search and filtering
- [ ] Data export (CSV/PDF)

### Phase 4 - DevOps & Scalability
- [ ] Docker containerization
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Database migration scripts
- [ ] Performance optimization
- [ ] Database replication
- [ ] Redis caching layer

### Phase 5 - Quality & Testing
- [ ] Unit tests (pytest)
- [ ] Integration tests
- [ ] API documentation (Swagger/OpenAPI)
- [ ] Code coverage reporting
- [ ] Load testing

## 💡 Architecture Highlights

### Design Patterns Used

1. **Separation of Concerns** - Clear layer separation for UI, business logic, and data access
2. **CRUD Pattern** - Standard Create, Read, Update, Delete operations
3. **Error Handling Pattern** - Try-catch blocks with graceful error recovery
4. **Connection Management** - Efficient resource handling

### Best Practices Implemented

✓ Prepared statements for SQL injection prevention  
✓ Transaction management with rollback capability  
✓ Resource cleanup with proper connection closure  
✓ Meaningful error messages for debugging  
✓ Modular code structure for maintainability  
✓ Configuration externalization  

## 🤝 Contributing

This is an internship project demonstrating professional Python backend development. Feel free to fork, study, and build upon this codebase.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 👨‍💻 Author

**Flavio Silva**

- GitHub: [@flavio083](https://github.com/flavio083)
- Repository: [ouvidoriaintegrabd](https://github.com/flavio083/ouvidoriaintegrabd)
- Institution: Universidade Federal de Campina Grande (UNIFACISA)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support & Contact

- 📧 For questions or issues, open a GitHub Issue
- 💬 GitHub Discussions for feature requests
- 🐛 Bug reports can be submitted via Issues

## 🎓 Learning Resources

This project demonstrates:

- Python backend development best practices
- Database design and SQL operations
- Python MySQL integration
- CLI application development
- Modular architecture patterns
- Error handling and exception management
- Configuration management
- Git version control workflows

## 🚀 Quick Start Summary

```bash
# Clone repository
git clone https://github.com/flavio083/ouvidoriaintegrabd.git
cd OuvidoriaBDGIT

# Setup virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Configure database
cp config_exemplo.py config.py
# Edit config.py with your MySQL credentials

# Run application
python menuv2.py
```

---

**Made with ❤️ for backend development excellence**

⭐ If this project helped you, please consider giving it a star!
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
