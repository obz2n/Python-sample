l1 = float(input('Digite o primeiro número: '))
l2 = float(input('Digite o segundo número: '))
l3 = float(input('Digite o terceiro número: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Com esses número dá para fazer um triangulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Com esses números não dará para fazer um triangulo!')
