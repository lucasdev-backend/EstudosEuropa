import sqlite3

# 1. Conecta ao banco de dados (se o arquivo não exixtir, o Python cria na hora)
conexao = sqlite3.connect("meu_banco.db")

# O cursor é que vai lá dentro do banco executar os comandos para a gente
cursor = conexao.cursor()

# 2. Criamos uma tabela usando comando SQL legítimos
# Definimos colunas fixas: id, nome, tema e interacoes
cursor.execute(
    """ CREATE TABLE IF NOT EXISTS sessoes( id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, tema TEXT NOT NULL, interacoes INTEGER NOT NULL)"""
)

# 3. Inserimos um dado de teste usandoo comando SQL: INSERT INTO
cursor.execute(
    """ INSERT INTO sessoes (nome, tema, interacoes) VALUES ('Rubia Iana', 'Introdução ao SQL', 3) """
)

# 4. Salvamos as alterações (commit) e fechamos a conexão por segurança
conexao.commit()
conexao.close()

print("Banco de dados criado e usuário inserido com sucesso!")
