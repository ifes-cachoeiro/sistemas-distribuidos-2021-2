from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

NOME_BANCO = "meubanco"

engine = create_engine(f"sqlite:///./{NOME_BANCO}.sqlite", echo=True)
Base = declarative_base()

# Declaracao das classes


class Cliente(Base):

    __tablename__ = "cliente"

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String, unique=False, nullable=False)

    def __repr__(self):
        return f"Cliente {self.nome}"


# fim da declaracao

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
