import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
VERSION = os.getenv("VERSION")
SECRET_TOKEN = os.getenv("SECRET_TOKEN")
SERVER_URL = os.getenv("SERVER_URL")
APP_ENV = os.getenv("APP_ENV")