import os

HOST = os.getenv("HOST", "localhost")
USER = os.getenv("USER", "user")
PASSWORD = os.getenv("PASSWORD", "")
DATABASE = os.getenv("DATABASE", "database")
PORT = int(os.getenv("PORT", 3306))