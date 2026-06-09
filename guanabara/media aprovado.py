# _*_ coding: utf-8 _*_

# programa para saber a media de um aluno
# com correcao e informando se o aluno passou ou repetiu de ano 


a = int(input("Primeiro Bimestre: "))
while a > 10:
    a = int(input("Nota digitada errada, digite novamente: "))
b = int(input("Segundo Bimestre: "))
while b > 10:
    b = int(input("Nota digitada errada, digite novamente: "))
c = int(input("Terceiro Bimestre: "))
while c > 10:
    c = int(input("Nota digitada errada, digite novamente: "))
d = int(input("Quarto Bimestre: "))
while d > 10:
    d = int(input("Nota digitada errada, digite novamente: "))

media = (a + b + c + d) / 4
print("Media: {}" .format(media))
if media >= 7:
    print("Aluno aprovado")
elif media < 7 and media >= 5:
    print("Aluno esta na AF")
else:
    print("Aluno reprovado")
print("Fim do Programa")


