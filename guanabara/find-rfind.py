frase = str(input('Escreva uma frase: ')).upper().strip()
print(f'A letra -a- aparece {frase.count("A")} vezes na frase')
print(f'A primeira letra -a- apareceu na posição: {frase.find("A")+1}')
print(f'A ultima letra -a- apareceu na posição: {frase.rfind("A")+1}')
