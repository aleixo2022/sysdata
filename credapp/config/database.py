import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Correção para verificar se DATABASE_URL é None e para corrigir URLs que começam com "postgres://"
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL não está definida no arquivo .env ou as variáveis de ambiente não estão sendo carregadas corretamente.")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})  # Adicionando sslmode conforme necessário no Heroku
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
