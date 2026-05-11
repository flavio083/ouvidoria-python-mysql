# 📋 Ouvidoria System — CLI Edition

A complaint management system developed with Python and MySQL, designed to simulate an academic ombudsman environment through a command-line interface.

This branch contains the **original CLI version** of the project.

---

# 🚀 Features

✅ Register complaints  
✅ List all complaints  
✅ Search complaints by code  
✅ Update existing complaints  
✅ Remove complaints  
✅ Count total records  
✅ Input validation for CLI menus  
✅ Modular architecture  

---

# 🛠 Technologies

- Python 3
- MySQL
- Git
- Virtual Environment (venv)

---

# 📂 Project Structure

```txt
ouvidoria-python-mysql/
│
├── main.py
├── README.md
├── LICENSE
│
├── config/
│   ├── __init__.py
│   └── config_exemplo.py
│
├── database/
│   ├── __init__.py
│   └── operacoesbd.py
│
├── services/
│   ├── __init__.py
│   └── backend.py
│
├── menus/
│   ├── __init__.py
│   └── menuv2.py
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
CREATE DATABASE ouvidoria;

USE ouvidoria;

CREATE TABLE Reclamações (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    reclamacao TEXT NOT NULL
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

---

# 🎯 Learning Outcomes

This project helped me improve in:

- CRUD operations
- Python modularization
- SQL integration
- Input validation
- Error handling
- Git and GitHub workflow

---

# 👨‍💻 Author

Flaviano Aguiar Silva Filho

🐙 GitHub: https://github.com/flavio083  
💼 LinkedIn: https://www.linkedin.com/in/flaviano-aguiar-173a93343