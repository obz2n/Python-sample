"""
Exercício 1: Relatório de Margem de Lucro (Setor Financeiro) Uma empresa de varejo
precisa de um resumo rápido sobre a performance de um produto. Dado o faturamento de
R$ 45.000,00 e o custo de R$ 23.500,00, crie um programa que calcule o lucro e a margem
de lucro (lucro dividido pelo faturamento). Exiba uma mensagem formatada onde o lucro
use o separador de milhar e duas casas decimais, e a margem seja exibida como uma
porcentagem inteira.
"""

faturamento = 45000
custo = 23500

lucro = faturamento - custo
margem_lucro = (lucro / faturamento) * 100

print("=" * 60)
print(f"Lucro total: R$ {lucro:,.2f}")
print(f"Margem de lucro: {margem_lucro:.0f}%")
print("=" * 60)
