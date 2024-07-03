from sqlalchemy.ext.declarative import declarative_base
from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Text, CHAR, DateTime, Float,Boolean
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256 as sha256
from datetime import datetime, timezone

# Exemplo de modelo
class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    email = Column(String, unique=True, index=True)
    admin = Column(Boolean, default=False)
    api_access_token = Column(String)
    api_refresh_token = Column(String)
    mercado_livre_user_id = Column(String, nullable=True)
    mercado_livre_access_token = Column(String, nullable=True)
    refresh_token = Column(String, nullable=True)
    token_saved_at = Column(DateTime,nullable=True)
    token_adjusted_date =  Column(DateTime,nullable=True)
    
    bonuses = relationship('Bonus', back_populates='user')  # Relacionamento com Bonus
    
    @staticmethod
    def verify_password(password_hash, password):
        return sha256.verify(password, password_hash)

    # Flask-Login propriedades
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True  # Você pode adicionar lógica aqui para desativar usuários

    @property
    def is_anonymous(self):
        return False


 

class Bonus(Base):
    __tablename__ = 'bonus'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    invoice = Column(String, nullable=False)
    stock = Column(Integer, nullable=False)
    sku = Column(String, nullable=False)
    value = Column(Numeric(10, 2), nullable=False)  # Decimal para valores monetários
    observation = Column(Text, nullable=True)
    operation = Column(CHAR, nullable=False)  # 'e', 's' ou 'r'
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    
    user = relationship('User', back_populates='bonuses')
    


class Rentabilidade(Base):
    __tablename__ = 'rentabilidade'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ordem = Column(String, nullable=False)
    carrinho = Column(String, nullable=True)
    sku = Column(String, nullable=False)
    mlb = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    tipo_anuncio = Column(String, nullable=False)
    comissao = Column(Numeric(10, 2), nullable=False)
    repasse = Column(Numeric(10, 2), nullable=False)
    desconto_bonus = Column(Numeric(10, 2), nullable=False)
    reembolso_frete = Column(Numeric(10, 2), nullable=False)
    preco_unitario = Column(Numeric(10, 2), nullable=False)
    preco_unitario_cheio = Column(Numeric(10, 2), nullable=False)
    total_pago = Column(Numeric(10, 2), nullable=False)
    id_conta_ml = Column(Integer, nullable=False)
    nome_conta_ml = Column(String, nullable=False)
    estado_origem = Column(String, nullable=False)
    estado_destino = Column(String, nullable=False)
    frete = Column(Numeric(10, 2), nullable=False)
    tipo_envio = Column(String, nullable=False)
    data_pedido = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    
    # Relacionamento com User se necessário
    # user = relationship('User', back_populates='rentabilidades')

