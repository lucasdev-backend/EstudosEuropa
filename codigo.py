API_KEY = "SUA_CHAVE_AQUI"
import sqlite3
def conectar():
    return sqlite3.connect("banco.db")

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
                    create table if not exists usuarios
                   ( 
                   id integer primary key 
                   autoincrement,
                    email text unique,
                   senha text
                   )
                   """)
    cursor.execute("""
                   create table if not exists
                   historico (
                   id integer primary key
                   autoincrement,
                   usuario_id integer,
                   conversa text,
                   data datetime default
                   current_timestamp
                   )
                   """)
    conn.commit()
    conn.close()
    
def salvar_conversa(usuario_id, texto):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "insert into historico (usuario_id, conversa) values (?, ?)",
        (usuario_id, texto)
    )

    conn.commit()
    conn.close()


from db import conectar    
import bcrypt
#Cadastro
def cadastrar(email, senha):
    conn = conectar()
    cursor = conn.cursor()
#criptografa senha
    senha_hash = bcrypt.hashpw(senha.encode(),
    bcrypt.gensalt())
    #importante salvar como texto
    cursor.execute("insert info usuarios (email, senha) values (?, ?)",(email, senha_hash.decode())
                   )
    conn.commit()
    conn.close()

def login(email, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "select * from usuarios where email=?",
                   (email,))
    usuario = cursor.fetchone()
    conn.close()
    #Verifica a senha
    if usuario:
        senha_hash = usuario[2].encode() #pega do banco e volta para bytes

    if bcrypt.checkpw(senha.encode(),
     senha_hash): return usuario
    return None

#IA

from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)
def responder_ia(mensagem):
    prompt = f"""Você é uma terapeuta de Reiki profissional a mais de 15 anos, ajude o usuário com: respiração, meditação curtas de no máximo 5 minutos, tecnicas de relaxamento.utilize esses topicos conforme sua avaliação de que o clinte precisa.
    O usuário disse:
    "{mensagem}" 
    responda com: empatia, calma, orientação leve"""

    response = client.chat.completions.create(
        model="gpt-40-mini",
        messages=[
            {"role": "system", "content":
             "Você é uma terapeuta Reiki muito experiente"},
             {"role": "user", "content":
              "Estou ansioso"}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

#Sistema principal
from db import criar_tabelas,
salvar_conversa
from auth import login, cadastrar
from ai import responder_ia
criar_tabelas() 
email = input("email: ")
senha = input("senha: ")
usuario = login(email, senha)
if usuario:
    usuario_id = usuario[0]
    historico = ""
    while True:
        msg = input("você:")
        resposta = responder_ia(msg)
        print("IA:", resposta)
        conversa = f"Usuário: {msg}\nIA:
        {resposta}"
        salvar_conversa(usuario_id, conversa)
        historico += conversa +"\n"
        if msg.lower() == "sair":
            break
        else:
            print("login inválido")














from db import criar_tabelas
from auth import cadastrar, login
#criar banco 
criar_tabelas()

print("1 - cadrastar")
print("2 - login")

op = input("escolha:")

if op == "1":
    email = input("email:")
    senha = input("senha:")

    cadastrar(email,senha)
    print("Usuário Cadstrado!")

elif op == "2":
    email = input("email:")
    senha = input("senha:")

    usuario = login(email, senha)

    if usuario:
        print("Login realizado com sucesso!")
    else:
        print("Email ou senha incorretos")


