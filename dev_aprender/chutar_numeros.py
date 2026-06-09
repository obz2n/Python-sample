# Desafio

# Escreva um programa que, ao iniciar, gere um valor aleatorio de 1 a 10 e permita
# que o usuário chute numero ate acertar p valor gerado

# o programa deve informar se o chute foi maior, menor ou igual ao valor aleatorio gerado no inicio

import random

numero_random = random.randint(1, 10)
numero_usuario = int(input("Chute um numero de 1 a 10: "))
while True:
    if numero_usuario > numero_random:
        print("Errou! Seu numero é maior.")
        numero_usuario = int(input("Chute novamente: "))
    elif numero_usuario < numero_random:
        print("Errou! Seu numero é menor.")
        numero_usuario = int(input("Chute novamente: "))
    else:
        print("Parabens! Voce acertou!")
        break


# Solução com contador de palpites

from random import randint

computador = randint(0, 10)
print("Adivinhe o número que estou pensando ")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais...Tente mais um vez.")
        elif jogador > computador:
            print("Menos...Tente mais uma vez.")
print(f"Acertou com {palpite} tentativas. Parabéns!")
