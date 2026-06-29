class Usuario:
    # O método __init__ é o "Construtor". É ele quem define o que o objeto
    # PRECISA receber no momento exato em que for criado.
    def __init__(self, nome_usuario, email_usuario):
        # Usamos o 'self' para dizer que estas variáveis pertencem a ESTE objeto específico
        self.nome = nome_usuario
        self.email = email_usuario
        self.status_da_conta = "Ativo"  # Um atributo que já começa com um padrão

    # Isto é um Método. Uma ação que o usuário pode executar.
    # Note que ele SEMPRE recebe o 'self' como primeiro argumento.
    def exibir_perfil(self):
        print("___PERFIL DO USUÁRIO___")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Status: {self.status_da_conta}")
        print("-------------------------")


# --- TESTANDO NOSSO MOLDE NO MUNDO REAL ---
# Aqui estamos criando (instanciando) dois objetos diferentes usando a mesma classe.
Usuario_1 = Usuario("lucas Flores", "lucas@email.com")
Usuario_2 = Usuario("Rubia Iana", "rubia@email.com")

# Agora, mandamos cada objeto executar a sua ação
Usuario_1.exibir_perfil()
Usuario_2.exibir_perfil()


# EXERCÍCIO DA AULA 1
class Sessao:
    # construtor
    def __init__(self, nome_usuario, tema_sessao):
        # usamos self para dizer que essa variável pertence a este obejeto.
        self.nome = nome_usuario
        self.tema = tema_sessao
        self.__interacoes_realizadas = 0

    # Isto é um Método. Uma ação que o usuário pode executar.
    def adicionar_intercao(self):
        if self.__interacoes_realizadas < 5:
            self.__interacoes_realizadas += 1  # Se for menor, permite somar!
        else:
            # 2. Se já for 5 ou mais, cai e bloqueia
            print("Limite de interações atingido para esta sessão!")

    def gerar_resumo(self):

        print("___RESUMO INTERAÇÕES___")
        print(f"Nome: {self.nome}")
        print(f"Tema: {self.tema}")
        print(f"Interações: {self.__interacoes_realizadas}")

        print("-------------------------")


# --- TESTANDO SEU EXERCÍCIO ---
# 1. Criamos uma sessão para você
minha_sessao = Sessao("Lucas Flores", "Planejamento  de Estudos")

# 2. Simulamos que você interagiu com o sistema 3 vezes
# chama 6 vezes seguidas
minha_sessao.adicionar_intercao()  # 1
minha_sessao.adicionar_intercao()  # 2
minha_sessao.adicionar_intercao()  # 3
minha_sessao.adicionar_intercao()  # 4
minha_sessao.adicionar_intercao()  # 5
minha_sessao.adicionar_intercao()  # 6-> Aqui deve printar o aviso!

minha_sessao.gerar_resumo()  # O resumo deve mostrar no máximo 5 interações

# ___ AULA 3: HERANÇA ___


# Criamos a classe Administrador que ela HERDA de Usuario
class Administrador(Usuario):
    # Este método é EXCLUSIVO do Administrador.
    # Um usuário comum não terá acesso a ele.
    def alterar_status_sistema(self, novo_status):
        print(f"\n[ALERTA] O Admin {self.nome} alterou o sistema para: {novo_status}")


# ___ TESTANDO SEU NOVO CÓDIGO ___

# 1. Criamos um objeto de tipo Administrador
# Note que passamos nome e e-mail normalmente, porque ele herdou isso de Usuario!
admin_1 = Administrador("Rubia lider", "rubia.admin@empresa.pt")

# 2. Executamos o método que ela herdou da classe mãe (Usuario)
admin_1.exibir_perfil()

# 3. Executamos o método EXCLUSIVO que só o Administrador tem
admin_1.alterar_status_sistema("Modo Manutenção")
