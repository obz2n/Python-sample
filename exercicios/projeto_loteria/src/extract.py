import sqlite3
import datetime
import os
from random import randint

class Bilhete:
    def __init__(self, numeros):
        self.numeros = numeros
    
    def receber_bilhete(self):
        self.numeros = [randint(1, 60) for _ in range(6)]
        print(f"Bilhete recebido com números: {self.numeros}")

    def perguntar_forma_pagamento(self):
        pagamento = {'1': 'Cartão', '2': 'Dinheiro'}
        
        self.forma_pagamento = input("Qual a forma de pagamento? ")
        if self.forma_pagamento in pagamento:
            pagamento = pagamento[self.forma_pagamento]
        else:
            pagamento = pagamento['2']
            troco = input("Deseja receber troco? (s/n) ")
            if troco.lower() == 's':
                print("Troco será fornecido.")
        return pagamento
    
    def confirmar_pagamento(self):
        if hasattr(self, 'forma_pagamento'):
            print(f"Pagamento confirmado via {self.forma_pagamento}")
        else:
            print("Forma de pagamento não informada.")

    def inserir_pagamento_banco(self):
        if hasattr(self, 'forma_pagamento'):
            print(f"Inserindo pagamento no banco via {self.forma_pagamento}")
        else:
            print("Forma de pagamento não informada.")

    def registrar_bilhete(self):
        if hasattr(self, 'numeros'):
            print(f"Registrando bilhete com números: {self.numeros}")
        else:
            print("Bilhete não recebido.")

    def encerrar_operacao(self):
        print("Operação encerrada.")