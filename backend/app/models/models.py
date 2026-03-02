from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Local(Base):
    __tablename__ = "locales"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    activo = Column(Boolean, default=True)

class Familia(Base):
    __tablename__ = "familias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

class SKU(Base):
    __tablename__ = "skus"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    familia_id = Column(Integer, ForeignKey("familias.id"))
    activo = Column(Boolean, default=True)

class StockObjetivo(Base):
    __tablename__ = "stock_objetivo"
    id = Column(Integer, primary_key=True, index=True)
    local_id = Column(Integer)
    sku_id = Column(Integer)
    horario_corte = Column(String)
    cantidad_objetivo = Column(Integer)

class StockCorte(Base):
    __tablename__ = "stock_corte"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    local_id = Column(Integer)
    sku_id = Column(Integer)
    horario_corte = Column(String)
    cantidad_registrada = Column(Integer)