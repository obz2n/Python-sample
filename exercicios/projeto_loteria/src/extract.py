import datetime
import os
from random import randint

class fazerFezinha:
    def __init__(self, numeros):
        self.numeros = numeros

    def criar_bilhete(self):
        self.numeros = int(input("Digite o 1º número do bilhete: "))
        for i in range(5):
            numero = int(input(f"Digite o {i+2}º número do bilhete: "))
            self.numeros = [self.numeros, numero] if isinstance(self.numeros, int) else self.numeros + [numero]
        print(f"Bilhete recebido com os números: {self.numeros}")

    def realizar_pagamento(self):
        pagamento = {'1': 'Cartão', '2': 'Dinheiro'}
        print(f'Seguintes formas de pagamento: {pagamento}')

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

    def registrar_bilhete(self):
        if hasattr(self, 'numeros'):
            print(f"Registrando bilhete com números: {self.numeros}")
        else:
            print("Bilhete não recebido.")

    def encerrar_operacao(self):
        print("Operação encerrada.")

if __name__ == "__main__":
    bilhete = fazerFezinha([])
    bilhete.criar_bilhete()
    bilhete.realizar_pagamento()
    #bilhete.confirmar_pagamento()
    #bilhete.inserir_pagamento_banco()
    #bilhete.registrar_bilhete()
    #bilhete.encerrar_operacao()
