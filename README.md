# 📋 Gestão.AI — CLI Edition

A management platform developed with Python and MySQL, designed to simulate a corporate management environment through a command-line interface.

This branch contains the **CLI version** of the project, featuring two integrated modules: **Ouvidoria (Complaints)** and **Estoque (Stock Management)**.

---

# 🚀 Features

## Ouvidoria (Complaints)

✅ Register complaints  
✅ List all complaints  
✅ Search complaints by code  
✅ Update existing complaints  
✅ Remove complaints  
✅ Count total records  

## Estoque (Stock Management)

✅ Register products (name, category, quantity, price, supplier)  
✅ List all products  
✅ Search products by ID  
✅ Update product quantity  
✅ Update product price  
✅ Remove products  
✅ Low stock alert (configurable threshold)  
✅ Stock summary (total products, items, and value)  

## Platform

✅ Input validation for all menus  
✅ Modular architecture  
✅ Centralized database connection  

---

# 🛠 Technologies

- Python 3
- MySQL
- Git
- Virtual Environment (venv)

---

# 📂 Project Structure

```txt
gestao-ai/
│
├── main.py                          # Main menu (Ouvidoria + Estoque)
├── README.md
├── LICENSE
│
├── config/
│   ├── __init__.py
│   ├── config.py                    # Local config (gitignored)
│   └── config_exemplo.py           # Config template
│
├── database/
│   ├── __init__.py
│   └── operacoesbd.py              # Database operations (CRUD)
│
├── services/
│   ├── __init__.py
│   ├── backend.py                   # Complaint operations
│   └── backend_estoque.py          # Stock operations
│
├── menus/
│   ├── __init__.py
│   ├── menuv2.py                    # Complaint CLI menu
│   └── menu_estoque.py             # Stock CLI menu
```

---

# ⚙️ Configuration

Create:

```bash
config/config.py
```

Using:

```python
HOST = "localhost"
USER = "your_user"
PASSWORD = "your_password"
DATABASE = "your_database"
PORT = 3306
```

A template is included:

```bash
config/config_exemplo.py
```

---

# 🗄 Database Setup

```sql
CREATE DATABASE ouvidoriabd;

USE ouvidoriabd;

CREATE TABLE Reclamações (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    reclamacao TEXT NOT NULL
);

CREATE TABLE Produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL DEFAULT 0,
    preco DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    fornecedor VARCHAR(255) NOT NULL
);
```

---

# 🔧 Installation

Clone repository:

```bash
git clone https://github.com/flavio083/ouvidoria-python-mysql.git
```

Enter project folder:

```bash
cd ouvidoria-python-mysql
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
source .venv/Scripts/activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running

Run the CLI application:

```bash
python main.py
```

You will see a main menu:

```
=== MENU PRINCIPAL ===
1) Ouvidoria;
2) Estoque;
3) Sair.
```

---

# 🎯 Learning Outcomes

This project helped me improve in:

- CRUD operations
- Python modularization
- SQL integration
- Input validation
- Error handling
- Multi-module architecture
- Git and GitHub workflow

---

# 👨‍💻 Author

Flaviano Aguiar Silva Filho

🐙 GitHub: https://github.com/flavio083  
💼 LinkedIn: https://www.linkedin.com/in/flaviano-aguiar-173a93343