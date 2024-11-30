import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    favoritos = relationship('Favorito', back_populates='usuario')

class Planeta(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String)
    clima = Column(String(50), nullable=False)  
    terreno = Column(String(100), nullable=False)  
    gravedad = Column(String(50), nullable=False)  
    populacion = Column(Integer, nullable=True)  
    favoritos = relationship('Favorito', back_populates='planeta')

class Personaje(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String)
    edad = Column(Integer, nullable=True)  
    peso = Column(Float, nullable=True)  
    raza = Column(String(50), nullable=True)  
    color_ojos = Column(String(50), nullable=True)  
    favoritos = relationship('Favorito', back_populates='personaje')

class Favorito(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    id_planeta = Column(Integer, ForeignKey('planetas.id'), nullable=True)
    id_personaje = Column(Integer, ForeignKey('personajes.id'), nullable=True)
    
    usuario = relationship(Usuario, back_populates='favoritos')
    planeta = relationship(Planeta, back_populates='favoritos')
    personaje = relationship(Personaje, back_populates='favoritos')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
