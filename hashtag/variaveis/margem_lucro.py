"""
Exercício 4: Análise de Margem de Lucro (Financeiro)
Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$
5.000,00 e o imposto sobre o faturamento é de 15%. Objetivo: Calcule o imposto, o lucro
líquido e a margem de lucro (Lucro / Faturamento). No final, crie uma variável booleana
chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).
"""

faturamento = 15000
custos_fixos = 5000
imposto = 0.15


imposto_pagar = faturamento * imposto
lucro_liquido = faturamento - custos_fixos - imposto_pagar
margem_lucro = lucro_liquido / faturamento
print("=" * 50)
print(f"Imposto a pagar: R${imposto_pagar}")
print(f"O lucro liquido é de : R${lucro_liquido}")
print(f"A margem de lucro é: R${margem_lucro}")
print("=" * 50)


def verificar_meta(margem_lucro):
    if margem_lucro > 0.30:
        return "Sim"
    else:
        return "Não"


meta_atingida = verificar_meta(margem_lucro)
print("Verificar Meta")
print(f"Meta atingida? {meta_atingida}")
print("=" * 50)
