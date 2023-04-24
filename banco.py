class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.cliente = []
        self.contas = []
    
    def abre_conta(self,conta):
        self.contas.append(conta)
    
    def listas_contas(self):
        for c in self.contas:
            c.resumo()