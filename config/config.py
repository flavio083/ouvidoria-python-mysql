import os

DB_HOST = os.getenv("HOST", "localhost")
DB_USER = os.getenv("USER", "user")
DB_PASSWORD = os.getenv("PASSWORD", "")
DB_NAME = os.getenv("DATABASE", "database")
DB_PORT = int(os.getenv("DB_PORT", 3306))