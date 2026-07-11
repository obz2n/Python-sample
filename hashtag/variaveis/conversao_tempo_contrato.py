"""
Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)
Cenário: Um contrato de manutenção de software tem a duração de 40 meses. O cliente
quer ver esse tempo no formato: "X anos e Y meses". Objetivo: Utilize os operadores de
divisão inteira e resto da divisão para converter os 40 meses.
"""

contrato = 40
anos = contrato // 12
meses = contrato % 12

print(f"{anos} anos e {meses} meses")
