import os
from flask import send_file
import pandas as pd

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

def inscricaoProjeto():
    consulta_projeto = pd.read_sql_query(f"SELECT * FROM inscricaoProjeto", SQLALCHEMY_DATABASE_URI)
    if consulta_projeto.empty:
        return False
    df_projeto = consulta_projeto
    return df_projeto.to_html(classes='table', border=0, header=None,index=False)