# config/config.py
import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret_key')
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)  # Configuração do tempo de expiração do token
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=1)

    #DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///sysbimetric.db')
    DATABASE_URL = os.getenv('DATABASE_URL')
    
    # Configuração do JWT para utilizar apenas headers
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
 

