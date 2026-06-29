class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # o '__' torna o saldo PRIVADO.Protegido contra alterações maliciosas de fora.
        self.__saldo = saldo_inicial

    # Como o saldo é privado, criamos um método seguro para alterá-lo (Movimentação)
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de ${valor} realizado com sucesso!")
        else:
            print("Operação Inválida! O valor do depósito deve ser positivo.")

    # Criamos um método seguro para ler o dado (Busca/Visualização)
    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo Atual: ${self.__saldo}")


# ___ TESTANDO A SEGURANÇA ___

minha_conta = ContaBancaria("Rubia Iana", 10000)
# Tentativa 1: Tentar alterar o saldo diretamente de fora (como um hacker ou bug faria)
minha_conta.__saldo = (
    50000  # O python vai ignorar isso ou criar uma variável genérica isolada!
)

# Vamos ver se o saldo real mudou?
minha_conta.exibir_saldo()  # vai continuar mostrando $10000! O cofre funcionou.

# Tentativa 2: Ussando a movimentação correta e segura
minha_conta.depositar(250)
minha_conta.exibir_saldo()  # Agora sim, mostra $10250!
