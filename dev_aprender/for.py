# laços de repetição For

for item in range(3):
    print('item')

'''
for item in colecao:
    comandos
'''

# Range nunca inclui o ultimo numero

for item in range(10):
    print(item)

# Definindo um valor inicial

for item in range(1,10):
    print(item)

# Definindo passo

for item in range(1,10,2):
    print(item)


for item in range(2,12,2):
    print(item)


# listas
nomes = ['joao','maria','jose','raimundo']
for nome in nomes:
    print(nome)

# varios tipos dentro de uma lista
all_data = [1,'jose',True,2.5]
for data in all_data:
    print(data)
print(type(data))

# Utilizando condicionais dentro do laço
idades = [13,15,18,30,50,75]
for idade in idades:
    if idade >= 18:
        print(f'Idade: {idade} - Maior de idade')
    else:
        print(f'Idade: {idade} - Menor de idade')


'''
Desafio:
Validador de senhas

Problema:
você trabalha em um sistema que precisa verificar se todas as senhas digitadas
por usuário são válidas

Para uma senha ser válida, ela precisa ter pelo menos 6 caracteres
'''
# com variável contagem
senha = int(input('Digite a sua senha: '))
contagem = 6
if senha < contagem:
    print('Sua senha tem menos de 6 caracteres')
else:
    print('Sua senha é válida')
 
# com laço e len
senhas = []
for senha in senhas:
    if len(senha) >= 6:
        print('Senha válida')
    else:
        print('Senha inválida')