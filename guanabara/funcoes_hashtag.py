# Função -> um bloco de código reutilizável e organizacional

# Sintaxe 
'''
def nome_da_funcao(parametros):
    instrucao 1
    instrucao 2
    ...
    return valor (opcionaal)
'''

# exemplo
def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.2
    return imposto


preco_produto = 2500
imposto = calcular_imposto(preco_produto)
print(imposto)


# exemplo 2

def nome(valor):
    nome = print(f'Olá {valor}')

nome('Rubens')