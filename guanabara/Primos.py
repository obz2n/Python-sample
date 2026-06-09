num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m',end=' ')
        tot += 1
    else:
        print('\033[33m',end=' ')
    print(f'{c}',end=' ')
print('\n\033[m'f'O nùmero {num} foi divisível {tot}x')
if tot == 2:
    print('O número é PRIMO')
else:
    print('O número NÃO É PRIMO')