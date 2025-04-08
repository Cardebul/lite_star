import os

from dotenv import load_dotenv

load_dotenv()


class AppConfig:
    pg_user = os.getenv('POSTGRES_USER')
    pg_pass = os.getenv('POSTGRES_PASSWORD')
    pg_host = os.getenv('DB_HOST')
    pg_port = os.getenv('DB_PORT')
    pg_db = os.getenv('POSTGRES_DB')