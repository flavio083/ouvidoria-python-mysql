# 📋 Ouvidoria System

A modular complaint management system built with Python and MySQL.

---

# 🚀 Features

✅ Register complaints  
✅ List complaints  
✅ Search complaints  
✅ Update complaints  
✅ Remove complaints  
✅ Count records  
✅ Modular architecture  
✅ Secure local configuration  

---

# 🛠 Technologies

- Python
- MySQL
- Git

---

# 📂 Project Structure

```bash
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
│   ├── backend.py
│   ├── adicionar.py
│   ├── listar.py
│   ├── pesquisar.py
│   ├── remover.py
│   └── substituir.py
│
├── menus/
│   ├── __init__.py
│   ├── menu.py
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

# ▶️ Running

Clone repository:

```bash
git clone https://github.com/flavio083/ouvidoria-python-mysql.git
```

Run:

```bash
python main.py
```

---

# 🎯 Learning Outcomes

This project helped me improve in:

- CRUD operations
- Python modularization
- Database integration
- Git and GitHub workflow
- Software organization

---

# 👨‍💻 Author

Flaviano Aguiar

📧 flaviano-filho@hotmail.com  
🐙 GitHub: https://github.com/flavio083  
💼 LinkedIn: https://www.linkedin.com/in/flaviano-aguiar-173a93343