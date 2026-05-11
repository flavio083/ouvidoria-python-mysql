# 🌐 Ouvidoria System — Web Edition

A complaint management system built with Python, Flask, and MySQL.

This branch contains the **web version** of the original CLI project, featuring a REST API and browser-based interface.

---

# 🚀 Features

✅ Register complaints  
✅ List complaints  
✅ Search complaints by code  
✅ Update complaints  
✅ Remove complaints  
✅ Count total complaints  
✅ REST API  
✅ Input validation  
✅ Web interface  
✅ Admin dashboard  

---

# 🛠 Technologies

- Python 3
- Flask
- Flask-CORS
- MySQL
- HTML5
- CSS3
- JavaScript
- Git

---

# 📂 Project Structure

```txt
ouvidoria-python-mysql/
│
├── config/
├── database/
├── services/
│
└── web/
    ├── app.py
    ├── requirements.txt
    ├── templates/
    │   ├── index.html
    │   └── admin.html
    └── static/
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

Checkout web branch:

```bash
git checkout web
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

Run Flask application:

```bash
python -m web.app
```

Open in browser:

```txt
http://localhost:5000
```

---

# API Endpoints

## List complaints

```http
GET /api/reclamacoes
```

## Create complaint

```http
POST /api/reclamacoes
```

## Search complaint

```http
GET /api/reclamacoes/<codigo>
```

## Update complaint

```http
PUT /api/reclamacoes/<codigo>
```

## Delete complaint

```http
DELETE /api/reclamacoes/<codigo>
```

## Count complaints

```http
GET /api/reclamacoes/quantidade
```

---

# 🎯 Learning Outcomes

This project helped me improve in:

- REST API development
- Flask backend development
- Frontend integration
- CORS configuration
- Database persistence
- Full-stack architecture

---

# 👨‍💻 Author

Flaviano Aguiar Silva Filho

🐙 GitHub: https://github.com/flavio083  
💼 LinkedIn: https://www.linkedin.com/in/flaviano-aguiar-173a93343