import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "sua_senha")
DB_NAME = os.getenv("DB_NAME", "ouvidoriabd")
DB_PORT = int(os.getenv("DB_PORT", 3306))