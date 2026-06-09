nota1 = int(input('Digite a primeira nota: '))
while nota1 > 10:
    nota1 =int(input('Nota digitada errada, digite novamente: '))
nota2 = int(input('Digite a segunda nota: '))
while nota2 > 10:
    nota2 = int(input('Nota digitada errada, digite novamente: '))#

media = (nota1 + nota2) / 2
print('A média do aluno é: {:.1f}'.format(media))
if media >= 7:
    print('Aluno Aprovado')
elif media < 7 and media > 4:
    print('Aluno de Recuperação')
else:
    print("Aluno Reprovado")
