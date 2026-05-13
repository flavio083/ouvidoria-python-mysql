import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "your_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your_password")
DB_NAME = os.getenv("DB_NAME", "your_database")
DB_PORT = int(os.getenv("DB_PORT", 3306))

DB_ADMIN_USER = os.getenv(
    "DB_ADMIN_USER",
    "your_admin_user"
)

DB_ADMIN_PASSWORD = os.getenv(
    "DB_ADMIN_PASSWORD",
    "your_admin_password"
)