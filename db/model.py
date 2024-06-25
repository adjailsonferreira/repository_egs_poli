from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from db.config_db import Base

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
db=SQLAlchemy(app)

#pre-inscricao projetos
class PreinscricaoProjeto(Base):
  __tablename__ = 'preinscricao_projeto'
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(244))
  equipe = db.Column(db.String(244))
  data = db.Column(db.String(244))
  cliente = db.Column(db.String(244))
  tecnologia = db.Column(db.String(244))
  descricao = db.Column(db.String(244))
  link = db.Column(db.String(244))
  pitch = db.Column(db.String(244))
  logomarca = db.Column(db.String(244))

  def __init__(self,nome,equipe,data,cliente,tecnologia,descricao,link,pitch,logomarca):
    self.nome=nome
    self.equipe=equipe
    self.data=data
    self.cliente=cliente
    self.tecnologia=tecnologia
    self.descricao=descricao
    self.link=link
    self.pitch=pitch
    self.logomarca = logomarca
