from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase
from dotenv import load_dotenv
import os
from config import config
import requests

app = Flask(__name__)

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
app.secret_key = os.getenv("secret_key")
user = auth.current_user

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html",dados="Olá Mundo! (Exemplo de enviar dados para a página)")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if('user' in session):
        return render_template('/views/dashboard/homepage.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            return redirect(url_for('homepage'))
        except: 
            return render_template("Falha no Login")

    else:
        return render_template("/views/auth/login/login.html")


@app.route("/cadastro", methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.create_user_with_email_and_password(email, password)
        except:
            return 'Falha no cadastro'
    return render_template("/views/auth/cadastro/cadastro.html")

@app.route("/homepage", methods=['POST', 'GET'])
def homepage():
    user_session = session.get('user')
    try:
        # if 'idToken' in user_session:
        token = user_session['idToken']
        autenticado = autenticar_usuario(token)
        if autenticado:
            return render_template("/views/dashboard/homepage.html", user_email=user_session['email'])
        else:
            return "Falha na autenticação do usuário"
    except:
        return "Falha na autenticação do usuário"
    
@app.route("/recuperar-senha", methods=['POST', 'GET'])
def recuperar_senha():
    if request.method == 'POST':
        email = request.form.get('email')
        try: 
            auth.send_password_reset_email(email)
            return redirect(url_for('login'))
        except:
            return 'Usuário não encontrado'
    return render_template("/views/auth/recuperar-senha/recuperar-senha.html")

def autenticar_usuario(token):
    url = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key={config['apiKey']}"
    payload = {
            'idToken': token
        }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return True
    else:
        return False


if __name__ in "__main__":
  app.run (debug=True)