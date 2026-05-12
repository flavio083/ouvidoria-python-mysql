# 🌐 Ouvidoria System — Web Edition

A complaint management system built with Python, Flask, and MySQL.

This branch contains the **web version** of the original CLI project, featuring a REST API, browser-based interface, and an authenticated admin dashboard deployed in production.

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
✅ Basic authentication  
✅ Environment variables  
✅ Production deployment  

---

# 🛠 Technologies

- Python 3
- :contentReference[oaicite:0]{index=0}
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

# ⚙️ Environment Variables

Create environment variables:

```env
DB_HOST=
DB_USER=
DB_PASSWORD=
DB_NAME=
DB_PORT=

ADMIN_USER=
ADMIN_PASSWORD=
```

Example local fallback configuration:

```python
import os

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT"))

ADMIN_USER = os.getenv("ADMIN_USER")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
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

# 🌍 Production

Live application:

https://ouvidoria-python-mysql.onrender.com

Hosted on :contentReference[oaicite:1]{index=1}.

---

# 🔐 Admin Dashboard

Protected route:

```txt
/admin
```

Authentication uses HTTP Basic Auth with environment variables.

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

# 🔒 Security

✅ Environment variables  
✅ Prepared statements  
✅ Restricted CORS  
✅ Basic authentication  
✅ Exception protection  

---

# 🎯 Learning Outcomes

This project helped me improve in:

- REST API development
- Flask backend development
- Frontend integration
- Authentication
- CORS configuration
- Database persistence
- Cloud deployment
- Full-stack architecture

---

# 👨‍💻 Author

Flaviano Aguiar Silva Filho

🐙 GitHub: https://github.com/flavio083  
💼 LinkedIn: https://www.linkedin.com/in/flaviano-aguiar-173a93343