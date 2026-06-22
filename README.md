# 🌐 Gestão.AI — Web Edition

A management platform built with Python, Flask, and MySQL — featuring a **Complaint system (Ouvidoria)** and a **Stock management module (Estoque)**.

This branch contains the **web version** of the project, with REST API, browser-based interface, and authenticated admin dashboards deployed in production.

---

# 🚀 Features

## Ouvidoria (Complaints)

✅ Register complaints  
✅ List all complaints  
✅ Search complaints by code  
✅ Update complaints  
✅ Remove complaints  
✅ Count total complaints  

## Estoque (Stock Management)

✅ Register products (name, category, quantity, price, supplier)  
✅ List all products  
✅ Search products by ID  
✅ Update products (full edit)  
✅ Remove products  
✅ Stock summary (total products, total items, total value)  
✅ Low stock alert system  

## Platform

✅ REST API  
✅ Input validation  
✅ Responsive web interface  
✅ Admin dashboard with authentication  
✅ Environment variables  
✅ Production deployment  

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
gestao-ai/
│
├── main.py                          # CLI entry point (main menu)
├── config/
│   ├── config.py                    # Local config (gitignored)
│   └── config_exemplo.py           # Config template
│
├── database/
│   └── operacoesbd.py              # Database operations
│
├── services/
│   ├── backend.py                   # Complaint backend (CLI)
│   └── backend_estoque.py          # Stock backend (CLI)
│
├── menus/
│   ├── menuv2.py                    # Complaint CLI menu
│   └── menu_estoque.py             # Stock CLI menu
│
└── web/
    ├── app.py                       # Flask app + REST API
    ├── requirements.txt
    ├── templates/
    │   ├── index.html               # Complaint dashboard
    │   ├── admin.html               # Complaint admin panel
    │   ├── estoque.html             # Stock dashboard
    │   └── admin_estoque.html       # Stock admin panel
    └── static/
        ├── styles.css
        ├── script.js                # Complaint dashboard JS
        ├── script_admin.js          # Complaint admin JS
        ├── script_estoque.js        # Stock dashboard JS
        └── script_admin_estoque.js  # Stock admin JS
```

---

# ⚙️ Environment Variables

Create environment variables:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=ouvidoriabd
DB_PORT=3306

DB_ADMIN_USER=your_admin_user
DB_ADMIN_PASSWORD=your_admin_password
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

## Web Application (Flask)

```bash
python -m web.app
```

Open in browser:

```txt
http://localhost:5000
```

## CLI Application

```bash
python main.py
```

---

# 🌐 Web Pages

| Route | Description | Auth |
|-------|-------------|------|
| `/` | Complaint dashboard (Ouvidoria) | ❌ |
| `/estoque` | Stock dashboard (Estoque) | ❌ |
| `/admin` | Complaint admin panel | ✅ Basic Auth |
| `/admin/estoque` | Stock admin panel | ✅ Basic Auth |

---

# 📡 API Endpoints

## Complaints (`/api/reclamacoes`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/reclamacoes` | List all complaints |
| `POST` | `/api/reclamacoes` | Create a complaint |
| `GET` | `/api/reclamacoes/<codigo>` | Search complaint by code |
| `PUT` | `/api/reclamacoes/<codigo>` | Update a complaint |
| `DELETE` | `/api/reclamacoes/<codigo>` | Delete a complaint |
| `GET` | `/api/reclamacoes/quantidade` | Count total complaints |

## Products (`/api/produtos`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/produtos` | List all products |
| `POST` | `/api/produtos` | Create a product |
| `GET` | `/api/produtos/<id>` | Search product by ID |
| `PUT` | `/api/produtos/<id>` | Update a product |
| `DELETE` | `/api/produtos/<id>` | Delete a product |
| `GET` | `/api/produtos/resumo` | Stock summary (totals + value) |
| `GET` | `/api/produtos/alerta?limite=5` | Products with low stock |

---

# 🌍 Production

Live application:

https://ouvidoria-python-mysql.onrender.com

---

# 🔐 Admin Dashboards

Protected routes:

```txt
/admin          → Complaint management
/admin/estoque  → Stock management
```

Authentication uses HTTP Basic Auth with environment variables.

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
- Modular project design

---

# 👨‍💻 Author

Flaviano Aguiar Silva Filho

🐙 GitHub: https://github.com/flavio083  
💼 LinkedIn: https://www.linkedin.com/in/flaviano-aguiar-173a93343
