import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# Fazendo uma busca FILTRADA usando o WHERE (procurando apenas pelo nome Rubia)
cursor.execute("SELECT * FROM sessoes")
resultados = cursor.fetchall()

print("\n--- RELATÓRIO DO BANCO DE DADOS (FORMATADO)---")
for linha in resultados:
    # Acessamos cada posição da tupla para organizar o texto
    print(
        f"Usuário: {linha[1]} | Tema estudos: {linha[2]} | Total de Interações: {linha[3]}"
    )

conexao.close()
