# laços de repetição While

'''
While condicao:
    codigo a ser executado
'''

# Programa que permite 3 tentativas, antes de fechar
tentativas = 0
while tentativas < 3:
    print('Tente novamente')
    tentativas = tentativas + 1

# Quando queremos que uma ação continue acontecendo, até que um 
# critério seja satisfeito
# so pode logar, se digitar a senha correta
senha = 0
while senha != '123456':
    senha = input('Digite a senha corretamente: ')
print('Login realizado com sucesso')

# Garantir que algo está preenchido
# Só deve continuar, quanddo o usuário informar seu nome
nome = ''
while nome == '':
    nome = input('Digite novamente o seu nome: ')
print(f'Bem vindo {nome}')

# contadores dentro do while
# ser avisado as 17hrs do por do sol
# contar de hora em hora ate chegar as 17hrs
# ao chegar as 17hrs, exibir: 'Hora de ver o por do sol'

horario = 0
while horario <= 17:
    print(horario)
    horario = horario + 1
print('Hora de ver o por do sol')


# Desafio
# Crie um gerenciador de login simples, com no maximo 3 tentativas.
# (teremos apenas um unicos usuário e senha permitido)

# usuario - juliano
# senha - senha123

# Apos 3 tentativas, se o usuário estiver errado, exibir:
# "Aguarde 30 mins antes de tentar novamente!"

# Se o usuário acertar o usuário e a senha, exibir: "Login feito com sucesso"

from time import sleep

tentativas = 0
usuario = 'juliano'
senha = 'senha123'
while tentativas <= 3:
    usuario = input('Digite o seu nome: ')
    senha = input('Digite sua senha: ')
    tentativas = tentativas + 1
    if usuario != 'juliano' or senha != 'senha123':
        print('Login inválido. Tente novamente')
    elif usuario == 'juliano' and senha == 'senha123':
        print('Login realizado com sucesso')
        break
if tentativas > 3:
    print('Login falho. Aguarde 30min para uma nova tentativa')
    sleep(30)

