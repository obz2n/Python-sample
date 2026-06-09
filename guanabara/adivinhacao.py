from random import randint
from time import sleep
print('-=-'*10)
print('----Jogo da adivinhação----')
print('-=-'*10)
print('Vou pensar em um número de 0 a 5')
sleep(1)
player = float(input('Digite um número de 0 a 5 : '))
ramdon = int(randint(0,5))
print('Processando....')
sleep(1)
if player == ramdon:
    print('Parabéns seu sortudo, você acertou!!')
else:
    print(f'Você errou! O número que eu escolhi foi: {ramdon}')

