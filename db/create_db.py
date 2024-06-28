from config_db import engine, Base
from sqlalchemy.exc import SQLAlchemyError
from model import  InformacoesIndicado, PreinscricaoPessoa, EnvioProjeto, PreinscricaoProjeto

try:
    print("creating database ...")
    Base.metadata.create_all(engine)
    print("success!")
except SQLAlchemyError as e:
    print(f"error database: {e}")

