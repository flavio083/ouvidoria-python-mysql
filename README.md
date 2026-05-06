# 🌐 Ouvidoria Web System

A complaint management system built with Python, Flask and MySQL.

This branch contains the web version of the original CLI project.

---

# 🚀 Features

✅ Register complaints  
✅ List complaints  
✅ Search complaints  
✅ Update complaints  
✅ Remove complaints  
✅ REST API  
✅ Web interface  
✅ Admin dashboard  

---

# 🛠 Technologies

- Python
- Flask
- Flask-CORS
- MySQL
- HTML
- CSS
- JavaScript

---

# 📂 Project Structure

```txt
ouvidoria-python-mysql/
│
├── config/
├── database/
├── services/
├── menus/
│
└── web/
    ├── app.py
    ├── requirements.txt
    ├── templates/
    └── static/
```

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/flavio083/ouvidoria-python-mysql.git
```

Install dependencies:

```bash
pip install -r web/requirements.txt
```

Run application:

```bash
python -m web.app
```

Open:

```txt
http://localhost:5000
```

---

# API Endpoints

## List

```http
GET /api/reclamacoes
```

## Create

```http
POST /api/reclamacoes
```

## Update

```http
PUT /api/reclamacoes/<id>
```

## Delete

```http
DELETE /api/reclamacoes/<id>
```

---

# 👨‍💻 Author

Flaviano Aguiar

📧 flaviano-filho@hotmail.com  
🐙 GitHub: https://github.com/flavio083  
💼 LinkedIn: https://www.linkedin.com/in/flaviano-aguiar-173a93343