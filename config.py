import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:5432/{os.getenv('POSTGRES_DB')}"
VERSION = os.getenv("VERSION")
SECRET_TOKEN = os.getenv("SECRET_TOKEN")
SERVER_URL = os.getenv("SERVER_URL")
APP_ENV = os.getenv("APP_ENV")
CACHE_REDIS_HOST = os.getenv("CACHE_REDIS_HOST")
CACHE_REDIS_PORT = os.getenv("CACHE_REDIS_PORT")
