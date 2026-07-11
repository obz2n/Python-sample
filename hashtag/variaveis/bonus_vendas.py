"""
Exercício 1: Cálculo de Bônus de Vendas (RH/Vendas)
Cenário: Uma empresa decidiu dar um bônus de 10% sobre o faturamento total para a
equipe de vendas. Objetivo: Calcule o valor do bônus e o faturamento final da empresa
após subtrair esse bônus.
●​ Faturamento inicial: 50.000
●​ Percentual de bônus: 0.1
"""

percentual_bonus = 0.1
faturamento__inicial = 50000
valor_bonus = faturamento__inicial * percentual_bonus
faturamento_final = faturamento__inicial - valor_bonus
print("=" * 50)
print(f"O valor do bônus é: R${valor_bonus}")
print(f"O valor do faturamento final é: R${faturamento_final}")
print("=" * 50)
