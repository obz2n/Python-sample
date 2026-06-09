num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] Para converter para BINÁRIO''\n''[ 2 ] Para converter para OCTAL''\n''[ 3 ] Para converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
while opcao != 1 and opcao !=2 and opcao !=3:
    opcao = int(input('Opção errada, digite novamente: '))
if opcao == 1:
    print(f'{num} convertido para Binário é igual a: {bin(num)}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a: {oct(num)}')
elif opcao ==3:
    print(f'{num} convertido para HEXADECIMAL é igual a: {hex(num)}')
