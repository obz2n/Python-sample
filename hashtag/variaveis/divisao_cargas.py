"""
Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. Cada
caminhão suporta exatamente 12 caixas. Objetivo: 1. Quantos caminhões sairão
totalmente cheios? (Use //) 2. Quantas caixas sobrarão para serem enviadas em uma
última viagem menor? (Use %)
"""

caixas = 1250
caminhoes = caixas // 12
caixas_restantes = caixas % 12

print(f"Total de caminhões: {caminhoes}")
print(f"Caixas restantes: {caixas_restantes}")
