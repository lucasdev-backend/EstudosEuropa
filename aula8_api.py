from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

# Criamos o noss aplicativo web
app = FastAPI()


# Criamos um modelo para vlidar os dados que chegam da internet
class NovaSessaoSchema(BaseModel):
    nome: str
    tema: str


# Função garantida que cria a tabela se ela sumir
def criar_tabela_se_nao_existir():
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS sessoes ( id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, tema TEXT NOT NULL, interacoes INTEGER NOT NULL) """
    )
    conexao.commit()
    conexao.close()


@app.get("/sessoes")
def listar_sessoes_na_internet():
    criar_tabela_se_nao_existir()  # Garante a tabela antes de buscar

    # 1. Vamos buscar os dados do banco exatemente como você aprendeu!
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM sessoes")
    resultados = cursor.fetchall()
    conexao.close()
    return {"status": "Sucesso", "dados": resultados}


# NOVA ROTA: Porta de entrada para receber dados novos
@app.post("/criar-sessao")
def criar_nova_sessao_via_api(dados: NovaSessaoSchema):
    criar_tabela_se_nao_existir()  # Garante a tabela antes de salvar

    # 1. Conectamos ao banco
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    # 2. Passamos o 0 dentro da tupla de parámetros para oSQLite aceitar sem chiar
    cursor.execute(
        """ INSERT INTO sessoes (nome, tema, interacoes) VALUES (?, ?, ?)""",
        (dados.nome, dados.tema, 0),
    )

    conexao.commit()
    conexao.close()

    return {
        "status": "Sucesso",
        "mensagem": f"Sessão de {dados.nome} criada com sucesso via internet!",
    }


# NOVA ROTA: Porta de entrada para deletar uma sessão pelo ID
@app.delete("/deletar-sesao/{sessao_id}")
def deletar_sessao_via_api(sessao_id: int):
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    # Executamos o comando SQL DELETE usando o ID que veio da internet
    cursor.execute("DELETE FROM sessoes WHERE id = ?", (sessao_id,))

    conexao.commit()
    conexao.close()

    return {
        "status": "Sucesso",
        "mensagem": f"Sessão com ID {sessao_id} foi deletada com sucesso!",
    }
