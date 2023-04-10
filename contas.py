class Conta:
    def __init__(self, cliente, conta, saldo = 0):
        self.__cliente = cliente
        self.__conta = conta
        self.__saldo = saldo
        self.operacoes = []
        self.deposito(saldo) 

    def resumo(self):
        print(f"Cliente:{self.cliente}, Conta:{self.conta}, Saldo:{self.saldo}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append("SAQUE", valor)
        else:
            print("Saldo Insuficiente para saque!")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append("DEPOSITO", valor)
    




conta1 = Conta("Fabricio", 123, 200)
print(conta1.cliente, conta1.conta, conta1.saldo)
