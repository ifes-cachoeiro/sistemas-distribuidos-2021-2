from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

NOME_BANCO = "meubanco"

engine = create_engine(f"sqlite:///./{NOME_BANCO}.sqlite", echo=True)
Base = declarative_base()

# Declaracao das classes


class Cliente(Base):

    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=False, nullable=False)
    endereco = Column(String, nullable=False)

    def __repr__(self):
        return f"Cliente {self.nome}"


class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    valor = Column(Float, nullable=False)

    def __repr__(self) -> str:
        return f"Produto {self.nome}"


class Carrinho(Base):

    __tablename__ = "carrinho"
    id = Column(Integer, primary_key=True)
    produto_id = Column(
        Integer,
        ForeignKey('produto.id'),
        nullable=False
    )


class Venda(Base):

    __tablename__ = "venda"

    id = Column(Integer, primary_key=True)
    data_venda = Column(Date, nullable=False)
    carrinho_id = Column(
        Integer,
        ForeignKey('carrinho.id'),
        nullable=False
    )
    cliente_id = Column(
        Integer,
        ForeignKey('cliente.id'),
        nullable=False
    )

# fim da declaracao


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
