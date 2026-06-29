import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# Atualizando as interações APENAS onde nome for 'Rubia Iana'
# Vamos mudar de 3 para 4 interações
cursor.execute(""" UPDATE sessoes SET interacoes = 4 WHERE nome = 'Rubia Iana' """)

# Salvando a alteração no banco de dados de forma definitiva
conexao.commit()

print("Dados atualizados com sucessono banco!")

# --- AGORA VAMOS BUSCAR PARA VER SE MUDOU MESMO ---
cursor.execute("SELECT * FROM sessoes WHERE nome = 'Rubia Iana'")
resultados = cursor.fetchall()

print("\n--- RELATÓRIO ATUALIZADO---")
for linha in resultados:
    print(f"Usuário: {linha[1]} | Total de Interações Atualizado: {linha[3]}")

conexao.close()
