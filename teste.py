from cliente import Cliente
from contas import Conta

joao = Cliente(8941202710,'João', 21998306499)
maria = Cliente(8941202712,'Maria', 21985344474)

c1 = Conta('João',1,1000)

c1.saque(50)
c1.deposito(300)
c1.extrato()