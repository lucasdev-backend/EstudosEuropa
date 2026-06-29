# Simulando a ação do Admistrador que você aprendeu na aula passada
nome_admin = "Rubia Lider"
acao = "Alterou o sistema para Modo Manutenção"

# USANDO O WITH OPEN:
# 'historico_sistema.txt' é o nome do arquivo que vai ser criado.
# 'a' significa APPEND (Vai adicionando linhas sem apagar as anteriores).
# 'encoding="utf-8"' Serve para o arquivo aceitar acentos (como o 'ç' e '~').
with open("historico_sistema.txt", "a", encoding="utf-8") as arquivo:
    # Escrevemos a linha dentro do arquivo.
    # O '\n' no final da linha serve para pular para próxima linha no bloco de notas.
    arquivo.write(f"Admin: {nome_admin} | Ação: {acao}\n")

print("Dados salvos permanentemente com sucesso!")


class Sessao:
    def __init__(self, nome_usuario, tema_sessao):
        self.nome = nome_usuario
        self.tema = tema_sessao
        self.__interacoes_realizadas = 0  # Atributo privado que você aprendeu!

    def adicionar_intercao(self):
        if self.__interacoes_realizadas < 5:
            self.__interacoes_realizadas += 1
        else:
            print("Limite de interações atingido para esta sessão!")

    # AQUI ESTÁ A MÁGICA DA AULA 4
    def gerar_resumo(self):
        # Em vez de dar print na tela, jogamosdireto para o arquivo!
        with open("resumo_sessoes.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(
                f"Nome: {self.nome} | Tema: {self.tema} | Interações: {self.__interacoes_realizadas}\n"
            )
            print("Resumo da sessão salvo no arquivo com sucesso!")


# ___ TESTANDO O SALVAMENTO PERMANENTE ___

# 1. Criamos a sessão
minha_sessao = Sessao("Rubia Iana", "Persistência de Dados")

# 2.  Adicionamos 3 interações
minha_sessao.adicionar_intercao()
minha_sessao.adicionar_intercao()
minha_sessao.adicionar_intercao()

# 3. Chamamos o método que grava no arquivo de texto
minha_sessao.gerar_resumo()
