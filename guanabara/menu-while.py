from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Maior  \n[ 4 ] Outros Números \n[ 5 ] Sair do Programa')
    opcao = int(input('Escolha a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'\n>>>> A Soma entre {n1} e {n2} é: {soma}\n')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'\n>>>> A multiplicação entre {n1} e {n2} é: {multiplicacao}\n')
    elif opcao == 3:
        if n1 > n2:
            print(f'\n>>>> {n1} é maior que {n2}\n')
        elif n1 < n2:
            print(f'\n>>>> {n2} é maior que {n1}\n')
    elif opcao == 4:
        print('\n>>>> Informe os números novamente: <<<<\n')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('\nOpção inválida, tente novamente\n')
print('Fim do Programa')
