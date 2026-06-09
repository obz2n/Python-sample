# condicionais - if elif else
'''
Eaeh, vamos tomar aquela gelada hoje?
 - Se eu terminar meu trabalho aqui eu consigo
'''

trabalho_terminado = False
if trabalho_terminado == True:
    print('Onde vai ser o gera?')
else:
    print('é pedo pivete')


'''
Eaeh, consegue me ajudar a mover essas caixas lá para fora hoje a tarde?

 - Se eu estiver livre, sim. Mas se não der, pede meu irmão pra ajudar 
'''

estou_livre = False
if estou_livre == True:
    print('ok, bora mover as caixas')
else:
    print('Meu irmão vai ter que lhe ajudar')


'''
Eu cheguei atrasado na aula. Ainda posso entrar?

 - Se for a primeira vez ou segunda vez que você chega atrasado, pode sim.
 Mas se for a terceira vez, você será suspenso. 
'''
quantidade_atraso = int(input('Quantas vezes cheguei atrasado?: '))
if quantidade_atraso == 1:
    print('Posso entrar')
elif quantidade_atraso == 2:
    print('Ainda posso entrar')
else:
    print('Serei suspenso')


# Crie um programa que recebe dois valores e exibe qual é o maior entre eles

primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

if primeiro_valor > segundo_valor:
    print(f'Primeiro valor = {primeiro_valor}\nSegundo valor = {segundo_valor}\nResultado: Primeiro valor maior que o segundo valor')
else:
    print(f'Primeiro valor = {primeiro_valor}\nSegundo valor = {segundo_valor}\nResultado: Segundo valor maior que o primeiro valor')