class Conta:
    def __init__(self, cliente, conta, saldo = 0):
        self.cliente = cliente
        self.conta = conta
        self.saldo = 0
        self.operacoes = []
        self.deposito(saldo) 

    def resumo(self):
        print(f"Cliente:{self.cliente}, Conta:{self.conta}, Saldo:{self.saldo}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo Insuficiente para saque!")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])
    
    def extrato(self):
        
        print(f'Extrato de CC Nº {self.conta}')

        for i in self.operacoes:
            print(f"{i[0]}, {i[1]}")
        
        print(f'\n Saldo: {self.saldo}')