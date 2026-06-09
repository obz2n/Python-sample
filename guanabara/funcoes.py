# exemplo de funções

# funções locais
# exemplo colocando a variavel nome dentro da função e tentando chamar fora da função
# não funciona por ser local
'''
def minha_funcao():
    nome = 'juliano'
    print('Esta é uma função no python')
minha_funcao()
print(nome)

'''
# --funções globais--
# exemplo colocando a variável nome conmpleto fora da função e tentando chamar dentro da função 
# funciona por ser global
nome = 'juliano'

def minha_funcao():
    print(f'Este é o meu nome: {nome}')
minha_funcao()


# --Parametros e argumentos--
# parametros é o que a função vai receber:
def somar(n1, n2):
    resultado = n1 + n2
    print(f'A soma entre {n1} e {n2} é igual a {resultado}')

# argumentos são os valores que são enviados para os parametros
somar(5,4)

# exemplo com string
def niveis(nivel):
    print(f'O seu nivel em python é: {nivel}')
niveis('Pleno')


# Fazer com que algum resultado retorne algum valor para a variável
def subtrair(n1, n2):
    resultado = n1 - n2
    return resultado
# o return aplica o valor dela para a variável
resultado_subtrair = subtrair(2,1)
print(resultado_subtrair)


# Exemplo com numeros pares
def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
verificacao = verificar_par(3)
print(verificacao)


# exemplo com lista de numeros e retornar a media 
def somar_lista(*numeros):
    resultado = 0
    for numero in numeros:
        print(numero)
        resultado += numero
    return resultado

def calcular_media(*numeros):
    qtd = len(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
        media = soma / qtd
    return media

resultado = calcular_media(7,2,4,9)
print(f'A média é {resultado}')

# exemplo informações pessoais com várias chaves e valores
def informacoes_pessoais(**informacoes):
    for chave, valor in informacoes.items():
        print(f'{chave}: {valor}')

        
informacoes_pessoais(nome="Claudio", idade=22, natural='Paraíba', cargo='Coordenador')


'''
Desafio
crie uma função que recebe um numero, e faz um contador regressivo a partir dele
'''

def contador_regressivo(numero):
    for i in range(numero, -1, -1):
        print(i)
contador_regressivo(20)

# alternativa
def contagem_regrassiva(numero):
    while True:
        print(numero)
        # numero = numero - 1
        numero-=1
        if numero < 0:
            break
contagem_regrassiva(10)




'''
crie uma função que recebe uma lista e retorn o maior numero dessa lista
'''
def maior_numero(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior
lista_numeros = [3,5,7,2,8,1]
resultado_maior = maior_numero(lista_numeros)
print(f'O maior numero da lista é: {resultado_maior}')

# alternativa
def maior_numero(lista_de_numeros):
    maior_numero = max(lista_de_numeros)
    return maior_numero
lista = [4,8,9,2,5]
maior_numero_lista = maior_numero(lista)
print(f'O maior numero da lista é {maior_numero_lista}')

