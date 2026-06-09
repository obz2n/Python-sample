from random import randint

computador = randint(0, 10)
print("Adidinhe o número que estou pensando ")
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
