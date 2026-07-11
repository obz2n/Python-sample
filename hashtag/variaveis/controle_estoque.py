"""
Exercício 2: Controle de Estoque de E-commerce (Logística)
Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no
estoque. Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um
fornecedor. Objetivo: Atualize a variável de estoque e exiba o saldo final.
"""

smartphones = 250
total_vendas = 78
novos_smartphones = 100


def atualizar_estoque():
    saldo = smartphones - total_vendas + novos_smartphones
    print(f"O saldo final de smartphones no estoque é: {saldo} unidades")


atualizar_estoque()
