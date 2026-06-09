casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário atual: R$'))
anos = int(input('Digite em quantos anos deseja pagar: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Valor da R${casa:.2f} com o salário de R${salario:.2f} para pagar em {anos}x')
print(f'O valor da prestação será de {prestacao:.2f}')
if prestacao <= minimo:
    print('>Emprestimo CONCEDIDO!<')
else:
    print('>Emprestimo NEGADO!<')
