# variaveis

velocidade_internet = 400
print(velocidade_internet)

# numeros inteiros
idade = 15

# nunmeros decimais
nota = 8.5

# textos
nome_completo = 'Raimundo Soldado'

# booleanos (True ou False)
pode_entrar = True #False

# saber o tipo de variavel
print(type(nota))


# Problema 1 - Valor por hora
# escreva um programa que retorna o valor de um funcionário
# com base no seu salario mensal e horas trabalhadas por mês


# Metodo 5'qs
# Analise criticamente o problema e descubra:
# (tente explicar este problema para você mesmo em voz alta e peça mais
# informações/investigue mais até você compreender completamente o problema.)

# 1 - Quais sao os dados de entrada necessários?

# 2 - O que devo fazer com estes dados? 

# 3 - Quais são as restrições deste problema

# 4 - Qual é o resultado esperado? 

# 5 - Qual é a sequência de passos a ser feita para chegar ao resultado esperado? 

# resumo: 
# receber salário mensal
# receber quantidade de horas trabalhadas 
# valor hora = salário mensal / quantidade de horas trabalhadas
# exibir valor hora


salario_mensal = int(input('Salario mensal: '))
horas_trabalhadas = int(input('Quantidade de horas trabalhadas: '))
valor_hora = salario_mensal / horas_trabalhadas
print(f'Valor por hora trabalhada = {valor_hora}')