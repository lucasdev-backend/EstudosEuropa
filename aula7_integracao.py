import sqlite3


class Sessao:
    def __init__(self, nome_usuario, tema_sessao):
        self.nome = nome_usuario
        self.tema = tema_sessao
        self.__interacoes_realizadas = 0

    def adicionar_interacao(self):
        if self.__interacoes_realizadas < 5:
            self.__interacoes_realizadas += 1
        else:
            print("Limite de interações atingido para esta sessão!")

    # 3 AQUI ESTÁ A INTERAÇÃO REAL:
    def salvar_no_banco(self):
        # 1. Conecta ao mesmo banco que criamos antes
        conexao = sqlite3.connect("meu_banco.db")
        cursor = conexao.cursor()

        # 2. Insere os dados usando as variáveis do próprio objeto (usando o ponto de interrogaçãopor segurança)
        cursor.execute(
            """ INSERT INTO sessoes (nome, tema, interacoes) VALUES (?, ?, ?) """,
            (self.nome, self.tema, self.__interacoes_realizadas),
        )
        # 3. Salva e fecha
        conexao.commit()
        conexao.close()

        print(
            f"Sucesso! A sessão de '{self.nome}' foi gravada direto no Banco de Dados!"
        )


# --- TESTANDO A INTERAÇÃO DOS DOIS MUNDOS ---

# Criamos um objeto novinho em folha
sessao_automatica = Sessao("Rubia Dev", "Integração POO e SQL")

# Simulamos 4 interações
sessao_automatica.adicionar_interacao()
sessao_automatica.adicionar_interacao()
sessao_automatica.adicionar_interacao()
sessao_automatica.adicionar_interacao()

# Chamamos o método que faz a mágica acontecer lá dentro do banco!
sessao_automatica.salvar_no_banco()
